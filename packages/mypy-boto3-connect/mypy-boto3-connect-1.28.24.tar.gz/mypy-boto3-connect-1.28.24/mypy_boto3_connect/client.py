"""
Type annotations for connect service client.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/)

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_connect.client import ConnectClient

    session = Session()
    client: ConnectClient = session.client("connect")
    ```
"""
import sys
from typing import Any, Dict, Mapping, Sequence, Type, overload

from botocore.client import BaseClient, ClientMeta

from .literals import (
    AgentAvailabilityTimerType,
    AgentStatusStateType,
    AgentStatusTypeType,
    ContactFlowModuleStateType,
    ContactFlowStateType,
    ContactFlowTypeType,
    DirectoryTypeType,
    EventSourceNameType,
    GroupingType,
    InstanceAttributeTypeType,
    InstanceStorageResourceTypeType,
    IntegrationTypeType,
    LexVersionType,
    MonitorCapabilityType,
    PhoneNumberCountryCodeType,
    PhoneNumberTypeType,
    QueueStatusType,
    QueueTypeType,
    QuickConnectTypeType,
    ReferenceTypeType,
    RulePublishStatusType,
    SourceTypeType,
    TaskTemplateStatusType,
    TrafficTypeType,
    UseCaseTypeType,
    VocabularyLanguageCodeType,
    VocabularyStateType,
)
from .paginator import (
    GetMetricDataPaginator,
    ListAgentStatusesPaginator,
    ListApprovedOriginsPaginator,
    ListBotsPaginator,
    ListContactEvaluationsPaginator,
    ListContactFlowModulesPaginator,
    ListContactFlowsPaginator,
    ListContactReferencesPaginator,
    ListDefaultVocabulariesPaginator,
    ListEvaluationFormsPaginator,
    ListEvaluationFormVersionsPaginator,
    ListHoursOfOperationsPaginator,
    ListInstanceAttributesPaginator,
    ListInstancesPaginator,
    ListInstanceStorageConfigsPaginator,
    ListIntegrationAssociationsPaginator,
    ListLambdaFunctionsPaginator,
    ListLexBotsPaginator,
    ListPhoneNumbersPaginator,
    ListPhoneNumbersV2Paginator,
    ListPromptsPaginator,
    ListQueueQuickConnectsPaginator,
    ListQueuesPaginator,
    ListQuickConnectsPaginator,
    ListRoutingProfileQueuesPaginator,
    ListRoutingProfilesPaginator,
    ListRulesPaginator,
    ListSecurityKeysPaginator,
    ListSecurityProfilePermissionsPaginator,
    ListSecurityProfilesPaginator,
    ListTaskTemplatesPaginator,
    ListTrafficDistributionGroupsPaginator,
    ListTrafficDistributionGroupUsersPaginator,
    ListUseCasesPaginator,
    ListUserHierarchyGroupsPaginator,
    ListUsersPaginator,
    SearchAvailablePhoneNumbersPaginator,
    SearchHoursOfOperationsPaginator,
    SearchPromptsPaginator,
    SearchQueuesPaginator,
    SearchQuickConnectsPaginator,
    SearchResourceTagsPaginator,
    SearchRoutingProfilesPaginator,
    SearchSecurityProfilesPaginator,
    SearchUsersPaginator,
    SearchVocabulariesPaginator,
)
from .type_defs import (
    ActivateEvaluationFormResponseTypeDef,
    AgentConfigTypeDef,
    AnswerMachineDetectionConfigTypeDef,
    AssociateInstanceStorageConfigResponseTypeDef,
    AssociateSecurityKeyResponseTypeDef,
    ChatMessageTypeDef,
    ChatStreamingConfigurationTypeDef,
    ClaimPhoneNumberResponseTypeDef,
    CreateAgentStatusResponseTypeDef,
    CreateContactFlowModuleResponseTypeDef,
    CreateContactFlowResponseTypeDef,
    CreateEvaluationFormResponseTypeDef,
    CreateHoursOfOperationResponseTypeDef,
    CreateInstanceResponseTypeDef,
    CreateIntegrationAssociationResponseTypeDef,
    CreateParticipantResponseTypeDef,
    CreatePromptResponseTypeDef,
    CreateQueueResponseTypeDef,
    CreateQuickConnectResponseTypeDef,
    CreateRoutingProfileResponseTypeDef,
    CreateRuleResponseTypeDef,
    CreateSecurityProfileResponseTypeDef,
    CreateTaskTemplateResponseTypeDef,
    CreateTrafficDistributionGroupResponseTypeDef,
    CreateUseCaseResponseTypeDef,
    CreateUserHierarchyGroupResponseTypeDef,
    CreateUserResponseTypeDef,
    CreateVocabularyResponseTypeDef,
    CurrentMetricSortCriteriaTypeDef,
    CurrentMetricTypeDef,
    DeactivateEvaluationFormResponseTypeDef,
    DeleteVocabularyResponseTypeDef,
    DescribeAgentStatusResponseTypeDef,
    DescribeContactEvaluationResponseTypeDef,
    DescribeContactFlowModuleResponseTypeDef,
    DescribeContactFlowResponseTypeDef,
    DescribeContactResponseTypeDef,
    DescribeEvaluationFormResponseTypeDef,
    DescribeHoursOfOperationResponseTypeDef,
    DescribeInstanceAttributeResponseTypeDef,
    DescribeInstanceResponseTypeDef,
    DescribeInstanceStorageConfigResponseTypeDef,
    DescribePhoneNumberResponseTypeDef,
    DescribePromptResponseTypeDef,
    DescribeQueueResponseTypeDef,
    DescribeQuickConnectResponseTypeDef,
    DescribeRoutingProfileResponseTypeDef,
    DescribeRuleResponseTypeDef,
    DescribeSecurityProfileResponseTypeDef,
    DescribeTrafficDistributionGroupResponseTypeDef,
    DescribeUserHierarchyGroupResponseTypeDef,
    DescribeUserHierarchyStructureResponseTypeDef,
    DescribeUserResponseTypeDef,
    DescribeVocabularyResponseTypeDef,
    EmptyResponseMetadataTypeDef,
    EvaluationAnswerInputTypeDef,
    EvaluationFormItemTypeDef,
    EvaluationFormScoringStrategyTypeDef,
    EvaluationNoteTypeDef,
    FiltersTypeDef,
    FilterV2TypeDef,
    GetContactAttributesResponseTypeDef,
    GetCurrentMetricDataResponseTypeDef,
    GetCurrentUserDataResponseTypeDef,
    GetFederationTokenResponseTypeDef,
    GetMetricDataResponseTypeDef,
    GetMetricDataV2ResponseTypeDef,
    GetPromptFileResponseTypeDef,
    GetTaskTemplateResponseTypeDef,
    GetTrafficDistributionResponseTypeDef,
    HierarchyStructureUpdateTypeDef,
    HistoricalMetricTypeDef,
    HoursOfOperationConfigTypeDef,
    HoursOfOperationSearchCriteriaTypeDef,
    HoursOfOperationSearchFilterTypeDef,
    InstanceStorageConfigTypeDef,
    LexBotTypeDef,
    LexV2BotTypeDef,
    ListAgentStatusResponseTypeDef,
    ListApprovedOriginsResponseTypeDef,
    ListBotsResponseTypeDef,
    ListContactEvaluationsResponseTypeDef,
    ListContactFlowModulesResponseTypeDef,
    ListContactFlowsResponseTypeDef,
    ListContactReferencesResponseTypeDef,
    ListDefaultVocabulariesResponseTypeDef,
    ListEvaluationFormsResponseTypeDef,
    ListEvaluationFormVersionsResponseTypeDef,
    ListHoursOfOperationsResponseTypeDef,
    ListInstanceAttributesResponseTypeDef,
    ListInstancesResponseTypeDef,
    ListInstanceStorageConfigsResponseTypeDef,
    ListIntegrationAssociationsResponseTypeDef,
    ListLambdaFunctionsResponseTypeDef,
    ListLexBotsResponseTypeDef,
    ListPhoneNumbersResponseTypeDef,
    ListPhoneNumbersV2ResponseTypeDef,
    ListPromptsResponseTypeDef,
    ListQueueQuickConnectsResponseTypeDef,
    ListQueuesResponseTypeDef,
    ListQuickConnectsResponseTypeDef,
    ListRoutingProfileQueuesResponseTypeDef,
    ListRoutingProfilesResponseTypeDef,
    ListRulesResponseTypeDef,
    ListSecurityKeysResponseTypeDef,
    ListSecurityProfilePermissionsResponseTypeDef,
    ListSecurityProfilesResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTaskTemplatesResponseTypeDef,
    ListTrafficDistributionGroupsResponseTypeDef,
    ListTrafficDistributionGroupUsersResponseTypeDef,
    ListUseCasesResponseTypeDef,
    ListUserHierarchyGroupsResponseTypeDef,
    ListUsersResponseTypeDef,
    MediaConcurrencyTypeDef,
    MetricV2TypeDef,
    MonitorContactResponseTypeDef,
    OutboundCallerConfigTypeDef,
    ParticipantDetailsToAddTypeDef,
    ParticipantDetailsTypeDef,
    PersistentChatTypeDef,
    PromptSearchCriteriaTypeDef,
    PromptSearchFilterTypeDef,
    QueueSearchCriteriaTypeDef,
    QueueSearchFilterTypeDef,
    QuickConnectConfigTypeDef,
    QuickConnectSearchCriteriaTypeDef,
    QuickConnectSearchFilterTypeDef,
    ReferenceTypeDef,
    ReplicateInstanceResponseTypeDef,
    ResourceTagsSearchCriteriaTypeDef,
    RoutingProfileQueueConfigTypeDef,
    RoutingProfileQueueReferenceTypeDef,
    RoutingProfileSearchCriteriaTypeDef,
    RoutingProfileSearchFilterTypeDef,
    RuleActionTypeDef,
    RuleTriggerEventSourceTypeDef,
    SearchAvailablePhoneNumbersResponseTypeDef,
    SearchHoursOfOperationsResponseTypeDef,
    SearchPromptsResponseTypeDef,
    SearchQueuesResponseTypeDef,
    SearchQuickConnectsResponseTypeDef,
    SearchResourceTagsResponseTypeDef,
    SearchRoutingProfilesResponseTypeDef,
    SearchSecurityProfilesResponseTypeDef,
    SearchUsersResponseTypeDef,
    SearchVocabulariesResponseTypeDef,
    SecurityProfileSearchCriteriaTypeDef,
    SecurityProfilesSearchFilterTypeDef,
    SignInConfigTypeDef,
    StartChatContactResponseTypeDef,
    StartContactEvaluationResponseTypeDef,
    StartContactStreamingResponseTypeDef,
    StartOutboundVoiceContactResponseTypeDef,
    StartTaskContactResponseTypeDef,
    SubmitContactEvaluationResponseTypeDef,
    TaskTemplateConstraintsTypeDef,
    TaskTemplateDefaultsTypeDef,
    TaskTemplateFieldTypeDef,
    TelephonyConfigTypeDef,
    TimestampTypeDef,
    TransferContactResponseTypeDef,
    UpdateContactEvaluationResponseTypeDef,
    UpdateEvaluationFormResponseTypeDef,
    UpdateParticipantRoleConfigChannelInfoTypeDef,
    UpdatePhoneNumberResponseTypeDef,
    UpdatePromptResponseTypeDef,
    UpdateTaskTemplateResponseTypeDef,
    UserDataFiltersTypeDef,
    UserIdentityInfoTypeDef,
    UserPhoneConfigTypeDef,
    UserSearchCriteriaTypeDef,
    UserSearchFilterTypeDef,
    VoiceRecordingConfigurationTypeDef,
)

