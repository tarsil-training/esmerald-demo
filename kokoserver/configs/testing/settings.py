"""
Esmerald settings for kokoserver project.

Generated by 'esmerald createproject' using Esmerald 2.4.0.
"""

from typing import Optional

from esmerald.conf.enums import EnvironmentType

from ..settings import AppSettings


class TestingAppSettings(AppSettings):
    debug: bool = True
    app_name: str = "My application in testing mode."
    title: str = "My kokoserver"
    environment: Optional[str] = EnvironmentType.TESTING