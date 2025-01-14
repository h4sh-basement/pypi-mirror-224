from __future__ import annotations

import json
import platform
from datetime import datetime

from jinja2 import ChoiceLoader, Environment, FileSystemLoader, PackageLoader

from .processors import load_processors
from ..config import load_config
from ..db import load_trace_from_db, setup_db
from ..version import __version__


class KoloPackageLoader(PackageLoader):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        # Work around UNC path mishandling:
        # https://github.com/pallets/jinja/issues/1675
        if platform.system() == "Windows":
            unc_prefix = "\\\\?\\"
            if self._template_root.startswith(unc_prefix):  # pragma: no cover
                self._template_root = self._template_root[len(unc_prefix) :]


env = Environment(
    loader=ChoiceLoader(
        (
            FileSystemLoader(""),
            KoloPackageLoader("kolo"),
        )
    )
)


def maybe_black(rendered):
    try:
        from black import format_file_contents
        from black.mode import Mode
        from black.parsing import InvalidInput
        from black.report import NothingChanged
    except ImportError:  # pragma: no cover
        return rendered

    try:
        return format_file_contents(
            rendered, fast=True, mode=Mode(magic_trailing_comma=False)
        )
    except (InvalidInput, NothingChanged):  # pragma: no cover
        return rendered


def generate_from_trace_id(
    trace_id: str,
    test_class: str,
    test_name: str,
    template_name: str = "",
) -> str:
    config = load_config()
    wal_mode = config.get("wal_mode", True)
    db_path = setup_db(wal_mode=wal_mode)
    raw_data = load_trace_from_db(db_path, trace_id, wal_mode=wal_mode)
    trace = json.loads(raw_data)

    processors = load_processors(config)

    context = {
        "_config": config,
        "_db_path": db_path,
        "_frames": trace["frames_of_interest"],
        "_trace": trace,
        "_wal_mode": wal_mode,
        "kolo_version": __version__,
        "now": datetime.utcnow(),
        "test_class": test_class,
        "test_name": test_name,
        "trace_id": trace_id,
    }
    for processor in processors:
        context.update(processor(context))

    if not template_name:
        template_name = "django_request_test.py.j2"
    template = env.get_template(template_name)
    rendered = template.render(**context)
    return maybe_black(rendered)
