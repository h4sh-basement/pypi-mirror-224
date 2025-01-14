# coding: utf-8

# flake8: noqa

"""
    Tator REST API

    Interface to the Tator backend.  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

__version__ = "1.1.1"

# import apis into sdk package
from tator.openapi.tator_openapi.api.tator_api import TatorApi

# import ApiClient
from tator.openapi.tator_openapi.api_client import ApiClient
from tator.openapi.tator_openapi.configuration import Configuration
from tator.openapi.tator_openapi.exceptions import OpenApiException
from tator.openapi.tator_openapi.exceptions import ApiTypeError
from tator.openapi.tator_openapi.exceptions import ApiValueError
from tator.openapi.tator_openapi.exceptions import ApiKeyError
from tator.openapi.tator_openapi.exceptions import ApiException
# import models into sdk package
from tator.openapi.tator_openapi.models.affiliation import Affiliation
from tator.openapi.tator_openapi.models.affiliation_spec import AffiliationSpec
from tator.openapi.tator_openapi.models.affiliation_update import AffiliationUpdate
from tator.openapi.tator_openapi.models.algorithm import Algorithm
from tator.openapi.tator_openapi.models.algorithm_manifest import AlgorithmManifest
from tator.openapi.tator_openapi.models.algorithm_manifest_spec import AlgorithmManifestSpec
from tator.openapi.tator_openapi.models.algorithm_parameter import AlgorithmParameter
from tator.openapi.tator_openapi.models.algorithm_spec import AlgorithmSpec
from tator.openapi.tator_openapi.models.announcement import Announcement
from tator.openapi.tator_openapi.models.applet import Applet
from tator.openapi.tator_openapi.models.applet_spec import AppletSpec
from tator.openapi.tator_openapi.models.archive_config import ArchiveConfig
from tator.openapi.tator_openapi.models.attribute_combinator_spec import AttributeCombinatorSpec
from tator.openapi.tator_openapi.models.attribute_filter_spec import AttributeFilterSpec
from tator.openapi.tator_openapi.models.attribute_operation_spec import AttributeOperationSpec
from tator.openapi.tator_openapi.models.attribute_type import AttributeType
from tator.openapi.tator_openapi.models.attribute_type_delete import AttributeTypeDelete
from tator.openapi.tator_openapi.models.attribute_type_spec import AttributeTypeSpec
from tator.openapi.tator_openapi.models.attribute_type_update import AttributeTypeUpdate
from tator.openapi.tator_openapi.models.attribute_type_update_attribute_type_update import AttributeTypeUpdateAttributeTypeUpdate
from tator.openapi.tator_openapi.models.audio_definition import AudioDefinition
from tator.openapi.tator_openapi.models.autocomplete_service import AutocompleteService
from tator.openapi.tator_openapi.models.auxiliary_file_definition import AuxiliaryFileDefinition
from tator.openapi.tator_openapi.models.bad_request_response import BadRequestResponse
from tator.openapi.tator_openapi.models.bookmark import Bookmark
from tator.openapi.tator_openapi.models.bookmark_spec import BookmarkSpec
from tator.openapi.tator_openapi.models.bookmark_update import BookmarkUpdate
from tator.openapi.tator_openapi.models.bucket import Bucket
from tator.openapi.tator_openapi.models.bucket_gcp_config import BucketGCPConfig
from tator.openapi.tator_openapi.models.bucket_oci_config import BucketOCIConfig
from tator.openapi.tator_openapi.models.bucket_oci_native_config import BucketOCINativeConfig
from tator.openapi.tator_openapi.models.bucket_s3_config import BucketS3Config
from tator.openapi.tator_openapi.models.bucket_spec import BucketSpec
from tator.openapi.tator_openapi.models.bucket_update import BucketUpdate
from tator.openapi.tator_openapi.models.change_log import ChangeLog
from tator.openapi.tator_openapi.models.change_log_description_of_change import ChangeLogDescriptionOfChange
from tator.openapi.tator_openapi.models.change_log_description_of_change_new import ChangeLogDescriptionOfChangeNew
from tator.openapi.tator_openapi.models.clone_media_spec import CloneMediaSpec
from tator.openapi.tator_openapi.models.color_map import ColorMap
from tator.openapi.tator_openapi.models.concat_definition import ConcatDefinition
from tator.openapi.tator_openapi.models.create_list_response import CreateListResponse
from tator.openapi.tator_openapi.models.create_response import CreateResponse
from tator.openapi.tator_openapi.models.credentials import Credentials
from tator.openapi.tator_openapi.models.download_info import DownloadInfo
from tator.openapi.tator_openapi.models.download_info_spec import DownloadInfoSpec
from tator.openapi.tator_openapi.models.email_attachment_spec import EmailAttachmentSpec
from tator.openapi.tator_openapi.models.email_spec import EmailSpec
from tator.openapi.tator_openapi.models.encode_config import EncodeConfig
from tator.openapi.tator_openapi.models.favorite import Favorite
from tator.openapi.tator_openapi.models.favorite_spec import FavoriteSpec
from tator.openapi.tator_openapi.models.favorite_update import FavoriteUpdate
from tator.openapi.tator_openapi.models.feed_definition import FeedDefinition
from tator.openapi.tator_openapi.models.file import File
from tator.openapi.tator_openapi.models.file_spec import FileSpec
from tator.openapi.tator_openapi.models.file_type import FileType
from tator.openapi.tator_openapi.models.file_type_spec import FileTypeSpec
from tator.openapi.tator_openapi.models.file_type_update import FileTypeUpdate
from tator.openapi.tator_openapi.models.file_update import FileUpdate
from tator.openapi.tator_openapi.models.fill import Fill
from tator.openapi.tator_openapi.models.float_array_query import FloatArrayQuery
from tator.openapi.tator_openapi.models.generic_file import GenericFile
from tator.openapi.tator_openapi.models.generic_file_spec import GenericFileSpec
from tator.openapi.tator_openapi.models.get_cloned_media_response import GetClonedMediaResponse
from tator.openapi.tator_openapi.models.image_definition import ImageDefinition
from tator.openapi.tator_openapi.models.invitation import Invitation
from tator.openapi.tator_openapi.models.invitation_spec import InvitationSpec
from tator.openapi.tator_openapi.models.invitation_update import InvitationUpdate
from tator.openapi.tator_openapi.models.job import Job
from tator.openapi.tator_openapi.models.job_cluster import JobCluster
from tator.openapi.tator_openapi.models.job_cluster_spec import JobClusterSpec
from tator.openapi.tator_openapi.models.job_node import JobNode
from tator.openapi.tator_openapi.models.job_spec import JobSpec
from tator.openapi.tator_openapi.models.job_spec_failure_email_spec import JobSpecFailureEmailSpec
from tator.openapi.tator_openapi.models.leaf import Leaf
from tator.openapi.tator_openapi.models.leaf_bulk_update import LeafBulkUpdate
from tator.openapi.tator_openapi.models.leaf_id_query import LeafIdQuery
from tator.openapi.tator_openapi.models.leaf_spec import LeafSpec
from tator.openapi.tator_openapi.models.leaf_suggestion import LeafSuggestion
from tator.openapi.tator_openapi.models.leaf_type import LeafType
from tator.openapi.tator_openapi.models.leaf_type_spec import LeafTypeSpec
from tator.openapi.tator_openapi.models.leaf_type_update import LeafTypeUpdate
from tator.openapi.tator_openapi.models.leaf_update import LeafUpdate
from tator.openapi.tator_openapi.models.live_definition import LiveDefinition
from tator.openapi.tator_openapi.models.live_update_definition import LiveUpdateDefinition
from tator.openapi.tator_openapi.models.localization import Localization
from tator.openapi.tator_openapi.models.localization_bulk_delete import LocalizationBulkDelete
from tator.openapi.tator_openapi.models.localization_bulk_update import LocalizationBulkUpdate
from tator.openapi.tator_openapi.models.localization_delete import LocalizationDelete
from tator.openapi.tator_openapi.models.localization_id_query import LocalizationIdQuery
from tator.openapi.tator_openapi.models.localization_spec import LocalizationSpec
from tator.openapi.tator_openapi.models.localization_type import LocalizationType
from tator.openapi.tator_openapi.models.localization_type_spec import LocalizationTypeSpec
from tator.openapi.tator_openapi.models.localization_type_update import LocalizationTypeUpdate
from tator.openapi.tator_openapi.models.localization_update import LocalizationUpdate
from tator.openapi.tator_openapi.models.media import Media
from tator.openapi.tator_openapi.models.media_bulk_update import MediaBulkUpdate
from tator.openapi.tator_openapi.models.media_files import MediaFiles
from tator.openapi.tator_openapi.models.media_id_query import MediaIdQuery
from tator.openapi.tator_openapi.models.media_next import MediaNext
from tator.openapi.tator_openapi.models.media_prev import MediaPrev
from tator.openapi.tator_openapi.models.media_spec import MediaSpec
from tator.openapi.tator_openapi.models.media_stats import MediaStats
from tator.openapi.tator_openapi.models.media_type import MediaType
from tator.openapi.tator_openapi.models.media_type_spec import MediaTypeSpec
from tator.openapi.tator_openapi.models.media_type_update import MediaTypeUpdate
from tator.openapi.tator_openapi.models.media_update import MediaUpdate
from tator.openapi.tator_openapi.models.membership import Membership
from tator.openapi.tator_openapi.models.membership_spec import MembershipSpec
from tator.openapi.tator_openapi.models.membership_update import MembershipUpdate
from tator.openapi.tator_openapi.models.message_response import MessageResponse
from tator.openapi.tator_openapi.models.multi_definition import MultiDefinition
from tator.openapi.tator_openapi.models.not_found_response import NotFoundResponse
from tator.openapi.tator_openapi.models.notify_spec import NotifySpec
from tator.openapi.tator_openapi.models.organization import Organization
from tator.openapi.tator_openapi.models.organization_spec import OrganizationSpec
from tator.openapi.tator_openapi.models.organization_update import OrganizationUpdate
from tator.openapi.tator_openapi.models.password_reset_spec import PasswordResetSpec
from tator.openapi.tator_openapi.models.project import Project
from tator.openapi.tator_openapi.models.project_spec import ProjectSpec
from tator.openapi.tator_openapi.models.project_update import ProjectUpdate
from tator.openapi.tator_openapi.models.resolution_config import ResolutionConfig
from tator.openapi.tator_openapi.models.s3_storage_config import S3StorageConfig
from tator.openapi.tator_openapi.models.section import Section
from tator.openapi.tator_openapi.models.section_spec import SectionSpec
from tator.openapi.tator_openapi.models.section_update import SectionUpdate
from tator.openapi.tator_openapi.models.state import State
from tator.openapi.tator_openapi.models.state_bulk_delete import StateBulkDelete
from tator.openapi.tator_openapi.models.state_bulk_update import StateBulkUpdate
from tator.openapi.tator_openapi.models.state_delete import StateDelete
from tator.openapi.tator_openapi.models.state_id_query import StateIdQuery
from tator.openapi.tator_openapi.models.state_merge_update import StateMergeUpdate
from tator.openapi.tator_openapi.models.state_spec import StateSpec
from tator.openapi.tator_openapi.models.state_trim_update import StateTrimUpdate
from tator.openapi.tator_openapi.models.state_type import StateType
from tator.openapi.tator_openapi.models.state_type_spec import StateTypeSpec
from tator.openapi.tator_openapi.models.state_type_update import StateTypeUpdate
from tator.openapi.tator_openapi.models.state_update import StateUpdate
from tator.openapi.tator_openapi.models.temporary_file import TemporaryFile
from tator.openapi.tator_openapi.models.temporary_file_spec import TemporaryFileSpec
from tator.openapi.tator_openapi.models.token import Token
from tator.openapi.tator_openapi.models.transcode import Transcode
from tator.openapi.tator_openapi.models.transcode_spec import TranscodeSpec
from tator.openapi.tator_openapi.models.upload_completion_spec import UploadCompletionSpec
from tator.openapi.tator_openapi.models.upload_info import UploadInfo
from tator.openapi.tator_openapi.models.upload_part import UploadPart
from tator.openapi.tator_openapi.models.user import User
from tator.openapi.tator_openapi.models.user_spec import UserSpec
from tator.openapi.tator_openapi.models.user_update import UserUpdate
from tator.openapi.tator_openapi.models.version import Version
from tator.openapi.tator_openapi.models.version_spec import VersionSpec
from tator.openapi.tator_openapi.models.version_update import VersionUpdate
from tator.openapi.tator_openapi.models.video_clip import VideoClip
from tator.openapi.tator_openapi.models.video_definition import VideoDefinition

