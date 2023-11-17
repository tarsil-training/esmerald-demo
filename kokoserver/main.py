#!/usr/bin/env python
"""
Generated by 'esmerald createproject' using Esmerald 2.4.0.
"""
import os
import sys
from pathlib import Path

from edgy import Migrate
from esmerald import Esmerald, Include, settings

registry, database = settings.db_registry


def build_path():
    """
    Builds the path of the project and project root.
    """
    SITE_ROOT = os.path.dirname(os.path.realpath(__file__))

    if SITE_ROOT not in sys.path:
        sys.path.append(SITE_ROOT)
        sys.path.append(os.path.join(SITE_ROOT, "apps"))


def get_application():
    """
    This is optional. The function is only used for organisation purposes.
    """
    build_path()

    app = Esmerald(
        routes=[Include(namespace="kokoserver.urls")],
        on_startup=[database.connect],
        on_shutdown=[database.disconnect],
    )

    Migrate(app=app, registry=registry)
    return app


app = get_application()
