from __future__ import absolute_import

# flake8: noqa

# import apis into api package
from edgeimpulse_api.api.admin_api import AdminApi
from edgeimpulse_api.api.allows_read_only_api import AllowsReadOnlyApi
from edgeimpulse_api.api.auth_api import AuthApi
from edgeimpulse_api.api.cdn_api import CDNApi
from edgeimpulse_api.api.classify_api import ClassifyApi
from edgeimpulse_api.api.content_disposition_inline_api import ContentDispositionInlineApi
from edgeimpulse_api.api.dsp_api import DSPApi
from edgeimpulse_api.api.deployment_api import DeploymentApi
from edgeimpulse_api.api.devices_api import DevicesApi
from edgeimpulse_api.api.email_verification_api import EmailVerificationApi
from edgeimpulse_api.api.export_api import ExportApi
from edgeimpulse_api.api.health_api import HealthApi
from edgeimpulse_api.api.impulse_api import ImpulseApi
from edgeimpulse_api.api.jobs_api import JobsApi
from edgeimpulse_api.api.learn_api import LearnApi
from edgeimpulse_api.api.login_api import LoginApi
from edgeimpulse_api.api.metrics_api import MetricsApi
from edgeimpulse_api.api.optimization_api import OptimizationApi
from edgeimpulse_api.api.organization_allow_developer_profile_api import OrganizationAllowDeveloperProfileApi
from edgeimpulse_api.api.organization_allow_guest_access_api import OrganizationAllowGuestAccessApi
from edgeimpulse_api.api.organization_blocks_api import OrganizationBlocksApi
from edgeimpulse_api.api.organization_create_project_api import OrganizationCreateProjectApi
from edgeimpulse_api.api.organization_data_api import OrganizationDataApi
from edgeimpulse_api.api.organization_data_campaigns_api import OrganizationDataCampaignsApi
from edgeimpulse_api.api.organization_jobs_api import OrganizationJobsApi
from edgeimpulse_api.api.organization_pipelines_api import OrganizationPipelinesApi
from edgeimpulse_api.api.organization_portals_api import OrganizationPortalsApi
from edgeimpulse_api.api.organization_requires_admin_api import OrganizationRequiresAdminApi
from edgeimpulse_api.api.organization_requires_whitelabel_admin_api import OrganizationRequiresWhitelabelAdminApi
from edgeimpulse_api.api.organizations_api import OrganizationsApi
from edgeimpulse_api.api.performance_calibration_api import PerformanceCalibrationApi
from edgeimpulse_api.api.project_requires_admin_api import ProjectRequiresAdminApi
from edgeimpulse_api.api.projects_api import ProjectsApi
from edgeimpulse_api.api.raw_data_api import RawDataApi
from edgeimpulse_api.api.requires_sudo_api import RequiresSudoApi
from edgeimpulse_api.api.requires_third_party_auth_api_key_api import RequiresThirdPartyAuthApiKeyApi
from edgeimpulse_api.api.supports_range_api import SupportsRangeApi
from edgeimpulse_api.api.themes_api import ThemesApi
from edgeimpulse_api.api.third_party_auth_api import ThirdPartyAuthApi
from edgeimpulse_api.api.upload_portal_api import UploadPortalApi
from edgeimpulse_api.api.user_api import UserApi
from edgeimpulse_api.api.whitelabels_api import WhitelabelsApi
