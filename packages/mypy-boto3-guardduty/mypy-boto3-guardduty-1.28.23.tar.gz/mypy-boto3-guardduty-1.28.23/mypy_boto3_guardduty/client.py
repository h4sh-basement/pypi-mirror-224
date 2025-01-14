"""
Type annotations for guardduty service client.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client/)

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_guardduty.client import GuardDutyClient

    session = Session()
    client: GuardDutyClient = session.client("guardduty")
    ```
"""
import sys
from typing import Any, Dict, Mapping, Sequence, Type, overload

from botocore.client import BaseClient, ClientMeta

from .literals import (
    AutoEnableMembersType,
    CoverageStatisticsTypeType,
    EbsSnapshotPreservationType,
    FeedbackType,
    FilterActionType,
    FindingPublishingFrequencyType,
    IpSetFormatType,
    ThreatIntelSetFormatType,
    UsageStatisticTypeType,
)
from .paginator import (
    DescribeMalwareScansPaginator,
    ListCoveragePaginator,
    ListDetectorsPaginator,
    ListFiltersPaginator,
    ListFindingsPaginator,
    ListInvitationsPaginator,
    ListIPSetsPaginator,
    ListMembersPaginator,
    ListOrganizationAdminAccountsPaginator,
    ListThreatIntelSetsPaginator,
)
from .type_defs import (
    AccountDetailTypeDef,
    CoverageFilterCriteriaTypeDef,
    CoverageSortCriteriaTypeDef,
    CreateDetectorResponseTypeDef,
    CreateFilterResponseTypeDef,
    CreateIPSetResponseTypeDef,
    CreateMembersResponseTypeDef,
    CreatePublishingDestinationResponseTypeDef,
    CreateThreatIntelSetResponseTypeDef,
    DataSourceConfigurationsTypeDef,
    DeclineInvitationsResponseTypeDef,
    DeleteInvitationsResponseTypeDef,
    DeleteMembersResponseTypeDef,
    DescribeMalwareScansResponseTypeDef,
    DescribeOrganizationConfigurationResponseTypeDef,
    DescribePublishingDestinationResponseTypeDef,
    DestinationPropertiesTypeDef,
    DetectorFeatureConfigurationTypeDef,
    DisassociateMembersResponseTypeDef,
    FilterCriteriaTypeDef,
    FindingCriteriaTypeDef,
    GetAdministratorAccountResponseTypeDef,
    GetCoverageStatisticsResponseTypeDef,
    GetDetectorResponseTypeDef,
    GetFilterResponseTypeDef,
    GetFindingsResponseTypeDef,
    GetFindingsStatisticsResponseTypeDef,
    GetInvitationsCountResponseTypeDef,
    GetIPSetResponseTypeDef,
    GetMalwareScanSettingsResponseTypeDef,
    GetMasterAccountResponseTypeDef,
    GetMemberDetectorsResponseTypeDef,
    GetMembersResponseTypeDef,
    GetRemainingFreeTrialDaysResponseTypeDef,
    GetThreatIntelSetResponseTypeDef,
    GetUsageStatisticsResponseTypeDef,
    InviteMembersResponseTypeDef,
    ListCoverageResponseTypeDef,
    ListDetectorsResponseTypeDef,
    ListFiltersResponseTypeDef,
    ListFindingsResponseTypeDef,
    ListInvitationsResponseTypeDef,
    ListIPSetsResponseTypeDef,
    ListMembersResponseTypeDef,
    ListOrganizationAdminAccountsResponseTypeDef,
    ListPublishingDestinationsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListThreatIntelSetsResponseTypeDef,
    MemberFeaturesConfigurationTypeDef,
    OrganizationDataSourceConfigurationsTypeDef,
    OrganizationFeatureConfigurationTypeDef,
    ScanResourceCriteriaTypeDef,
    SortCriteriaTypeDef,
    StartMalwareScanResponseTypeDef,
    StartMonitoringMembersResponseTypeDef,
    StopMonitoringMembersResponseTypeDef,
    UpdateFilterResponseTypeDef,
    UpdateMemberDetectorsResponseTypeDef,
    UsageCriteriaTypeDef,
)