if sys.version_info >= (3, 9):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ConnectClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ContactFlowNotPublishedException: Type[BotocoreClientError]
    ContactNotFoundException: Type[BotocoreClientError]
    DestinationNotAllowedException: Type[BotocoreClientError]
    DuplicateResourceException: Type[BotocoreClientError]
    IdempotencyException: Type[BotocoreClientError]
    InternalServiceException: Type[BotocoreClientError]
    InvalidContactFlowException: Type[BotocoreClientError]
    InvalidContactFlowModuleException: Type[BotocoreClientError]
    InvalidParameterException: Type[BotocoreClientError]
    InvalidRequestException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    MaximumResultReturnedException: Type[BotocoreClientError]
    OutboundContactNotPermittedException: Type[BotocoreClientError]
    PropertyValidationException: Type[BotocoreClientError]
    ResourceConflictException: Type[BotocoreClientError]
    ResourceInUseException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ResourceNotReadyException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    UserNotFoundException: Type[BotocoreClientError]


class ConnectClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        ConnectClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.exceptions)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#exceptions)
        """

    def activate_evaluation_form(
        self, *, InstanceId: str, EvaluationFormId: str, EvaluationFormVersion: int
    ) -> ActivateEvaluationFormResponseTypeDef:
        """
        Activates an evaluation form in the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.activate_evaluation_form)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#activate_evaluation_form)
        """

    def associate_approved_origin(
        self, *, InstanceId: str, Origin: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.associate_approved_origin)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#associate_approved_origin)
        """

    def associate_bot(
        self, *, InstanceId: str, LexBot: LexBotTypeDef = ..., LexV2Bot: LexV2BotTypeDef = ...
    ) -> EmptyResponseMetadataTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.associate_bot)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#associate_bot)
        """

    def associate_default_vocabulary(
        self, *, InstanceId: str, LanguageCode: VocabularyLanguageCodeType, VocabularyId: str = ...
    ) -> Dict[str, Any]:
        """
        Associates an existing vocabulary as the default.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.associate_default_vocabulary)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#associate_default_vocabulary)
        """

    def associate_instance_storage_config(
        self,
        *,
        InstanceId: str,
        ResourceType: InstanceStorageResourceTypeType,
        StorageConfig: InstanceStorageConfigTypeDef
    ) -> AssociateInstanceStorageConfigResponseTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.associate_instance_storage_config)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#associate_instance_storage_config)
        """

    def associate_lambda_function(
        self, *, InstanceId: str, FunctionArn: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.associate_lambda_function)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#associate_lambda_function)
        """

    def associate_lex_bot(
        self, *, InstanceId: str, LexBot: LexBotTypeDef
    ) -> EmptyResponseMetadataTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.associate_lex_bot)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#associate_lex_bot)
        """

    def associate_phone_number_contact_flow(
        self, *, PhoneNumberId: str, InstanceId: str, ContactFlowId: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Associates a flow with a phone number claimed to your Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.associate_phone_number_contact_flow)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#associate_phone_number_contact_flow)
        """

    def associate_queue_quick_connects(
        self, *, InstanceId: str, QueueId: str, QuickConnectIds: Sequence[str]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.associate_queue_quick_connects)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#associate_queue_quick_connects)
        """

    def associate_routing_profile_queues(
        self,
        *,
        InstanceId: str,
        RoutingProfileId: str,
        QueueConfigs: Sequence[RoutingProfileQueueConfigTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Associates a set of queues with a routing profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.associate_routing_profile_queues)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#associate_routing_profile_queues)
        """

    def associate_security_key(
        self, *, InstanceId: str, Key: str
    ) -> AssociateSecurityKeyResponseTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.associate_security_key)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#associate_security_key)
        """

    def associate_traffic_distribution_group_user(
        self, *, TrafficDistributionGroupId: str, UserId: str, InstanceId: str
    ) -> Dict[str, Any]:
        """
        Associates an agent with a traffic distribution group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.associate_traffic_distribution_group_user)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#associate_traffic_distribution_group_user)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.can_paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#can_paginate)
        """

    def claim_phone_number(
        self,
        *,
        TargetArn: str,
        PhoneNumber: str,
        PhoneNumberDescription: str = ...,
        Tags: Mapping[str, str] = ...,
        ClientToken: str = ...
    ) -> ClaimPhoneNumberResponseTypeDef:
        """
        Claims an available phone number to your Amazon Connect instance or traffic
        distribution group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.claim_phone_number)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#claim_phone_number)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.close)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#close)
        """

    def create_agent_status(
        self,
        *,
        InstanceId: str,
        Name: str,
        State: AgentStatusStateType,
        Description: str = ...,
        DisplayOrder: int = ...,
        Tags: Mapping[str, str] = ...
    ) -> CreateAgentStatusResponseTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.create_agent_status)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#create_agent_status)
        """

    def create_contact_flow(
        self,
        *,
        InstanceId: str,
        Name: str,
        Type: ContactFlowTypeType,
        Content: str,
        Description: str = ...,
        Tags: Mapping[str, str] = ...
    ) -> CreateContactFlowResponseTypeDef:
        """
        Creates a flow for the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.create_contact_flow)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#create_contact_flow)
        """

    def create_contact_flow_module(
        self,
        *,
        InstanceId: str,
        Name: str,
        Content: str,
        Description: str = ...,
        Tags: Mapping[str, str] = ...,
        ClientToken: str = ...
    ) -> CreateContactFlowModuleResponseTypeDef:
        """
        Creates a flow module for the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.create_contact_flow_module)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#create_contact_flow_module)
        """

    def create_evaluation_form(
        self,
        *,
        InstanceId: str,
        Title: str,
        Items: Sequence["EvaluationFormItemTypeDef"],
        Description: str = ...,
        ScoringStrategy: EvaluationFormScoringStrategyTypeDef = ...,
        ClientToken: str = ...
    ) -> CreateEvaluationFormResponseTypeDef:
        """
        Creates an evaluation form in the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.create_evaluation_form)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#create_evaluation_form)
        """

    def create_hours_of_operation(
        self,
        *,
        InstanceId: str,
        Name: str,
        TimeZone: str,
        Config: Sequence[HoursOfOperationConfigTypeDef],
        Description: str = ...,
        Tags: Mapping[str, str] = ...
    ) -> CreateHoursOfOperationResponseTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.create_hours_of_operation)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#create_hours_of_operation)
        """

    def create_instance(
        self,
        *,
        IdentityManagementType: DirectoryTypeType,
        InboundCallsEnabled: bool,
        OutboundCallsEnabled: bool,
        ClientToken: str = ...,
        InstanceAlias: str = ...,
        DirectoryId: str = ...
    ) -> CreateInstanceResponseTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.create_instance)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#create_instance)
        """

    def create_integration_association(
        self,
        *,
        InstanceId: str,
        IntegrationType: IntegrationTypeType,
        IntegrationArn: str,
        SourceApplicationUrl: str = ...,
        SourceApplicationName: str = ...,
        SourceType: SourceTypeType = ...,
        Tags: Mapping[str, str] = ...
    ) -> CreateIntegrationAssociationResponseTypeDef:
        """
        Creates an Amazon Web Services resource association with an Amazon Connect
        instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.create_integration_association)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#create_integration_association)
        """

    def create_participant(
        self,
        *,
        InstanceId: str,
        ContactId: str,
        ParticipantDetails: ParticipantDetailsToAddTypeDef,
        ClientToken: str = ...
    ) -> CreateParticipantResponseTypeDef:
        """
        Adds a new participant into an on-going chat contact.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.create_participant)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#create_participant)
        """

    def create_prompt(
        self,
        *,
        InstanceId: str,
        Name: str,
        S3Uri: str,
        Description: str = ...,
        Tags: Mapping[str, str] = ...
    ) -> CreatePromptResponseTypeDef:
        """
        Creates a prompt.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.create_prompt)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#create_prompt)
        """

    def create_queue(
        self,
        *,
        InstanceId: str,
        Name: str,
        HoursOfOperationId: str,
        Description: str = ...,
        OutboundCallerConfig: OutboundCallerConfigTypeDef = ...,
        MaxContacts: int = ...,
        QuickConnectIds: Sequence[str] = ...,
        Tags: Mapping[str, str] = ...
    ) -> CreateQueueResponseTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.create_queue)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#create_queue)
        """

    def create_quick_connect(
        self,
        *,
        InstanceId: str,
        Name: str,
        QuickConnectConfig: QuickConnectConfigTypeDef,
        Description: str = ...,
        Tags: Mapping[str, str] = ...
    ) -> CreateQuickConnectResponseTypeDef:
        """
        Creates a quick connect for the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.create_quick_connect)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#create_quick_connect)
        """

    def create_routing_profile(
        self,
        *,
        InstanceId: str,
        Name: str,
        Description: str,
        DefaultOutboundQueueId: str,
        MediaConcurrencies: Sequence[MediaConcurrencyTypeDef],
        QueueConfigs: Sequence[RoutingProfileQueueConfigTypeDef] = ...,
        Tags: Mapping[str, str] = ...,
        AgentAvailabilityTimer: AgentAvailabilityTimerType = ...
    ) -> CreateRoutingProfileResponseTypeDef:
        """
        Creates a new routing profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.create_routing_profile)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#create_routing_profile)
        """

    def create_rule(
        self,
        *,
        InstanceId: str,
        Name: str,
        TriggerEventSource: RuleTriggerEventSourceTypeDef,
        Function: str,
        Actions: Sequence[RuleActionTypeDef],
        PublishStatus: RulePublishStatusType,
        ClientToken: str = ...
    ) -> CreateRuleResponseTypeDef:
        """
        Creates a rule for the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.create_rule)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#create_rule)
        """

    def create_security_profile(
        self,
        *,
        SecurityProfileName: str,
        InstanceId: str,
        Description: str = ...,
        Permissions: Sequence[str] = ...,
        Tags: Mapping[str, str] = ...,
        AllowedAccessControlTags: Mapping[str, str] = ...,
        TagRestrictedResources: Sequence[str] = ...
    ) -> CreateSecurityProfileResponseTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.create_security_profile)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#create_security_profile)
        """

    def create_task_template(
        self,
        *,
        InstanceId: str,
        Name: str,
        Fields: Sequence[TaskTemplateFieldTypeDef],
        Description: str = ...,
        ContactFlowId: str = ...,
        Constraints: TaskTemplateConstraintsTypeDef = ...,
        Defaults: TaskTemplateDefaultsTypeDef = ...,
        Status: TaskTemplateStatusType = ...,
        ClientToken: str = ...
    ) -> CreateTaskTemplateResponseTypeDef:
        """
        Creates a new task template in the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.create_task_template)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#create_task_template)
        """

    def create_traffic_distribution_group(
        self,
        *,
        Name: str,
        InstanceId: str,
        Description: str = ...,
        ClientToken: str = ...,
        Tags: Mapping[str, str] = ...
    ) -> CreateTrafficDistributionGroupResponseTypeDef:
        """
        Creates a traffic distribution group given an Amazon Connect instance that has
        been replicated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.create_traffic_distribution_group)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#create_traffic_distribution_group)
        """

    def create_use_case(
        self,
        *,
        InstanceId: str,
        IntegrationAssociationId: str,
        UseCaseType: UseCaseTypeType,
        Tags: Mapping[str, str] = ...
    ) -> CreateUseCaseResponseTypeDef:
        """
        Creates a use case for an integration association.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.create_use_case)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#create_use_case)
        """

    def create_user(
        self,
        *,
        Username: str,
        PhoneConfig: UserPhoneConfigTypeDef,
        SecurityProfileIds: Sequence[str],
        RoutingProfileId: str,
        InstanceId: str,
        Password: str = ...,
        IdentityInfo: UserIdentityInfoTypeDef = ...,
        DirectoryUserId: str = ...,
        HierarchyGroupId: str = ...,
        Tags: Mapping[str, str] = ...
    ) -> CreateUserResponseTypeDef:
        """
        Creates a user account for the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.create_user)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#create_user)
        """

    def create_user_hierarchy_group(
        self, *, Name: str, InstanceId: str, ParentGroupId: str = ..., Tags: Mapping[str, str] = ...
    ) -> CreateUserHierarchyGroupResponseTypeDef:
        """
        Creates a new user hierarchy group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.create_user_hierarchy_group)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#create_user_hierarchy_group)
        """

    def create_vocabulary(
        self,
        *,
        InstanceId: str,
        VocabularyName: str,
        LanguageCode: VocabularyLanguageCodeType,
        Content: str,
        ClientToken: str = ...,
        Tags: Mapping[str, str] = ...
    ) -> CreateVocabularyResponseTypeDef:
        """
        Creates a custom vocabulary associated with your Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.create_vocabulary)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#create_vocabulary)
        """

    def deactivate_evaluation_form(
        self, *, InstanceId: str, EvaluationFormId: str, EvaluationFormVersion: int
    ) -> DeactivateEvaluationFormResponseTypeDef:
        """
        Deactivates an evaluation form in the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.deactivate_evaluation_form)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#deactivate_evaluation_form)
        """

    def delete_contact_evaluation(
        self, *, InstanceId: str, EvaluationId: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a contact evaluation in the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.delete_contact_evaluation)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#delete_contact_evaluation)
        """

    def delete_contact_flow(self, *, InstanceId: str, ContactFlowId: str) -> Dict[str, Any]:
        """
        Deletes a flow for the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.delete_contact_flow)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#delete_contact_flow)
        """

    def delete_contact_flow_module(
        self, *, InstanceId: str, ContactFlowModuleId: str
    ) -> Dict[str, Any]:
        """
        Deletes the specified flow module.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.delete_contact_flow_module)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#delete_contact_flow_module)
        """

    def delete_evaluation_form(
        self, *, InstanceId: str, EvaluationFormId: str, EvaluationFormVersion: int = ...
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes an evaluation form in the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.delete_evaluation_form)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#delete_evaluation_form)
        """

    def delete_hours_of_operation(
        self, *, InstanceId: str, HoursOfOperationId: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.delete_hours_of_operation)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#delete_hours_of_operation)
        """

    def delete_instance(self, *, InstanceId: str) -> EmptyResponseMetadataTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.delete_instance)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#delete_instance)
        """

    def delete_integration_association(
        self, *, InstanceId: str, IntegrationAssociationId: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes an Amazon Web Services resource association from an Amazon Connect
        instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.delete_integration_association)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#delete_integration_association)
        """

    def delete_prompt(self, *, InstanceId: str, PromptId: str) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a prompt.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.delete_prompt)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#delete_prompt)
        """

    def delete_queue(self, *, InstanceId: str, QueueId: str) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a queue.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.delete_queue)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#delete_queue)
        """

    def delete_quick_connect(
        self, *, InstanceId: str, QuickConnectId: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a quick connect.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.delete_quick_connect)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#delete_quick_connect)
        """

    def delete_routing_profile(
        self, *, InstanceId: str, RoutingProfileId: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a routing profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.delete_routing_profile)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#delete_routing_profile)
        """

    def delete_rule(self, *, InstanceId: str, RuleId: str) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a rule for the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.delete_rule)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#delete_rule)
        """

    def delete_security_profile(
        self, *, InstanceId: str, SecurityProfileId: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.delete_security_profile)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#delete_security_profile)
        """

    def delete_task_template(self, *, InstanceId: str, TaskTemplateId: str) -> Dict[str, Any]:
        """
        Deletes the task template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.delete_task_template)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#delete_task_template)
        """

    def delete_traffic_distribution_group(
        self, *, TrafficDistributionGroupId: str
    ) -> Dict[str, Any]:
        """
        Deletes a traffic distribution group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.delete_traffic_distribution_group)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#delete_traffic_distribution_group)
        """

    def delete_use_case(
        self, *, InstanceId: str, IntegrationAssociationId: str, UseCaseId: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a use case from an integration association.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.delete_use_case)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#delete_use_case)
        """

    def delete_user(self, *, InstanceId: str, UserId: str) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a user account from the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.delete_user)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#delete_user)
        """

    def delete_user_hierarchy_group(
        self, *, HierarchyGroupId: str, InstanceId: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes an existing user hierarchy group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.delete_user_hierarchy_group)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#delete_user_hierarchy_group)
        """

    def delete_vocabulary(
        self, *, InstanceId: str, VocabularyId: str
    ) -> DeleteVocabularyResponseTypeDef:
        """
        Deletes the vocabulary that has the given identifier.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.delete_vocabulary)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#delete_vocabulary)
        """

    def describe_agent_status(
        self, *, InstanceId: str, AgentStatusId: str
    ) -> DescribeAgentStatusResponseTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.describe_agent_status)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#describe_agent_status)
        """

    def describe_contact(
        self, *, InstanceId: str, ContactId: str
    ) -> DescribeContactResponseTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.describe_contact)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#describe_contact)
        """

    def describe_contact_evaluation(
        self, *, InstanceId: str, EvaluationId: str
    ) -> DescribeContactEvaluationResponseTypeDef:
        """
        Describes a contact evaluation in the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.describe_contact_evaluation)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#describe_contact_evaluation)
        """

    def describe_contact_flow(
        self, *, InstanceId: str, ContactFlowId: str
    ) -> DescribeContactFlowResponseTypeDef:
        """
        Describes the specified flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.describe_contact_flow)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#describe_contact_flow)
        """

    def describe_contact_flow_module(
        self, *, InstanceId: str, ContactFlowModuleId: str
    ) -> DescribeContactFlowModuleResponseTypeDef:
        """
        Describes the specified flow module.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.describe_contact_flow_module)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#describe_contact_flow_module)
        """

    def describe_evaluation_form(
        self, *, InstanceId: str, EvaluationFormId: str, EvaluationFormVersion: int = ...
    ) -> DescribeEvaluationFormResponseTypeDef:
        """
        Describes an evaluation form in the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.describe_evaluation_form)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#describe_evaluation_form)
        """

    def describe_hours_of_operation(
        self, *, InstanceId: str, HoursOfOperationId: str
    ) -> DescribeHoursOfOperationResponseTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.describe_hours_of_operation)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#describe_hours_of_operation)
        """

    def describe_instance(self, *, InstanceId: str) -> DescribeInstanceResponseTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.describe_instance)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#describe_instance)
        """

    def describe_instance_attribute(
        self, *, InstanceId: str, AttributeType: InstanceAttributeTypeType
    ) -> DescribeInstanceAttributeResponseTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.describe_instance_attribute)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#describe_instance_attribute)
        """

    def describe_instance_storage_config(
        self, *, InstanceId: str, AssociationId: str, ResourceType: InstanceStorageResourceTypeType
    ) -> DescribeInstanceStorageConfigResponseTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.describe_instance_storage_config)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#describe_instance_storage_config)
        """

    def describe_phone_number(self, *, PhoneNumberId: str) -> DescribePhoneNumberResponseTypeDef:
        """
        Gets details and status of a phone number that’s claimed to your Amazon Connect
        instance or traffic distribution group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.describe_phone_number)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#describe_phone_number)
        """

    def describe_prompt(self, *, InstanceId: str, PromptId: str) -> DescribePromptResponseTypeDef:
        """
        Describes the prompt.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.describe_prompt)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#describe_prompt)
        """

    def describe_queue(self, *, InstanceId: str, QueueId: str) -> DescribeQueueResponseTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.describe_queue)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#describe_queue)
        """

    def describe_quick_connect(
        self, *, InstanceId: str, QuickConnectId: str
    ) -> DescribeQuickConnectResponseTypeDef:
        """
        Describes the quick connect.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.describe_quick_connect)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#describe_quick_connect)
        """

    def describe_routing_profile(
        self, *, InstanceId: str, RoutingProfileId: str
    ) -> DescribeRoutingProfileResponseTypeDef:
        """
        Describes the specified routing profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.describe_routing_profile)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#describe_routing_profile)
        """

    def describe_rule(self, *, InstanceId: str, RuleId: str) -> DescribeRuleResponseTypeDef:
        """
        Describes a rule for the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.describe_rule)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#describe_rule)
        """

    def describe_security_profile(
        self, *, SecurityProfileId: str, InstanceId: str
    ) -> DescribeSecurityProfileResponseTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.describe_security_profile)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#describe_security_profile)
        """

    def describe_traffic_distribution_group(
        self, *, TrafficDistributionGroupId: str
    ) -> DescribeTrafficDistributionGroupResponseTypeDef:
        """
        Gets details and status of a traffic distribution group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.describe_traffic_distribution_group)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#describe_traffic_distribution_group)
        """

    def describe_user(self, *, UserId: str, InstanceId: str) -> DescribeUserResponseTypeDef:
        """
        Describes the specified user account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.describe_user)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#describe_user)
        """

    def describe_user_hierarchy_group(
        self, *, HierarchyGroupId: str, InstanceId: str
    ) -> DescribeUserHierarchyGroupResponseTypeDef:
        """
        Describes the specified hierarchy group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.describe_user_hierarchy_group)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#describe_user_hierarchy_group)
        """

    def describe_user_hierarchy_structure(
        self, *, InstanceId: str
    ) -> DescribeUserHierarchyStructureResponseTypeDef:
        """
        Describes the hierarchy structure of the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.describe_user_hierarchy_structure)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#describe_user_hierarchy_structure)
        """

    def describe_vocabulary(
        self, *, InstanceId: str, VocabularyId: str
    ) -> DescribeVocabularyResponseTypeDef:
        """
        Describes the specified vocabulary.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.describe_vocabulary)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#describe_vocabulary)
        """

    def disassociate_approved_origin(
        self, *, InstanceId: str, Origin: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.disassociate_approved_origin)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#disassociate_approved_origin)
        """

    def disassociate_bot(
        self, *, InstanceId: str, LexBot: LexBotTypeDef = ..., LexV2Bot: LexV2BotTypeDef = ...
    ) -> EmptyResponseMetadataTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.disassociate_bot)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#disassociate_bot)
        """

    def disassociate_instance_storage_config(
        self, *, InstanceId: str, AssociationId: str, ResourceType: InstanceStorageResourceTypeType
    ) -> EmptyResponseMetadataTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.disassociate_instance_storage_config)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#disassociate_instance_storage_config)
        """

    def disassociate_lambda_function(
        self, *, InstanceId: str, FunctionArn: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.disassociate_lambda_function)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#disassociate_lambda_function)
        """

    def disassociate_lex_bot(
        self, *, InstanceId: str, BotName: str, LexRegion: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.disassociate_lex_bot)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#disassociate_lex_bot)
        """

    def disassociate_phone_number_contact_flow(
        self, *, PhoneNumberId: str, InstanceId: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Removes the flow association from a phone number claimed to your Amazon Connect
        instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.disassociate_phone_number_contact_flow)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#disassociate_phone_number_contact_flow)
        """

    def disassociate_queue_quick_connects(
        self, *, InstanceId: str, QueueId: str, QuickConnectIds: Sequence[str]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.disassociate_queue_quick_connects)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#disassociate_queue_quick_connects)
        """

    def disassociate_routing_profile_queues(
        self,
        *,
        InstanceId: str,
        RoutingProfileId: str,
        QueueReferences: Sequence[RoutingProfileQueueReferenceTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Disassociates a set of queues from a routing profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.disassociate_routing_profile_queues)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#disassociate_routing_profile_queues)
        """

    def disassociate_security_key(
        self, *, InstanceId: str, AssociationId: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.disassociate_security_key)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#disassociate_security_key)
        """

    def disassociate_traffic_distribution_group_user(
        self, *, TrafficDistributionGroupId: str, UserId: str, InstanceId: str
    ) -> Dict[str, Any]:
        """
        Disassociates an agent from a traffic distribution group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.disassociate_traffic_distribution_group_user)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#disassociate_traffic_distribution_group_user)
        """

    def dismiss_user_contact(
        self, *, UserId: str, InstanceId: str, ContactId: str
    ) -> Dict[str, Any]:
        """
        Dismisses contacts from an agent’s CCP and returns the agent to an available
        state, which allows the agent to receive a new routed contact.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.dismiss_user_contact)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#dismiss_user_contact)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#generate_presigned_url)
        """

    def get_contact_attributes(
        self, *, InstanceId: str, InitialContactId: str
    ) -> GetContactAttributesResponseTypeDef:
        """
        Retrieves the contact attributes for the specified contact.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.get_contact_attributes)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#get_contact_attributes)
        """

    def get_current_metric_data(
        self,
        *,
        InstanceId: str,
        Filters: FiltersTypeDef,
        CurrentMetrics: Sequence[CurrentMetricTypeDef],
        Groupings: Sequence[GroupingType] = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
        SortCriteria: Sequence[CurrentMetricSortCriteriaTypeDef] = ...
    ) -> GetCurrentMetricDataResponseTypeDef:
        """
        Gets the real-time metric data from the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.get_current_metric_data)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#get_current_metric_data)
        """

    def get_current_user_data(
        self,
        *,
        InstanceId: str,
        Filters: UserDataFiltersTypeDef,
        NextToken: str = ...,
        MaxResults: int = ...
    ) -> GetCurrentUserDataResponseTypeDef:
        """
        Gets the real-time active user data from the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.get_current_user_data)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#get_current_user_data)
        """

    def get_federation_token(self, *, InstanceId: str) -> GetFederationTokenResponseTypeDef:
        """
        Retrieves a token for federation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.get_federation_token)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#get_federation_token)
        """

    def get_metric_data(
        self,
        *,
        InstanceId: str,
        StartTime: TimestampTypeDef,
        EndTime: TimestampTypeDef,
        Filters: FiltersTypeDef,
        HistoricalMetrics: Sequence[HistoricalMetricTypeDef],
        Groupings: Sequence[GroupingType] = ...,
        NextToken: str = ...,
        MaxResults: int = ...
    ) -> GetMetricDataResponseTypeDef:
        """
        Gets historical metric data from the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.get_metric_data)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#get_metric_data)
        """

    def get_metric_data_v2(
        self,
        *,
        ResourceArn: str,
        StartTime: TimestampTypeDef,
        EndTime: TimestampTypeDef,
        Filters: Sequence[FilterV2TypeDef],
        Metrics: Sequence[MetricV2TypeDef],
        Groupings: Sequence[str] = ...,
        NextToken: str = ...,
        MaxResults: int = ...
    ) -> GetMetricDataV2ResponseTypeDef:
        """
        Gets metric data from the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.get_metric_data_v2)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#get_metric_data_v2)
        """

    def get_prompt_file(self, *, InstanceId: str, PromptId: str) -> GetPromptFileResponseTypeDef:
        """
        Gets the prompt file.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.get_prompt_file)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#get_prompt_file)
        """

    def get_task_template(
        self, *, InstanceId: str, TaskTemplateId: str, SnapshotVersion: str = ...
    ) -> GetTaskTemplateResponseTypeDef:
        """
        Gets details about a specific task template in the specified Amazon Connect
        instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.get_task_template)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#get_task_template)
        """

    def get_traffic_distribution(self, *, Id: str) -> GetTrafficDistributionResponseTypeDef:
        """
        Retrieves the current traffic distribution for a given traffic distribution
        group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.get_traffic_distribution)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#get_traffic_distribution)
        """

    def list_agent_statuses(
        self,
        *,
        InstanceId: str,
        NextToken: str = ...,
        MaxResults: int = ...,
        AgentStatusTypes: Sequence[AgentStatusTypeType] = ...
    ) -> ListAgentStatusResponseTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.list_agent_statuses)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#list_agent_statuses)
        """

    def list_approved_origins(
        self, *, InstanceId: str, NextToken: str = ..., MaxResults: int = ...
    ) -> ListApprovedOriginsResponseTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.list_approved_origins)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#list_approved_origins)
        """

    def list_bots(
        self,
        *,
        InstanceId: str,
        LexVersion: LexVersionType,
        NextToken: str = ...,
        MaxResults: int = ...
    ) -> ListBotsResponseTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.list_bots)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#list_bots)
        """

    def list_contact_evaluations(
        self, *, InstanceId: str, ContactId: str, NextToken: str = ...
    ) -> ListContactEvaluationsResponseTypeDef:
        """
        Lists contact evaluations in the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.list_contact_evaluations)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#list_contact_evaluations)
        """

    def list_contact_flow_modules(
        self,
        *,
        InstanceId: str,
        NextToken: str = ...,
        MaxResults: int = ...,
        ContactFlowModuleState: ContactFlowModuleStateType = ...
    ) -> ListContactFlowModulesResponseTypeDef:
        """
        Provides information about the flow modules for the specified Amazon Connect
        instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.list_contact_flow_modules)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#list_contact_flow_modules)
        """

    def list_contact_flows(
        self,
        *,
        InstanceId: str,
        ContactFlowTypes: Sequence[ContactFlowTypeType] = ...,
        NextToken: str = ...,
        MaxResults: int = ...
    ) -> ListContactFlowsResponseTypeDef:
        """
        Provides information about the flows for the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.list_contact_flows)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#list_contact_flows)
        """

    def list_contact_references(
        self,
        *,
        InstanceId: str,
        ContactId: str,
        ReferenceTypes: Sequence[ReferenceTypeType],
        NextToken: str = ...
    ) -> ListContactReferencesResponseTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.list_contact_references)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#list_contact_references)
        """

    def list_default_vocabularies(
        self,
        *,
        InstanceId: str,
        LanguageCode: VocabularyLanguageCodeType = ...,
        MaxResults: int = ...,
        NextToken: str = ...
    ) -> ListDefaultVocabulariesResponseTypeDef:
        """
        Lists the default vocabularies for the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.list_default_vocabularies)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#list_default_vocabularies)
        """

    def list_evaluation_form_versions(
        self, *, InstanceId: str, EvaluationFormId: str, MaxResults: int = ..., NextToken: str = ...
    ) -> ListEvaluationFormVersionsResponseTypeDef:
        """
        Lists versions of an evaluation form in the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.list_evaluation_form_versions)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#list_evaluation_form_versions)
        """

    def list_evaluation_forms(
        self, *, InstanceId: str, MaxResults: int = ..., NextToken: str = ...
    ) -> ListEvaluationFormsResponseTypeDef:
        """
        Lists evaluation forms in the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.list_evaluation_forms)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#list_evaluation_forms)
        """

    def list_hours_of_operations(
        self, *, InstanceId: str, NextToken: str = ..., MaxResults: int = ...
    ) -> ListHoursOfOperationsResponseTypeDef:
        """
        Provides information about the hours of operation for the specified Amazon
        Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.list_hours_of_operations)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#list_hours_of_operations)
        """

    def list_instance_attributes(
        self, *, InstanceId: str, NextToken: str = ..., MaxResults: int = ...
    ) -> ListInstanceAttributesResponseTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.list_instance_attributes)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#list_instance_attributes)
        """

    def list_instance_storage_configs(
        self,
        *,
        InstanceId: str,
        ResourceType: InstanceStorageResourceTypeType,
        NextToken: str = ...,
        MaxResults: int = ...
    ) -> ListInstanceStorageConfigsResponseTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.list_instance_storage_configs)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#list_instance_storage_configs)
        """

    def list_instances(
        self, *, NextToken: str = ..., MaxResults: int = ...
    ) -> ListInstancesResponseTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.list_instances)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#list_instances)
        """

    def list_integration_associations(
        self,
        *,
        InstanceId: str,
        IntegrationType: IntegrationTypeType = ...,
        NextToken: str = ...,
        MaxResults: int = ...
    ) -> ListIntegrationAssociationsResponseTypeDef:
        """
        Provides summary information about the Amazon Web Services resource associations
        for the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.list_integration_associations)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#list_integration_associations)
        """

    def list_lambda_functions(
        self, *, InstanceId: str, NextToken: str = ..., MaxResults: int = ...
    ) -> ListLambdaFunctionsResponseTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.list_lambda_functions)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#list_lambda_functions)
        """

    def list_lex_bots(
        self, *, InstanceId: str, NextToken: str = ..., MaxResults: int = ...
    ) -> ListLexBotsResponseTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.list_lex_bots)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#list_lex_bots)
        """

    def list_phone_numbers(
        self,
        *,
        InstanceId: str,
        PhoneNumberTypes: Sequence[PhoneNumberTypeType] = ...,
        PhoneNumberCountryCodes: Sequence[PhoneNumberCountryCodeType] = ...,
        NextToken: str = ...,
        MaxResults: int = ...
    ) -> ListPhoneNumbersResponseTypeDef:
        """
        Provides information about the phone numbers for the specified Amazon Connect
        instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.list_phone_numbers)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#list_phone_numbers)
        """

    def list_phone_numbers_v2(
        self,
        *,
        TargetArn: str = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
        PhoneNumberCountryCodes: Sequence[PhoneNumberCountryCodeType] = ...,
        PhoneNumberTypes: Sequence[PhoneNumberTypeType] = ...,
        PhoneNumberPrefix: str = ...
    ) -> ListPhoneNumbersV2ResponseTypeDef:
        """
        Lists phone numbers claimed to your Amazon Connect instance or traffic
        distribution group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.list_phone_numbers_v2)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#list_phone_numbers_v2)
        """

    def list_prompts(
        self, *, InstanceId: str, NextToken: str = ..., MaxResults: int = ...
    ) -> ListPromptsResponseTypeDef:
        """
        Provides information about the prompts for the specified Amazon Connect
        instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.list_prompts)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#list_prompts)
        """

    def list_queue_quick_connects(
        self, *, InstanceId: str, QueueId: str, NextToken: str = ..., MaxResults: int = ...
    ) -> ListQueueQuickConnectsResponseTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.list_queue_quick_connects)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#list_queue_quick_connects)
        """

    def list_queues(
        self,
        *,
        InstanceId: str,
        QueueTypes: Sequence[QueueTypeType] = ...,
        NextToken: str = ...,
        MaxResults: int = ...
    ) -> ListQueuesResponseTypeDef:
        """
        Provides information about the queues for the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.list_queues)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#list_queues)
        """

    def list_quick_connects(
        self,
        *,
        InstanceId: str,
        NextToken: str = ...,
        MaxResults: int = ...,
        QuickConnectTypes: Sequence[QuickConnectTypeType] = ...
    ) -> ListQuickConnectsResponseTypeDef:
        """
        Provides information about the quick connects for the specified Amazon Connect
        instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.list_quick_connects)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#list_quick_connects)
        """

    def list_routing_profile_queues(
        self, *, InstanceId: str, RoutingProfileId: str, NextToken: str = ..., MaxResults: int = ...
    ) -> ListRoutingProfileQueuesResponseTypeDef:
        """
        Lists the queues associated with a routing profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.list_routing_profile_queues)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#list_routing_profile_queues)
        """

    def list_routing_profiles(
        self, *, InstanceId: str, NextToken: str = ..., MaxResults: int = ...
    ) -> ListRoutingProfilesResponseTypeDef:
        """
        Provides summary information about the routing profiles for the specified Amazon
        Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.list_routing_profiles)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#list_routing_profiles)
        """

    def list_rules(
        self,
        *,
        InstanceId: str,
        PublishStatus: RulePublishStatusType = ...,
        EventSourceName: EventSourceNameType = ...,
        MaxResults: int = ...,
        NextToken: str = ...
    ) -> ListRulesResponseTypeDef:
        """
        List all rules for the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.list_rules)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#list_rules)
        """

    def list_security_keys(
        self, *, InstanceId: str, NextToken: str = ..., MaxResults: int = ...
    ) -> ListSecurityKeysResponseTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.list_security_keys)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#list_security_keys)
        """

    def list_security_profile_permissions(
        self,
        *,
        SecurityProfileId: str,
        InstanceId: str,
        NextToken: str = ...,
        MaxResults: int = ...
    ) -> ListSecurityProfilePermissionsResponseTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.list_security_profile_permissions)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#list_security_profile_permissions)
        """

    def list_security_profiles(
        self, *, InstanceId: str, NextToken: str = ..., MaxResults: int = ...
    ) -> ListSecurityProfilesResponseTypeDef:
        """
        Provides summary information about the security profiles for the specified
        Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.list_security_profiles)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#list_security_profiles)
        """

    def list_tags_for_resource(self, *, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        Lists the tags for the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#list_tags_for_resource)
        """

    def list_task_templates(
        self,
        *,
        InstanceId: str,
        NextToken: str = ...,
        MaxResults: int = ...,
        Status: TaskTemplateStatusType = ...,
        Name: str = ...
    ) -> ListTaskTemplatesResponseTypeDef:
        """
        Lists task templates for the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.list_task_templates)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#list_task_templates)
        """

    def list_traffic_distribution_group_users(
        self, *, TrafficDistributionGroupId: str, MaxResults: int = ..., NextToken: str = ...
    ) -> ListTrafficDistributionGroupUsersResponseTypeDef:
        """
        Lists traffic distribution group users.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.list_traffic_distribution_group_users)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#list_traffic_distribution_group_users)
        """

    def list_traffic_distribution_groups(
        self, *, MaxResults: int = ..., NextToken: str = ..., InstanceId: str = ...
    ) -> ListTrafficDistributionGroupsResponseTypeDef:
        """
        Lists traffic distribution groups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.list_traffic_distribution_groups)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#list_traffic_distribution_groups)
        """

    def list_use_cases(
        self,
        *,
        InstanceId: str,
        IntegrationAssociationId: str,
        NextToken: str = ...,
        MaxResults: int = ...
    ) -> ListUseCasesResponseTypeDef:
        """
        Lists the use cases for the integration association.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.list_use_cases)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#list_use_cases)
        """

    def list_user_hierarchy_groups(
        self, *, InstanceId: str, NextToken: str = ..., MaxResults: int = ...
    ) -> ListUserHierarchyGroupsResponseTypeDef:
        """
        Provides summary information about the hierarchy groups for the specified Amazon
        Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.list_user_hierarchy_groups)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#list_user_hierarchy_groups)
        """

    def list_users(
        self, *, InstanceId: str, NextToken: str = ..., MaxResults: int = ...
    ) -> ListUsersResponseTypeDef:
        """
        Provides summary information about the users for the specified Amazon Connect
        instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.list_users)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#list_users)
        """

    def monitor_contact(
        self,
        *,
        InstanceId: str,
        ContactId: str,
        UserId: str,
        AllowedMonitorCapabilities: Sequence[MonitorCapabilityType] = ...,
        ClientToken: str = ...
    ) -> MonitorContactResponseTypeDef:
        """
        Initiates silent monitoring of a contact.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.monitor_contact)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#monitor_contact)
        """

    def put_user_status(
        self, *, UserId: str, InstanceId: str, AgentStatusId: str
    ) -> Dict[str, Any]:
        """
        Changes the current status of a user or agent in Amazon Connect.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.put_user_status)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#put_user_status)
        """

    def release_phone_number(
        self, *, PhoneNumberId: str, ClientToken: str = ...
    ) -> EmptyResponseMetadataTypeDef:
        """
        Releases a phone number previously claimed to an Amazon Connect instance or
        traffic distribution group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.release_phone_number)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#release_phone_number)
        """

    def replicate_instance(
        self, *, InstanceId: str, ReplicaRegion: str, ReplicaAlias: str, ClientToken: str = ...
    ) -> ReplicateInstanceResponseTypeDef:
        """
        Replicates an Amazon Connect instance in the specified Amazon Web Services
        Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.replicate_instance)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#replicate_instance)
        """

    def resume_contact_recording(
        self, *, InstanceId: str, ContactId: str, InitialContactId: str
    ) -> Dict[str, Any]:
        """
        When a contact is being recorded, and the recording has been suspended using
        SuspendContactRecording, this API resumes recording the call or screen.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.resume_contact_recording)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#resume_contact_recording)
        """

    def search_available_phone_numbers(
        self,
        *,
        TargetArn: str,
        PhoneNumberCountryCode: PhoneNumberCountryCodeType,
        PhoneNumberType: PhoneNumberTypeType,
        PhoneNumberPrefix: str = ...,
        MaxResults: int = ...,
        NextToken: str = ...
    ) -> SearchAvailablePhoneNumbersResponseTypeDef:
        """
        Searches for available phone numbers that you can claim to your Amazon Connect
        instance or traffic distribution group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.search_available_phone_numbers)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#search_available_phone_numbers)
        """

    def search_hours_of_operations(
        self,
        *,
        InstanceId: str,
        NextToken: str = ...,
        MaxResults: int = ...,
        SearchFilter: HoursOfOperationSearchFilterTypeDef = ...,
        SearchCriteria: "HoursOfOperationSearchCriteriaTypeDef" = ...
    ) -> SearchHoursOfOperationsResponseTypeDef:
        """
        Searches the hours of operation in an Amazon Connect instance, with optional
        filtering.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.search_hours_of_operations)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#search_hours_of_operations)
        """

    def search_prompts(
        self,
        *,
        InstanceId: str,
        NextToken: str = ...,
        MaxResults: int = ...,
        SearchFilter: PromptSearchFilterTypeDef = ...,
        SearchCriteria: "PromptSearchCriteriaTypeDef" = ...
    ) -> SearchPromptsResponseTypeDef:
        """
        Searches prompts in an Amazon Connect instance, with optional filtering.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.search_prompts)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#search_prompts)
        """

    def search_queues(
        self,
        *,
        InstanceId: str,
        NextToken: str = ...,
        MaxResults: int = ...,
        SearchFilter: QueueSearchFilterTypeDef = ...,
        SearchCriteria: "QueueSearchCriteriaTypeDef" = ...
    ) -> SearchQueuesResponseTypeDef:
        """
        Searches queues in an Amazon Connect instance, with optional filtering.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.search_queues)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#search_queues)
        """

    def search_quick_connects(
        self,
        *,
        InstanceId: str,
        NextToken: str = ...,
        MaxResults: int = ...,
        SearchFilter: QuickConnectSearchFilterTypeDef = ...,
        SearchCriteria: "QuickConnectSearchCriteriaTypeDef" = ...
    ) -> SearchQuickConnectsResponseTypeDef:
        """
        Searches quick connects in an Amazon Connect instance, with optional filtering.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.search_quick_connects)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#search_quick_connects)
        """

    def search_resource_tags(
        self,
        *,
        InstanceId: str,
        ResourceTypes: Sequence[str] = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
        SearchCriteria: ResourceTagsSearchCriteriaTypeDef = ...
    ) -> SearchResourceTagsResponseTypeDef:
        """
        Searches tags used in an Amazon Connect instance using optional search criteria.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.search_resource_tags)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#search_resource_tags)
        """

    def search_routing_profiles(
        self,
        *,
        InstanceId: str,
        NextToken: str = ...,
        MaxResults: int = ...,
        SearchFilter: RoutingProfileSearchFilterTypeDef = ...,
        SearchCriteria: "RoutingProfileSearchCriteriaTypeDef" = ...
    ) -> SearchRoutingProfilesResponseTypeDef:
        """
        Searches routing profiles in an Amazon Connect instance, with optional
        filtering.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.search_routing_profiles)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#search_routing_profiles)
        """

    def search_security_profiles(
        self,
        *,
        InstanceId: str,
        NextToken: str = ...,
        MaxResults: int = ...,
        SearchCriteria: "SecurityProfileSearchCriteriaTypeDef" = ...,
        SearchFilter: SecurityProfilesSearchFilterTypeDef = ...
    ) -> SearchSecurityProfilesResponseTypeDef:
        """
        Searches security profiles in an Amazon Connect instance, with optional
        filtering.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.search_security_profiles)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#search_security_profiles)
        """

    def search_users(
        self,
        *,
        InstanceId: str = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
        SearchFilter: UserSearchFilterTypeDef = ...,
        SearchCriteria: "UserSearchCriteriaTypeDef" = ...
    ) -> SearchUsersResponseTypeDef:
        """
        Searches users in an Amazon Connect instance, with optional filtering.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.search_users)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#search_users)
        """

    def search_vocabularies(
        self,
        *,
        InstanceId: str,
        MaxResults: int = ...,
        NextToken: str = ...,
        State: VocabularyStateType = ...,
        NameStartsWith: str = ...,
        LanguageCode: VocabularyLanguageCodeType = ...
    ) -> SearchVocabulariesResponseTypeDef:
        """
        Searches for vocabularies within a specific Amazon Connect instance using
        `State`, `NameStartsWith`, and `LanguageCode`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.search_vocabularies)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#search_vocabularies)
        """

    def start_chat_contact(
        self,
        *,
        InstanceId: str,
        ContactFlowId: str,
        ParticipantDetails: ParticipantDetailsTypeDef,
        Attributes: Mapping[str, str] = ...,
        InitialMessage: ChatMessageTypeDef = ...,
        ClientToken: str = ...,
        ChatDurationInMinutes: int = ...,
        SupportedMessagingContentTypes: Sequence[str] = ...,
        PersistentChat: PersistentChatTypeDef = ...,
        RelatedContactId: str = ...
    ) -> StartChatContactResponseTypeDef:
        """
        Initiates a flow to start a new chat for the customer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.start_chat_contact)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#start_chat_contact)
        """

    def start_contact_evaluation(
        self, *, InstanceId: str, ContactId: str, EvaluationFormId: str, ClientToken: str = ...
    ) -> StartContactEvaluationResponseTypeDef:
        """
        Starts an empty evaluation in the specified Amazon Connect instance, using the
        given evaluation form for the particular contact.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.start_contact_evaluation)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#start_contact_evaluation)
        """

    def start_contact_recording(
        self,
        *,
        InstanceId: str,
        ContactId: str,
        InitialContactId: str,
        VoiceRecordingConfiguration: VoiceRecordingConfigurationTypeDef
    ) -> Dict[str, Any]:
        """
        Starts recording the contact: * If the API is called *before* the agent joins
        the call, recording starts when the agent joins the call.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.start_contact_recording)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#start_contact_recording)
        """

    def start_contact_streaming(
        self,
        *,
        InstanceId: str,
        ContactId: str,
        ChatStreamingConfiguration: ChatStreamingConfigurationTypeDef,
        ClientToken: str
    ) -> StartContactStreamingResponseTypeDef:
        """
        Initiates real-time message streaming for a new chat contact.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.start_contact_streaming)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#start_contact_streaming)
        """

    def start_outbound_voice_contact(
        self,
        *,
        DestinationPhoneNumber: str,
        ContactFlowId: str,
        InstanceId: str,
        ClientToken: str = ...,
        SourcePhoneNumber: str = ...,
        QueueId: str = ...,
        Attributes: Mapping[str, str] = ...,
        AnswerMachineDetectionConfig: AnswerMachineDetectionConfigTypeDef = ...,
        CampaignId: str = ...,
        TrafficType: TrafficTypeType = ...
    ) -> StartOutboundVoiceContactResponseTypeDef:
        """
        Places an outbound call to a contact, and then initiates the flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.start_outbound_voice_contact)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#start_outbound_voice_contact)
        """

    def start_task_contact(
        self,
        *,
        InstanceId: str,
        Name: str,
        PreviousContactId: str = ...,
        ContactFlowId: str = ...,
        Attributes: Mapping[str, str] = ...,
        References: Mapping[str, ReferenceTypeDef] = ...,
        Description: str = ...,
        ClientToken: str = ...,
        ScheduledTime: TimestampTypeDef = ...,
        TaskTemplateId: str = ...,
        QuickConnectId: str = ...,
        RelatedContactId: str = ...
    ) -> StartTaskContactResponseTypeDef:
        """
        Initiates a flow to start a new task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.start_task_contact)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#start_task_contact)
        """

    def stop_contact(self, *, ContactId: str, InstanceId: str) -> Dict[str, Any]:
        """
        Ends the specified contact.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.stop_contact)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#stop_contact)
        """

    def stop_contact_recording(
        self, *, InstanceId: str, ContactId: str, InitialContactId: str
    ) -> Dict[str, Any]:
        """
        Stops recording a call when a contact is being recorded.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.stop_contact_recording)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#stop_contact_recording)
        """

    def stop_contact_streaming(
        self, *, InstanceId: str, ContactId: str, StreamingId: str
    ) -> Dict[str, Any]:
        """
        Ends message streaming on a specified contact.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.stop_contact_streaming)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#stop_contact_streaming)
        """

    def submit_contact_evaluation(
        self,
        *,
        InstanceId: str,
        EvaluationId: str,
        Answers: Mapping[str, EvaluationAnswerInputTypeDef] = ...,
        Notes: Mapping[str, EvaluationNoteTypeDef] = ...
    ) -> SubmitContactEvaluationResponseTypeDef:
        """
        Submits a contact evaluation in the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.submit_contact_evaluation)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#submit_contact_evaluation)
        """

    def suspend_contact_recording(
        self, *, InstanceId: str, ContactId: str, InitialContactId: str
    ) -> Dict[str, Any]:
        """
        When a contact is being recorded, this API suspends recording the call or
        screen.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.suspend_contact_recording)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#suspend_contact_recording)
        """

    def tag_resource(
        self, *, resourceArn: str, tags: Mapping[str, str]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Adds the specified tags to the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.tag_resource)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#tag_resource)
        """

    def transfer_contact(
        self,
        *,
        InstanceId: str,
        ContactId: str,
        ContactFlowId: str,
        QueueId: str = ...,
        UserId: str = ...,
        ClientToken: str = ...
    ) -> TransferContactResponseTypeDef:
        """
        Transfers contacts from one agent or queue to another agent or queue at any
        point after a contact is created.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.transfer_contact)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#transfer_contact)
        """

    def untag_resource(
        self, *, resourceArn: str, tagKeys: Sequence[str]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Removes the specified tags from the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.untag_resource)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#untag_resource)
        """

    def update_agent_status(
        self,
        *,
        InstanceId: str,
        AgentStatusId: str,
        Name: str = ...,
        Description: str = ...,
        State: AgentStatusStateType = ...,
        DisplayOrder: int = ...,
        ResetOrderNumber: bool = ...
    ) -> EmptyResponseMetadataTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.update_agent_status)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#update_agent_status)
        """

    def update_contact(
        self,
        *,
        InstanceId: str,
        ContactId: str,
        Name: str = ...,
        Description: str = ...,
        References: Mapping[str, ReferenceTypeDef] = ...
    ) -> Dict[str, Any]:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.update_contact)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#update_contact)
        """

    def update_contact_attributes(
        self, *, InitialContactId: str, InstanceId: str, Attributes: Mapping[str, str]
    ) -> Dict[str, Any]:
        """
        Creates or updates user-defined contact attributes associated with the specified
        contact.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.update_contact_attributes)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#update_contact_attributes)
        """

    def update_contact_evaluation(
        self,
        *,
        InstanceId: str,
        EvaluationId: str,
        Answers: Mapping[str, EvaluationAnswerInputTypeDef] = ...,
        Notes: Mapping[str, EvaluationNoteTypeDef] = ...
    ) -> UpdateContactEvaluationResponseTypeDef:
        """
        Updates details about a contact evaluation in the specified Amazon Connect
        instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.update_contact_evaluation)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#update_contact_evaluation)
        """

    def update_contact_flow_content(
        self, *, InstanceId: str, ContactFlowId: str, Content: str
    ) -> Dict[str, Any]:
        """
        Updates the specified flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.update_contact_flow_content)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#update_contact_flow_content)
        """

    def update_contact_flow_metadata(
        self,
        *,
        InstanceId: str,
        ContactFlowId: str,
        Name: str = ...,
        Description: str = ...,
        ContactFlowState: ContactFlowStateType = ...
    ) -> Dict[str, Any]:
        """
        Updates metadata about specified flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.update_contact_flow_metadata)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#update_contact_flow_metadata)
        """

    def update_contact_flow_module_content(
        self, *, InstanceId: str, ContactFlowModuleId: str, Content: str
    ) -> Dict[str, Any]:
        """
        Updates specified flow module for the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.update_contact_flow_module_content)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#update_contact_flow_module_content)
        """

    def update_contact_flow_module_metadata(
        self,
        *,
        InstanceId: str,
        ContactFlowModuleId: str,
        Name: str = ...,
        Description: str = ...,
        State: ContactFlowModuleStateType = ...
    ) -> Dict[str, Any]:
        """
        Updates metadata about specified flow module.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.update_contact_flow_module_metadata)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#update_contact_flow_module_metadata)
        """

    def update_contact_flow_name(
        self, *, InstanceId: str, ContactFlowId: str, Name: str = ..., Description: str = ...
    ) -> Dict[str, Any]:
        """
        The name of the flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.update_contact_flow_name)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#update_contact_flow_name)
        """

    def update_contact_schedule(
        self, *, InstanceId: str, ContactId: str, ScheduledTime: TimestampTypeDef
    ) -> Dict[str, Any]:
        """
        Updates the scheduled time of a task contact that is already scheduled.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.update_contact_schedule)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#update_contact_schedule)
        """

    def update_evaluation_form(
        self,
        *,
        InstanceId: str,
        EvaluationFormId: str,
        EvaluationFormVersion: int,
        Title: str,
        Items: Sequence["EvaluationFormItemTypeDef"],
        CreateNewVersion: bool = ...,
        Description: str = ...,
        ScoringStrategy: EvaluationFormScoringStrategyTypeDef = ...,
        ClientToken: str = ...
    ) -> UpdateEvaluationFormResponseTypeDef:
        """
        Updates details about a specific evaluation form version in the specified Amazon
        Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.update_evaluation_form)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#update_evaluation_form)
        """

    def update_hours_of_operation(
        self,
        *,
        InstanceId: str,
        HoursOfOperationId: str,
        Name: str = ...,
        Description: str = ...,
        TimeZone: str = ...,
        Config: Sequence[HoursOfOperationConfigTypeDef] = ...
    ) -> EmptyResponseMetadataTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.update_hours_of_operation)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#update_hours_of_operation)
        """

    def update_instance_attribute(
        self, *, InstanceId: str, AttributeType: InstanceAttributeTypeType, Value: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.update_instance_attribute)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#update_instance_attribute)
        """

    def update_instance_storage_config(
        self,
        *,
        InstanceId: str,
        AssociationId: str,
        ResourceType: InstanceStorageResourceTypeType,
        StorageConfig: InstanceStorageConfigTypeDef
    ) -> EmptyResponseMetadataTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.update_instance_storage_config)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#update_instance_storage_config)
        """

    def update_participant_role_config(
        self,
        *,
        InstanceId: str,
        ContactId: str,
        ChannelConfiguration: UpdateParticipantRoleConfigChannelInfoTypeDef
    ) -> Dict[str, Any]:
        """
        Updates timeouts for when human chat participants are to be considered idle, and
        when agents are automatically disconnected from a chat due to idleness.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.update_participant_role_config)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#update_participant_role_config)
        """

    def update_phone_number(
        self, *, PhoneNumberId: str, TargetArn: str, ClientToken: str = ...
    ) -> UpdatePhoneNumberResponseTypeDef:
        """
        Updates your claimed phone number from its current Amazon Connect instance or
        traffic distribution group to another Amazon Connect instance or traffic
        distribution group in the same Amazon Web Services Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.update_phone_number)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#update_phone_number)
        """

    def update_prompt(
        self,
        *,
        InstanceId: str,
        PromptId: str,
        Name: str = ...,
        Description: str = ...,
        S3Uri: str = ...
    ) -> UpdatePromptResponseTypeDef:
        """
        Updates a prompt.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.update_prompt)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#update_prompt)
        """

    def update_queue_hours_of_operation(
        self, *, InstanceId: str, QueueId: str, HoursOfOperationId: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.update_queue_hours_of_operation)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#update_queue_hours_of_operation)
        """

    def update_queue_max_contacts(
        self, *, InstanceId: str, QueueId: str, MaxContacts: int = ...
    ) -> EmptyResponseMetadataTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.update_queue_max_contacts)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#update_queue_max_contacts)
        """

    def update_queue_name(
        self, *, InstanceId: str, QueueId: str, Name: str = ..., Description: str = ...
    ) -> EmptyResponseMetadataTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.update_queue_name)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#update_queue_name)
        """

    def update_queue_outbound_caller_config(
        self, *, InstanceId: str, QueueId: str, OutboundCallerConfig: OutboundCallerConfigTypeDef
    ) -> EmptyResponseMetadataTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.update_queue_outbound_caller_config)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#update_queue_outbound_caller_config)
        """

    def update_queue_status(
        self, *, InstanceId: str, QueueId: str, Status: QueueStatusType
    ) -> EmptyResponseMetadataTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.update_queue_status)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#update_queue_status)
        """

    def update_quick_connect_config(
        self, *, InstanceId: str, QuickConnectId: str, QuickConnectConfig: QuickConnectConfigTypeDef
    ) -> EmptyResponseMetadataTypeDef:
        """
        Updates the configuration settings for the specified quick connect.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.update_quick_connect_config)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#update_quick_connect_config)
        """

    def update_quick_connect_name(
        self, *, InstanceId: str, QuickConnectId: str, Name: str = ..., Description: str = ...
    ) -> EmptyResponseMetadataTypeDef:
        """
        Updates the name and description of a quick connect.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.update_quick_connect_name)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#update_quick_connect_name)
        """

    def update_routing_profile_agent_availability_timer(
        self,
        *,
        InstanceId: str,
        RoutingProfileId: str,
        AgentAvailabilityTimer: AgentAvailabilityTimerType
    ) -> EmptyResponseMetadataTypeDef:
        """
        Whether agents with this routing profile will have their routing order
        calculated based on *time since their last inbound contact* or *longest idle
        time*.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.update_routing_profile_agent_availability_timer)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#update_routing_profile_agent_availability_timer)
        """

    def update_routing_profile_concurrency(
        self,
        *,
        InstanceId: str,
        RoutingProfileId: str,
        MediaConcurrencies: Sequence[MediaConcurrencyTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Updates the channels that agents can handle in the Contact Control Panel (CCP)
        for a routing profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.update_routing_profile_concurrency)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#update_routing_profile_concurrency)
        """

    def update_routing_profile_default_outbound_queue(
        self, *, InstanceId: str, RoutingProfileId: str, DefaultOutboundQueueId: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Updates the default outbound queue of a routing profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.update_routing_profile_default_outbound_queue)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#update_routing_profile_default_outbound_queue)
        """

    def update_routing_profile_name(
        self, *, InstanceId: str, RoutingProfileId: str, Name: str = ..., Description: str = ...
    ) -> EmptyResponseMetadataTypeDef:
        """
        Updates the name and description of a routing profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.update_routing_profile_name)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#update_routing_profile_name)
        """

    def update_routing_profile_queues(
        self,
        *,
        InstanceId: str,
        RoutingProfileId: str,
        QueueConfigs: Sequence[RoutingProfileQueueConfigTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Updates the properties associated with a set of queues for a routing profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.update_routing_profile_queues)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#update_routing_profile_queues)
        """

    def update_rule(
        self,
        *,
        RuleId: str,
        InstanceId: str,
        Name: str,
        Function: str,
        Actions: Sequence[RuleActionTypeDef],
        PublishStatus: RulePublishStatusType
    ) -> EmptyResponseMetadataTypeDef:
        """
        Updates a rule for the specified Amazon Connect instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.update_rule)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#update_rule)
        """

    def update_security_profile(
        self,
        *,
        SecurityProfileId: str,
        InstanceId: str,
        Description: str = ...,
        Permissions: Sequence[str] = ...,
        AllowedAccessControlTags: Mapping[str, str] = ...,
        TagRestrictedResources: Sequence[str] = ...
    ) -> EmptyResponseMetadataTypeDef:
        """
        This API is in preview release for Amazon Connect and is subject to change.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.update_security_profile)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#update_security_profile)
        """

    def update_task_template(
        self,
        *,
        TaskTemplateId: str,
        InstanceId: str,
        Name: str = ...,
        Description: str = ...,
        ContactFlowId: str = ...,
        Constraints: TaskTemplateConstraintsTypeDef = ...,
        Defaults: TaskTemplateDefaultsTypeDef = ...,
        Status: TaskTemplateStatusType = ...,
        Fields: Sequence[TaskTemplateFieldTypeDef] = ...
    ) -> UpdateTaskTemplateResponseTypeDef:
        """
        Updates details about a specific task template in the specified Amazon Connect
        instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.update_task_template)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#update_task_template)
        """

    def update_traffic_distribution(
        self,
        *,
        Id: str,
        TelephonyConfig: TelephonyConfigTypeDef = ...,
        SignInConfig: SignInConfigTypeDef = ...,
        AgentConfig: AgentConfigTypeDef = ...
    ) -> Dict[str, Any]:
        """
        Updates the traffic distribution for a given traffic distribution group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.update_traffic_distribution)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#update_traffic_distribution)
        """

    def update_user_hierarchy(
        self, *, UserId: str, InstanceId: str, HierarchyGroupId: str = ...
    ) -> EmptyResponseMetadataTypeDef:
        """
        Assigns the specified hierarchy group to the specified user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.update_user_hierarchy)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#update_user_hierarchy)
        """

    def update_user_hierarchy_group_name(
        self, *, Name: str, HierarchyGroupId: str, InstanceId: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Updates the name of the user hierarchy group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.update_user_hierarchy_group_name)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#update_user_hierarchy_group_name)
        """

    def update_user_hierarchy_structure(
        self, *, HierarchyStructure: HierarchyStructureUpdateTypeDef, InstanceId: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Updates the user hierarchy structure: add, remove, and rename user hierarchy
        levels.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.update_user_hierarchy_structure)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#update_user_hierarchy_structure)
        """

    def update_user_identity_info(
        self, *, IdentityInfo: UserIdentityInfoTypeDef, UserId: str, InstanceId: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Updates the identity information for the specified user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.update_user_identity_info)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#update_user_identity_info)
        """

    def update_user_phone_config(
        self, *, PhoneConfig: UserPhoneConfigTypeDef, UserId: str, InstanceId: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Updates the phone configuration settings for the specified user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.update_user_phone_config)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#update_user_phone_config)
        """

    def update_user_routing_profile(
        self, *, RoutingProfileId: str, UserId: str, InstanceId: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Assigns the specified routing profile to the specified user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.update_user_routing_profile)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#update_user_routing_profile)
        """

    def update_user_security_profiles(
        self, *, SecurityProfileIds: Sequence[str], UserId: str, InstanceId: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Assigns the specified security profiles to the specified user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.update_user_security_profiles)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#update_user_security_profiles)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_metric_data"]) -> GetMetricDataPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_agent_statuses"]
    ) -> ListAgentStatusesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_approved_origins"]
    ) -> ListApprovedOriginsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_bots"]) -> ListBotsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_contact_evaluations"]
    ) -> ListContactEvaluationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_contact_flow_modules"]
    ) -> ListContactFlowModulesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_contact_flows"]
    ) -> ListContactFlowsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_contact_references"]
    ) -> ListContactReferencesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_default_vocabularies"]
    ) -> ListDefaultVocabulariesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_evaluation_form_versions"]
    ) -> ListEvaluationFormVersionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_evaluation_forms"]
    ) -> ListEvaluationFormsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_hours_of_operations"]
    ) -> ListHoursOfOperationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_instance_attributes"]
    ) -> ListInstanceAttributesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_instance_storage_configs"]
    ) -> ListInstanceStorageConfigsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_instances"]) -> ListInstancesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_integration_associations"]
    ) -> ListIntegrationAssociationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_lambda_functions"]
    ) -> ListLambdaFunctionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_lex_bots"]) -> ListLexBotsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_phone_numbers"]
    ) -> ListPhoneNumbersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_phone_numbers_v2"]
    ) -> ListPhoneNumbersV2Paginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_prompts"]) -> ListPromptsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_queue_quick_connects"]
    ) -> ListQueueQuickConnectsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_queues"]) -> ListQueuesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_quick_connects"]
    ) -> ListQuickConnectsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_routing_profile_queues"]
    ) -> ListRoutingProfileQueuesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_routing_profiles"]
    ) -> ListRoutingProfilesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_rules"]) -> ListRulesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_security_keys"]
    ) -> ListSecurityKeysPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_security_profile_permissions"]
    ) -> ListSecurityProfilePermissionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_security_profiles"]
    ) -> ListSecurityProfilesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_task_templates"]
    ) -> ListTaskTemplatesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_traffic_distribution_group_users"]
    ) -> ListTrafficDistributionGroupUsersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_traffic_distribution_groups"]
    ) -> ListTrafficDistributionGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_use_cases"]) -> ListUseCasesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_user_hierarchy_groups"]
    ) -> ListUserHierarchyGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_users"]) -> ListUsersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["search_available_phone_numbers"]
    ) -> SearchAvailablePhoneNumbersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["search_hours_of_operations"]
    ) -> SearchHoursOfOperationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["search_prompts"]) -> SearchPromptsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["search_queues"]) -> SearchQueuesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["search_quick_connects"]
    ) -> SearchQuickConnectsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["search_resource_tags"]
    ) -> SearchResourceTagsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["search_routing_profiles"]
    ) -> SearchRoutingProfilesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["search_security_profiles"]
    ) -> SearchSecurityProfilesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["search_users"]) -> SearchUsersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["search_vocabularies"]
    ) -> SearchVocabulariesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect/client/#get_paginator)
        """
