import warnings
from typing import Optional
from urllib.parse import urljoin

from fiddler._version import __version__
from fiddler.api.alert_mixin import AlertMixin
from fiddler.api.baseline_mixin import BaselineMixin
# @todo: This is v1 implementation needs to have a proper v2 approach
from fiddler.api.compatibility_mixin import CompatibilityMixin
from fiddler.api.dataset_mixin import DatasetMixin
from fiddler.api.events_mixin import EventsMixin
from fiddler.api.explainability_mixin import ExplainabilityMixin
from fiddler.api.generate_schema_mixin import GenerateSchemaMixin
from fiddler.api.job_mixin import JobMixin
from fiddler.api.model_deployment_mixin import ModelDeploymentMixin
from fiddler.api.model_mixin import ModelMixin
from fiddler.api.project_mixin import ProjectMixin
from fiddler.api.webhooks_mixin import WebhookMixin
from fiddler.constants import (
    CURRENT_API_VERSION,
    FIDDLER_CLIENT_VERSION_HEADER,
    MIN_SERVER_VERSION,
)
from fiddler.libs.http_client import RequestClient
from fiddler.schema.server_info import ServerInfo
from fiddler.utils.decorators import handle_api_error_response
from fiddler.utils.helpers import match_semver, raise_not_supported
from fiddler.utils.logger import get_logger

logger = get_logger(__name__)


class FiddlerClient(
    ModelMixin,
    CompatibilityMixin,
    DatasetMixin,
    ProjectMixin,
    EventsMixin,
    JobMixin,
    BaselineMixin,
    AlertMixin,
    ExplainabilityMixin,
    ModelDeploymentMixin,
    GenerateSchemaMixin,
    WebhookMixin
):
    def __init__(
        self,
        url: Optional[str] = None,
        org_id: Optional[str] = None,
        auth_token: Optional[str] = None,
        proxies: Optional[dict] = None,
        verbose: Optional[bool] = False,
        timeout: int = 1200,  # sec
        version: int = 2,
        verify: bool = True,
        organization_name: Optional[str] = None,
    ) -> None:
        self.url = (
            url
            if url.endswith(CURRENT_API_VERSION)
            else urljoin(url, CURRENT_API_VERSION)
        )
        self.auth_token = auth_token
        self.request_headers = {'Authorization': f'Bearer {auth_token}'}
        self.request_headers.update({FIDDLER_CLIENT_VERSION_HEADER: f'{__version__}'})
        self.timeout = timeout
        self.client = RequestClient(
            base_url=self.url, headers=self.request_headers, verify=verify
        )

        # Check for duplicate params
        duplicated_params = [org_id, organization_name]
        if all(value is not None for value in duplicated_params):
            raise ValueError('Pass either org_id or organization_name')
        if all(value is None for value in duplicated_params):
            raise ValueError('Pass either org_id or organization_name')
        self.organization_name = organization_name
        if org_id:
            warnings.warn(
                'WARNING: org_id is deprecated and will be removed from future '
                'versions. Please use organization_name',
                FutureWarning,
            )

            self.organization_name = org_id

        self.server_info: ServerInfo = self._get_server_info()
        self._check_server_version()

        # Checks client's version compatibility with server
        self._check_version_compatibility()

    def _get_server_info(self) -> ServerInfo:
        response = self.client.get(
            url='server-info',
            params={'organization_name': self.organization_name},
        )

        return ServerInfo(**response.json().get('data'))

    @handle_api_error_response
    def _check_version_compatibility(self) -> None:
        params = {
            'client_version': __version__,
            'client_name': 'python-sdk',
        }
        self.client.get(
            url='version-compatibility',
            params=params,
        )

    def _check_server_version(self) -> None:
        if match_semver(self.server_info.server_version, f'>={MIN_SERVER_VERSION}'):
            return

        raise_not_supported(
            compatible_client_version='1.8',
            client_version=__version__,
            server_version=self.server_info.server_version,
        )


# Alias FiddlerClient as FiddlerApi
FiddlerApi = FiddlerClient
