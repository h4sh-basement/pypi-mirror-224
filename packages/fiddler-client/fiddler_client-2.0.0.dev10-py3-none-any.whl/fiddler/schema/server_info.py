from typing import Dict, Optional

from pydantic import BaseModel

from fiddler.utils.semver_version import VersionInfo


class Version(VersionInfo):

    @classmethod
    def __get_validators__(cls):
        """Return a list of validator methods for pydantic models."""
        yield cls.parse


class ServerInfo(BaseModel):
    feature_flags: Dict
    server_version: Optional[Version]