if sys.version_info >= (3, 9):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("GuardDutyClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    BadRequestException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerErrorException: Type[BotocoreClientError]


class GuardDutyClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        GuardDutyClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.exceptions)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client/#exceptions)
        """

    def accept_administrator_invitation(
        self, *, DetectorId: str, AdministratorId: str, InvitationId: str
    ) -> Dict[str, Any]:
        """
        Accepts the invitation to be a member account and get monitored by a GuardDuty
        administrator account that sent the invitation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.accept_administrator_invitation)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client/#accept_administrator_invitation)
        """

    def accept_invitation(
        self, *, DetectorId: str, MasterId: str, InvitationId: str
    ) -> Dict[str, Any]:
        """
        Accepts the invitation to be monitored by a GuardDuty administrator account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.accept_invitation)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client/#accept_invitation)
        """

    def archive_findings(self, *, DetectorId: str, FindingIds: Sequence[str]) -> Dict[str, Any]:
        """
        Archives GuardDuty findings that are specified by the list of finding IDs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.archive_findings)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client/#archive_findings)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.can_paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client/#can_paginate)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.close)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client/#close)
        """

    def create_detector(
        self,
        *,
        Enable: bool,
        ClientToken: str = ...,
        FindingPublishingFrequency: FindingPublishingFrequencyType = ...,
        DataSources: DataSourceConfigurationsTypeDef = ...,
        Tags: Mapping[str, str] = ...,
        Features: Sequence[DetectorFeatureConfigurationTypeDef] = ...
    ) -> CreateDetectorResponseTypeDef:
        """
        Creates a single Amazon GuardDuty detector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.create_detector)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client/#create_detector)
        """

    def create_filter(
        self,
        *,
        DetectorId: str,
        Name: str,
        FindingCriteria: FindingCriteriaTypeDef,
        Description: str = ...,
        Action: FilterActionType = ...,
        Rank: int = ...,
        ClientToken: str = ...,
        Tags: Mapping[str, str] = ...
    ) -> CreateFilterResponseTypeDef:
        """
        Creates a filter using the specified finding criteria.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.create_filter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client/#create_filter)
        """

    def create_ip_set(
        self,
        *,
        DetectorId: str,
        Name: str,
        Format: IpSetFormatType,
        Location: str,
        Activate: bool,
        ClientToken: str = ...,
        Tags: Mapping[str, str] = ...
    ) -> CreateIPSetResponseTypeDef:
        """
        Creates a new IPSet, which is called a trusted IP list in the console user
        interface.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.create_ip_set)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client/#create_ip_set)
        """

    def create_members(
        self, *, DetectorId: str, AccountDetails: Sequence[AccountDetailTypeDef]
    ) -> CreateMembersResponseTypeDef:
        """
        Creates member accounts of the current Amazon Web Services account by specifying
        a list of Amazon Web Services account IDs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.create_members)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client/#create_members)
        """

    def create_publishing_destination(
        self,
        *,
        DetectorId: str,
        DestinationType: Literal["S3"],
        DestinationProperties: DestinationPropertiesTypeDef,
        ClientToken: str = ...
    ) -> CreatePublishingDestinationResponseTypeDef:
        """
        Creates a publishing destination to export findings to.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.create_publishing_destination)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client/#create_publishing_destination)
        """

    def create_sample_findings(
        self, *, DetectorId: str, FindingTypes: Sequence[str] = ...
    ) -> Dict[str, Any]:
        """
        Generates sample findings of types specified by the list of finding types.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.create_sample_findings)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client/#create_sample_findings)
        """

    def create_threat_intel_set(
        self,
        *,
        DetectorId: str,
        Name: str,
        Format: ThreatIntelSetFormatType,
        Location: str,
        Activate: bool,
        ClientToken: str = ...,
        Tags: Mapping[str, str] = ...
    ) -> CreateThreatIntelSetResponseTypeDef:
        """
        Creates a new ThreatIntelSet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.create_threat_intel_set)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client/#create_threat_intel_set)
        """

    def decline_invitations(
        self, *, AccountIds: Sequence[str]
    ) -> DeclineInvitationsResponseTypeDef:
        """
        Declines invitations sent to the current member account by Amazon Web Services
        accounts specified by their account IDs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.decline_invitations)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client/#decline_invitations)
        """

    def delete_detector(self, *, DetectorId: str) -> Dict[str, Any]:
        """
        Deletes an Amazon GuardDuty detector that is specified by the detector ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.delete_detector)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client/#delete_detector)
        """

    def delete_filter(self, *, DetectorId: str, FilterName: str) -> Dict[str, Any]:
        """
        Deletes the filter specified by the filter name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.delete_filter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client/#delete_filter)
        """

    def delete_invitations(self, *, AccountIds: Sequence[str]) -> DeleteInvitationsResponseTypeDef:
        """
        Deletes invitations sent to the current member account by Amazon Web Services
        accounts specified by their account IDs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.delete_invitations)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client/#delete_invitations)
        """

    def delete_ip_set(self, *, DetectorId: str, IpSetId: str) -> Dict[str, Any]:
        """
        Deletes the IPSet specified by the `ipSetId`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.delete_ip_set)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client/#delete_ip_set)
        """

    def delete_members(
        self, *, DetectorId: str, AccountIds: Sequence[str]
    ) -> DeleteMembersResponseTypeDef:
        """
        Deletes GuardDuty member accounts (to the current GuardDuty administrator
        account) specified by the account IDs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.delete_members)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client/#delete_members)
        """

    def delete_publishing_destination(
        self, *, DetectorId: str, DestinationId: str
    ) -> Dict[str, Any]:
        """
        Deletes the publishing definition with the specified `destinationId`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.delete_publishing_destination)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client/#delete_publishing_destination)
        """

    def delete_threat_intel_set(self, *, DetectorId: str, ThreatIntelSetId: str) -> Dict[str, Any]:
        """
        Deletes the ThreatIntelSet specified by the ThreatIntelSet ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.delete_threat_intel_set)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client/#delete_threat_intel_set)
        """

    def describe_malware_scans(
        self,
        *,
        DetectorId: str,
        NextToken: str = ...,
        MaxResults: int = ...,
        FilterCriteria: FilterCriteriaTypeDef = ...,
        SortCriteria: SortCriteriaTypeDef = ...
    ) -> DescribeMalwareScansResponseTypeDef:
        """
        Returns a list of malware scans.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.describe_malware_scans)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client/#describe_malware_scans)
        """

    def describe_organization_configuration(
        self, *, DetectorId: str, MaxResults: int = ..., NextToken: str = ...
    ) -> DescribeOrganizationConfigurationResponseTypeDef:
        """
        Returns information about the account selected as the delegated administrator
        for GuardDuty.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.describe_organization_configuration)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client/#describe_organization_configuration)
        """

    def describe_publishing_destination(
        self, *, DetectorId: str, DestinationId: str
    ) -> DescribePublishingDestinationResponseTypeDef:
        """
        Returns information about the publishing destination specified by the provided
        `destinationId`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.describe_publishing_destination)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client/#describe_publishing_destination)
        """

    def disable_organization_admin_account(self, *, AdminAccountId: str) -> Dict[str, Any]:
        """
        Disables an Amazon Web Services account within the Organization as the GuardDuty
        delegated administrator.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.disable_organization_admin_account)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client/#disable_organization_admin_account)
        """

    def disassociate_from_administrator_account(self, *, DetectorId: str) -> Dict[str, Any]:
        """
        Disassociates the current GuardDuty member account from its administrator
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.disassociate_from_administrator_account)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client/#disassociate_from_administrator_account)
        """

    def disassociate_from_master_account(self, *, DetectorId: str) -> Dict[str, Any]:
        """
        Disassociates the current GuardDuty member account from its administrator
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.disassociate_from_master_account)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client/#disassociate_from_master_account)
        """

    def disassociate_members(
        self, *, DetectorId: str, AccountIds: Sequence[str]
    ) -> DisassociateMembersResponseTypeDef:
        """
        Disassociates GuardDuty member accounts (from the current administrator account)
        specified by the account IDs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.disassociate_members)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client/#disassociate_members)
        """

    def enable_organization_admin_account(self, *, AdminAccountId: str) -> Dict[str, Any]:
        """
        Enables an Amazon Web Services account within the organization as the GuardDuty
        delegated administrator.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.enable_organization_admin_account)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client/#enable_organization_admin_account)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client/#generate_presigned_url)
        """

    def get_administrator_account(
        self, *, DetectorId: str
    ) -> GetAdministratorAccountResponseTypeDef:
        """
        Provides the details for the GuardDuty administrator account associated with the
        current GuardDuty member account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.get_administrator_account)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client/#get_administrator_account)
        """

    def get_coverage_statistics(
        self,
        *,
        DetectorId: str,
        StatisticsType: Sequence[CoverageStatisticsTypeType],
        FilterCriteria: CoverageFilterCriteriaTypeDef = ...
    ) -> GetCoverageStatisticsResponseTypeDef:
        """
        Retrieves aggregated statistics for your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.get_coverage_statistics)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client/#get_coverage_statistics)
        """

    def get_detector(self, *, DetectorId: str) -> GetDetectorResponseTypeDef:
        """
        Retrieves an Amazon GuardDuty detector specified by the detectorId.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.get_detector)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client/#get_detector)
        """

    def get_filter(self, *, DetectorId: str, FilterName: str) -> GetFilterResponseTypeDef:
        """
        Returns the details of the filter specified by the filter name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.get_filter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client/#get_filter)
        """

    def get_findings(
        self, *, DetectorId: str, FindingIds: Sequence[str], SortCriteria: SortCriteriaTypeDef = ...
    ) -> GetFindingsResponseTypeDef:
        """
        Describes Amazon GuardDuty findings specified by finding IDs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.get_findings)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client/#get_findings)
        """

    def get_findings_statistics(
        self,
        *,
        DetectorId: str,
        FindingStatisticTypes: Sequence[Literal["COUNT_BY_SEVERITY"]],
        FindingCriteria: FindingCriteriaTypeDef = ...
    ) -> GetFindingsStatisticsResponseTypeDef:
        """
        Lists Amazon GuardDuty findings statistics for the specified detector ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.get_findings_statistics)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client/#get_findings_statistics)
        """

    def get_invitations_count(self) -> GetInvitationsCountResponseTypeDef:
        """
        Returns the count of all GuardDuty membership invitations that were sent to the
        current member account except the currently accepted invitation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.get_invitations_count)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client/#get_invitations_count)
        """

    def get_ip_set(self, *, DetectorId: str, IpSetId: str) -> GetIPSetResponseTypeDef:
        """
        Retrieves the IPSet specified by the `ipSetId`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.get_ip_set)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client/#get_ip_set)
        """

    def get_malware_scan_settings(
        self, *, DetectorId: str
    ) -> GetMalwareScanSettingsResponseTypeDef:
        """
        Returns the details of the malware scan settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.get_malware_scan_settings)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client/#get_malware_scan_settings)
        """

    def get_master_account(self, *, DetectorId: str) -> GetMasterAccountResponseTypeDef:
        """
        Provides the details for the GuardDuty administrator account associated with the
        current GuardDuty member account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.get_master_account)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client/#get_master_account)
        """

    def get_member_detectors(
        self, *, DetectorId: str, AccountIds: Sequence[str]
    ) -> GetMemberDetectorsResponseTypeDef:
        """
        Describes which data sources are enabled for the member account's detector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.get_member_detectors)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client/#get_member_detectors)
        """

    def get_members(
        self, *, DetectorId: str, AccountIds: Sequence[str]
    ) -> GetMembersResponseTypeDef:
        """
        Retrieves GuardDuty member accounts (of the current GuardDuty administrator
        account) specified by the account IDs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.get_members)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client/#get_members)
        """

    def get_remaining_free_trial_days(
        self, *, DetectorId: str, AccountIds: Sequence[str] = ...
    ) -> GetRemainingFreeTrialDaysResponseTypeDef:
        """
        Provides the number of days left for each data source used in the free trial
        period.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.get_remaining_free_trial_days)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client/#get_remaining_free_trial_days)
        """

    def get_threat_intel_set(
        self, *, DetectorId: str, ThreatIntelSetId: str
    ) -> GetThreatIntelSetResponseTypeDef:
        """
        Retrieves the ThreatIntelSet that is specified by the ThreatIntelSet ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.get_threat_intel_set)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client/#get_threat_intel_set)
        """

    def get_usage_statistics(
        self,
        *,
        DetectorId: str,
        UsageStatisticType: UsageStatisticTypeType,
        UsageCriteria: UsageCriteriaTypeDef,
        Unit: str = ...,
        MaxResults: int = ...,
        NextToken: str = ...
    ) -> GetUsageStatisticsResponseTypeDef:
        """
        Lists Amazon GuardDuty usage statistics over the last 30 days for the specified
        detector ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.get_usage_statistics)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client/#get_usage_statistics)
        """

    def invite_members(
        self,
        *,
        DetectorId: str,
        AccountIds: Sequence[str],
        DisableEmailNotification: bool = ...,
        Message: str = ...
    ) -> InviteMembersResponseTypeDef:
        """
        Invites Amazon Web Services accounts to become members of an organization
        administered by the Amazon Web Services account that invokes this API.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.invite_members)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client/#invite_members)
        """

    def list_coverage(
        self,
        *,
        DetectorId: str,
        NextToken: str = ...,
        MaxResults: int = ...,
        FilterCriteria: CoverageFilterCriteriaTypeDef = ...,
        SortCriteria: CoverageSortCriteriaTypeDef = ...
    ) -> ListCoverageResponseTypeDef:
        """
        Lists coverage details for your GuardDuty account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.list_coverage)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client/#list_coverage)
        """

    def list_detectors(
        self, *, MaxResults: int = ..., NextToken: str = ...
    ) -> ListDetectorsResponseTypeDef:
        """
        Lists detectorIds of all the existing Amazon GuardDuty detector resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.list_detectors)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client/#list_detectors)
        """

    def list_filters(
        self, *, DetectorId: str, MaxResults: int = ..., NextToken: str = ...
    ) -> ListFiltersResponseTypeDef:
        """
        Returns a paginated list of the current filters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.list_filters)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client/#list_filters)
        """

    def list_findings(
        self,
        *,
        DetectorId: str,
        FindingCriteria: FindingCriteriaTypeDef = ...,
        SortCriteria: SortCriteriaTypeDef = ...,
        MaxResults: int = ...,
        NextToken: str = ...
    ) -> ListFindingsResponseTypeDef:
        """
        Lists Amazon GuardDuty findings for the specified detector ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.list_findings)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client/#list_findings)
        """

    def list_invitations(
        self, *, MaxResults: int = ..., NextToken: str = ...
    ) -> ListInvitationsResponseTypeDef:
        """
        Lists all GuardDuty membership invitations that were sent to the current Amazon
        Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.list_invitations)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client/#list_invitations)
        """

    def list_ip_sets(
        self, *, DetectorId: str, MaxResults: int = ..., NextToken: str = ...
    ) -> ListIPSetsResponseTypeDef:
        """
        Lists the IPSets of the GuardDuty service specified by the detector ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.list_ip_sets)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client/#list_ip_sets)
        """

    def list_members(
        self,
        *,
        DetectorId: str,
        MaxResults: int = ...,
        NextToken: str = ...,
        OnlyAssociated: str = ...
    ) -> ListMembersResponseTypeDef:
        """
        Lists details about all member accounts for the current GuardDuty administrator
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.list_members)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client/#list_members)
        """

    def list_organization_admin_accounts(
        self, *, MaxResults: int = ..., NextToken: str = ...
    ) -> ListOrganizationAdminAccountsResponseTypeDef:
        """
        Lists the accounts configured as GuardDuty delegated administrators.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.list_organization_admin_accounts)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client/#list_organization_admin_accounts)
        """

    def list_publishing_destinations(
        self, *, DetectorId: str, MaxResults: int = ..., NextToken: str = ...
    ) -> ListPublishingDestinationsResponseTypeDef:
        """
        Returns a list of publishing destinations associated with the specified
        `detectorId`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.list_publishing_destinations)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client/#list_publishing_destinations)
        """

    def list_tags_for_resource(self, *, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        Lists tags for a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client/#list_tags_for_resource)
        """

    def list_threat_intel_sets(
        self, *, DetectorId: str, MaxResults: int = ..., NextToken: str = ...
    ) -> ListThreatIntelSetsResponseTypeDef:
        """
        Lists the ThreatIntelSets of the GuardDuty service specified by the detector ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.list_threat_intel_sets)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client/#list_threat_intel_sets)
        """

    def start_malware_scan(self, *, ResourceArn: str) -> StartMalwareScanResponseTypeDef:
        """
        Initiates the malware scan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.start_malware_scan)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client/#start_malware_scan)
        """

    def start_monitoring_members(
        self, *, DetectorId: str, AccountIds: Sequence[str]
    ) -> StartMonitoringMembersResponseTypeDef:
        """
        Turns on GuardDuty monitoring of the specified member accounts.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.start_monitoring_members)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client/#start_monitoring_members)
        """

    def stop_monitoring_members(
        self, *, DetectorId: str, AccountIds: Sequence[str]
    ) -> StopMonitoringMembersResponseTypeDef:
        """
        Stops GuardDuty monitoring for the specified member accounts.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.stop_monitoring_members)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client/#stop_monitoring_members)
        """

    def tag_resource(self, *, ResourceArn: str, Tags: Mapping[str, str]) -> Dict[str, Any]:
        """
        Adds tags to a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.tag_resource)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client/#tag_resource)
        """

    def unarchive_findings(self, *, DetectorId: str, FindingIds: Sequence[str]) -> Dict[str, Any]:
        """
        Unarchives GuardDuty findings specified by the `findingIds`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.unarchive_findings)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client/#unarchive_findings)
        """

    def untag_resource(self, *, ResourceArn: str, TagKeys: Sequence[str]) -> Dict[str, Any]:
        """
        Removes tags from a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.untag_resource)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client/#untag_resource)
        """

    def update_detector(
        self,
        *,
        DetectorId: str,
        Enable: bool = ...,
        FindingPublishingFrequency: FindingPublishingFrequencyType = ...,
        DataSources: DataSourceConfigurationsTypeDef = ...,
        Features: Sequence[DetectorFeatureConfigurationTypeDef] = ...
    ) -> Dict[str, Any]:
        """
        Updates the Amazon GuardDuty detector specified by the detectorId.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.update_detector)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client/#update_detector)
        """

    def update_filter(
        self,
        *,
        DetectorId: str,
        FilterName: str,
        Description: str = ...,
        Action: FilterActionType = ...,
        Rank: int = ...,
        FindingCriteria: FindingCriteriaTypeDef = ...
    ) -> UpdateFilterResponseTypeDef:
        """
        Updates the filter specified by the filter name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.update_filter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client/#update_filter)
        """

    def update_findings_feedback(
        self,
        *,
        DetectorId: str,
        FindingIds: Sequence[str],
        Feedback: FeedbackType,
        Comments: str = ...
    ) -> Dict[str, Any]:
        """
        Marks the specified GuardDuty findings as useful or not useful.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.update_findings_feedback)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client/#update_findings_feedback)
        """

    def update_ip_set(
        self,
        *,
        DetectorId: str,
        IpSetId: str,
        Name: str = ...,
        Location: str = ...,
        Activate: bool = ...
    ) -> Dict[str, Any]:
        """
        Updates the IPSet specified by the IPSet ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.update_ip_set)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client/#update_ip_set)
        """

    def update_malware_scan_settings(
        self,
        *,
        DetectorId: str,
        ScanResourceCriteria: ScanResourceCriteriaTypeDef = ...,
        EbsSnapshotPreservation: EbsSnapshotPreservationType = ...
    ) -> Dict[str, Any]:
        """
        Updates the malware scan settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.update_malware_scan_settings)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client/#update_malware_scan_settings)
        """

    def update_member_detectors(
        self,
        *,
        DetectorId: str,
        AccountIds: Sequence[str],
        DataSources: DataSourceConfigurationsTypeDef = ...,
        Features: Sequence[MemberFeaturesConfigurationTypeDef] = ...
    ) -> UpdateMemberDetectorsResponseTypeDef:
        """
        Contains information on member accounts to be updated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.update_member_detectors)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client/#update_member_detectors)
        """

    def update_organization_configuration(
        self,
        *,
        DetectorId: str,
        AutoEnable: bool = ...,
        DataSources: OrganizationDataSourceConfigurationsTypeDef = ...,
        Features: Sequence[OrganizationFeatureConfigurationTypeDef] = ...,
        AutoEnableOrganizationMembers: AutoEnableMembersType = ...
    ) -> Dict[str, Any]:
        """
        Configures the delegated administrator account with the provided values.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.update_organization_configuration)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client/#update_organization_configuration)
        """

    def update_publishing_destination(
        self,
        *,
        DetectorId: str,
        DestinationId: str,
        DestinationProperties: DestinationPropertiesTypeDef = ...
    ) -> Dict[str, Any]:
        """
        Updates information about the publishing destination specified by the
        `destinationId`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.update_publishing_destination)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client/#update_publishing_destination)
        """

    def update_threat_intel_set(
        self,
        *,
        DetectorId: str,
        ThreatIntelSetId: str,
        Name: str = ...,
        Location: str = ...,
        Activate: bool = ...
    ) -> Dict[str, Any]:
        """
        Updates the ThreatIntelSet specified by the ThreatIntelSet ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.update_threat_intel_set)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client/#update_threat_intel_set)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_malware_scans"]
    ) -> DescribeMalwareScansPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_coverage"]) -> ListCoveragePaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_detectors"]) -> ListDetectorsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_filters"]) -> ListFiltersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_findings"]) -> ListFindingsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_ip_sets"]) -> ListIPSetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_invitations"]
    ) -> ListInvitationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_members"]) -> ListMembersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_organization_admin_accounts"]
    ) -> ListOrganizationAdminAccountsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_threat_intel_sets"]
    ) -> ListThreatIntelSetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/guardduty.html#GuardDuty.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client/#get_paginator)
        """
