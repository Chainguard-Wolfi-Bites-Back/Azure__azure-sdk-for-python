# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.core.exceptions import HttpResponseError
import msrest.serialization


class BatchRequest(msrest.serialization.Model):
    """Definition for the input batch translation request.

    All required parameters must be populated in order to send to Azure.

    :param source: Required. Source of the input documents.
    :type source: ~azure.ai.translation.document.models.SourceInput
    :param targets: Required. Location of the destination for the output.
    :type targets: list[~azure.ai.translation.document.models.TargetInput]
    :param storage_type: Storage type of the input documents source string. Possible values
     include: "Folder", "File".
    :type storage_type: str or ~azure.ai.translation.document.models.StorageInputType
    """

    _validation = {
        'source': {'required': True},
        'targets': {'required': True},
    }

    _attribute_map = {
        'source': {'key': 'source', 'type': 'SourceInput'},
        'targets': {'key': 'targets', 'type': '[TargetInput]'},
        'storage_type': {'key': 'storageType', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(BatchRequest, self).__init__(**kwargs)
        self.source = kwargs['source']
        self.targets = kwargs['targets']
        self.storage_type = kwargs.get('storage_type', None)


class DocumentFilter(msrest.serialization.Model):
    """DocumentFilter.

    :param prefix: A case-sensitive prefix string to filter documents in the source path for
     translation.
     For example, when using a Azure storage blob Uri, use the prefix to restrict sub folders for
     translation.
    :type prefix: str
    :param suffix: A case-sensitive suffix string to filter documents in the source path for
     translation.
     This is most often use for file extensions.
    :type suffix: str
    """

    _attribute_map = {
        'prefix': {'key': 'prefix', 'type': 'str'},
        'suffix': {'key': 'suffix', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(DocumentFilter, self).__init__(**kwargs)
        self.prefix = kwargs.get('prefix', None)
        self.suffix = kwargs.get('suffix', None)


class DocumentsStatus(msrest.serialization.Model):
    """Documents Status Response.

    All required parameters must be populated in order to send to Azure.

    :param value: Required. The detail status of individual documents.
    :type value: list[~azure.ai.translation.document.models.DocumentStatus]
    :param next_link: Url for the next page.  Null if no more pages available.
    :type next_link: str
    """

    _validation = {
        'value': {'required': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': '[DocumentStatus]'},
        'next_link': {'key': '@nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(DocumentsStatus, self).__init__(**kwargs)
        self.value = kwargs['value']
        self.next_link = kwargs.get('next_link', None)


class DocumentStatus(msrest.serialization.Model):
    """Document Status Response.

    All required parameters must be populated in order to send to Azure.

    :param path: Location of the document or folder.
    :type path: str
    :param source_path: Required. Location of the source document.
    :type source_path: str
    :param created_date_time_utc: Required. Operation created date time.
    :type created_date_time_utc: ~datetime.datetime
    :param last_action_date_time_utc: Required. Date time in which the operation's status has been
     updated.
    :type last_action_date_time_utc: ~datetime.datetime
    :param status: Required. List of possible statuses for job or document. Possible values
     include: "NotStarted", "Running", "Succeeded", "Failed", "Cancelled", "Cancelling",
     "ValidationFailed".
    :type status: str or ~azure.ai.translation.document.models.Status
    :param to: Required. To language.
    :type to: str
    :param error: This contains an outer error with error code, message, details, target and an
     inner error with more descriptive details.
    :type error: ~azure.ai.translation.document.models.TranslationError
    :param progress: Required. Progress of the translation if available.
    :type progress: float
    :param id: Required. Document Id.
    :type id: str
    :param character_charged: Character charged by the API.
    :type character_charged: long
    """

    _validation = {
        'source_path': {'required': True},
        'created_date_time_utc': {'required': True},
        'last_action_date_time_utc': {'required': True},
        'status': {'required': True},
        'to': {'required': True},
        'progress': {'required': True, 'maximum': 1, 'minimum': 0},
        'id': {'required': True},
    }

    _attribute_map = {
        'path': {'key': 'path', 'type': 'str'},
        'source_path': {'key': 'sourcePath', 'type': 'str'},
        'created_date_time_utc': {'key': 'createdDateTimeUtc', 'type': 'iso-8601'},
        'last_action_date_time_utc': {'key': 'lastActionDateTimeUtc', 'type': 'iso-8601'},
        'status': {'key': 'status', 'type': 'str'},
        'to': {'key': 'to', 'type': 'str'},
        'error': {'key': 'error', 'type': 'TranslationError'},
        'progress': {'key': 'progress', 'type': 'float'},
        'id': {'key': 'id', 'type': 'str'},
        'character_charged': {'key': 'characterCharged', 'type': 'long'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(DocumentStatus, self).__init__(**kwargs)
        self.path = kwargs.get('path', None)
        self.source_path = kwargs['source_path']
        self.created_date_time_utc = kwargs['created_date_time_utc']
        self.last_action_date_time_utc = kwargs['last_action_date_time_utc']
        self.status = kwargs['status']
        self.to = kwargs['to']
        self.error = kwargs.get('error', None)
        self.progress = kwargs['progress']
        self.id = kwargs['id']
        self.character_charged = kwargs.get('character_charged', None)


class FileFormat(msrest.serialization.Model):
    """FileFormat.

    All required parameters must be populated in order to send to Azure.

    :param format: Required. Name of the format.
    :type format: str
    :param file_extensions: Required. Supported file extension for this format.
    :type file_extensions: list[str]
    :param content_types: Required. Supported Content-Types for this format.
    :type content_types: list[str]
    :param default_version: Default version if none is specified.
    :type default_version: str
    :param versions: Supported Version.
    :type versions: list[str]
    """

    _validation = {
        'format': {'required': True},
        'file_extensions': {'required': True},
        'content_types': {'required': True},
    }

    _attribute_map = {
        'format': {'key': 'format', 'type': 'str'},
        'file_extensions': {'key': 'fileExtensions', 'type': '[str]'},
        'content_types': {'key': 'contentTypes', 'type': '[str]'},
        'default_version': {'key': 'defaultVersion', 'type': 'str'},
        'versions': {'key': 'versions', 'type': '[str]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(FileFormat, self).__init__(**kwargs)
        self.format = kwargs['format']
        self.file_extensions = kwargs['file_extensions']
        self.content_types = kwargs['content_types']
        self.default_version = kwargs.get('default_version', None)
        self.versions = kwargs.get('versions', None)


class Glossary(msrest.serialization.Model):
    """Glossary / translation memory for the request.

    All required parameters must be populated in order to send to Azure.

    :param glossary_url: Required. Location of the glossary.
     We will use the file extension to extract the formatting if the format parameter is not
     supplied.
    
     If the translation language pair is not present in the glossary, it will not be applied.
    :type glossary_url: str
    :param format: Required. Format.
    :type format: str
    :param version: Optional Version.  If not specified, default is used.
    :type version: str
    :param storage_source: Storage Source. Possible values include: "AzureBlob".
    :type storage_source: str or ~azure.ai.translation.document.models.StorageSource
    """

    _validation = {
        'glossary_url': {'required': True},
        'format': {'required': True},
    }

    _attribute_map = {
        'glossary_url': {'key': 'glossaryUrl', 'type': 'str'},
        'format': {'key': 'format', 'type': 'str'},
        'version': {'key': 'version', 'type': 'str'},
        'storage_source': {'key': 'storageSource', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Glossary, self).__init__(**kwargs)
        self.glossary_url = kwargs['glossary_url']
        self.format = kwargs['format']
        self.version = kwargs.get('version', None)
        self.storage_source = kwargs.get('storage_source', None)


class InnerTranslationError(msrest.serialization.Model):
    """New Inner Error format which conforms to Cognitive Services API Guidelines which is available at https://microsoft.sharepoint.com/%3Aw%3A/t/CognitiveServicesPMO/EUoytcrjuJdKpeOKIK_QRC8BPtUYQpKBi8JsWyeDMRsWlQ?e=CPq8ow.
This contains required properties ErrorCode, message and optional properties target, details(key value pair), inner error(this can be nested).

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :param code: Required. Gets code error string.
    :type code: str
    :param message: Required. Gets high level error message.
    :type message: str
    :ivar target: Gets the source of the error.
     For example it would be "documents" or "document id" in case of invalid document.
    :vartype target: str
    :param inner_error: New Inner Error format which conforms to Cognitive Services API Guidelines
     which is available at
     https://microsoft.sharepoint.com/%3Aw%3A/t/CognitiveServicesPMO/EUoytcrjuJdKpeOKIK_QRC8BPtUYQpKBi8JsWyeDMRsWlQ?e=CPq8ow.
     This contains required properties ErrorCode, message and optional properties target,
     details(key value pair), inner error(this can be nested).
    :type inner_error: ~azure.ai.translation.document.models.InnerTranslationError
    """

    _validation = {
        'code': {'required': True},
        'message': {'required': True},
        'target': {'readonly': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'},
        'inner_error': {'key': 'innerError', 'type': 'InnerTranslationError'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(InnerTranslationError, self).__init__(**kwargs)
        self.code = kwargs['code']
        self.message = kwargs['message']
        self.target = None
        self.inner_error = kwargs.get('inner_error', None)


class SourceInput(msrest.serialization.Model):
    """Source of the input documents.

    All required parameters must be populated in order to send to Azure.

    :param source_url: Required. Location of the folder / container or single file with your
     documents.
    :type source_url: str
    :param filter:
    :type filter: ~azure.ai.translation.document.models.DocumentFilter
    :param language: Language code
     If none is specified, we will perform auto detect on the document.
    :type language: str
    :param storage_source: Storage Source. Possible values include: "AzureBlob".
    :type storage_source: str or ~azure.ai.translation.document.models.StorageSource
    """

    _validation = {
        'source_url': {'required': True},
    }

    _attribute_map = {
        'source_url': {'key': 'sourceUrl', 'type': 'str'},
        'filter': {'key': 'filter', 'type': 'DocumentFilter'},
        'language': {'key': 'language', 'type': 'str'},
        'storage_source': {'key': 'storageSource', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(SourceInput, self).__init__(**kwargs)
        self.source_url = kwargs['source_url']
        self.filter = kwargs.get('filter', None)
        self.language = kwargs.get('language', None)
        self.storage_source = kwargs.get('storage_source', None)


class StartTranslationDetails(msrest.serialization.Model):
    """Translation job submission batch request.

    All required parameters must be populated in order to send to Azure.

    :param inputs: Required. The input list of documents or folders containing documents.
    :type inputs: list[~azure.ai.translation.document.models.BatchRequest]
    """

    _validation = {
        'inputs': {'required': True},
    }

    _attribute_map = {
        'inputs': {'key': 'inputs', 'type': '[BatchRequest]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(StartTranslationDetails, self).__init__(**kwargs)
        self.inputs = kwargs['inputs']


class StatusSummary(msrest.serialization.Model):
    """StatusSummary.

    All required parameters must be populated in order to send to Azure.

    :param total: Required. Total count.
    :type total: int
    :param failed: Required. Failed count.
    :type failed: int
    :param success: Required. Number of Success.
    :type success: int
    :param in_progress: Required. Number of in progress.
    :type in_progress: int
    :param not_yet_started: Required. Count of not yet started.
    :type not_yet_started: int
    :param cancelled: Required. Number of cancelled.
    :type cancelled: int
    :param total_character_charged: Required. Total characters charged by the API.
    :type total_character_charged: long
    """

    _validation = {
        'total': {'required': True},
        'failed': {'required': True},
        'success': {'required': True},
        'in_progress': {'required': True},
        'not_yet_started': {'required': True},
        'cancelled': {'required': True},
        'total_character_charged': {'required': True},
    }

    _attribute_map = {
        'total': {'key': 'total', 'type': 'int'},
        'failed': {'key': 'failed', 'type': 'int'},
        'success': {'key': 'success', 'type': 'int'},
        'in_progress': {'key': 'inProgress', 'type': 'int'},
        'not_yet_started': {'key': 'notYetStarted', 'type': 'int'},
        'cancelled': {'key': 'cancelled', 'type': 'int'},
        'total_character_charged': {'key': 'totalCharacterCharged', 'type': 'long'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(StatusSummary, self).__init__(**kwargs)
        self.total = kwargs['total']
        self.failed = kwargs['failed']
        self.success = kwargs['success']
        self.in_progress = kwargs['in_progress']
        self.not_yet_started = kwargs['not_yet_started']
        self.cancelled = kwargs['cancelled']
        self.total_character_charged = kwargs['total_character_charged']


class SupportedFileFormats(msrest.serialization.Model):
    """Base type for List return in our api.

    All required parameters must be populated in order to send to Azure.

    :param value: Required. list of objects.
    :type value: list[~azure.ai.translation.document.models.FileFormat]
    """

    _validation = {
        'value': {'required': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': '[FileFormat]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(SupportedFileFormats, self).__init__(**kwargs)
        self.value = kwargs['value']


class SupportedStorageSources(msrest.serialization.Model):
    """Base type for List return in our api.

    All required parameters must be populated in order to send to Azure.

    :param value: Required. list of objects.
    :type value: list[str or ~azure.ai.translation.document.models.StorageSource]
    """

    _validation = {
        'value': {'required': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': '[str]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(SupportedStorageSources, self).__init__(**kwargs)
        self.value = kwargs['value']


class TargetInput(msrest.serialization.Model):
    """Destination for the finished translated documents.

    All required parameters must be populated in order to send to Azure.

    :param target_url: Required. Location of the folder / container with your documents.
    :type target_url: str
    :param category: Category / custom system for translation request.
    :type category: str
    :param language: Required. Target Language.
    :type language: str
    :param glossaries: List of Glossary.
    :type glossaries: list[~azure.ai.translation.document.models.Glossary]
    :param storage_source: Storage Source. Possible values include: "AzureBlob".
    :type storage_source: str or ~azure.ai.translation.document.models.StorageSource
    """

    _validation = {
        'target_url': {'required': True},
        'language': {'required': True},
    }

    _attribute_map = {
        'target_url': {'key': 'targetUrl', 'type': 'str'},
        'category': {'key': 'category', 'type': 'str'},
        'language': {'key': 'language', 'type': 'str'},
        'glossaries': {'key': 'glossaries', 'type': '[Glossary]'},
        'storage_source': {'key': 'storageSource', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(TargetInput, self).__init__(**kwargs)
        self.target_url = kwargs['target_url']
        self.category = kwargs.get('category', None)
        self.language = kwargs['language']
        self.glossaries = kwargs.get('glossaries', None)
        self.storage_source = kwargs.get('storage_source', None)


class TranslationError(msrest.serialization.Model):
    """This contains an outer error with error code, message, details, target and an inner error with more descriptive details.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :param code: Required. Enums containing high level error codes. Possible values include:
     "InvalidRequest", "InvalidArgument", "InternalServerError", "ServiceUnavailable",
     "ResourceNotFound", "Unauthorized", "RequestRateTooHigh".
    :type code: str or ~azure.ai.translation.document.models.TranslationErrorCode
    :param message: Required. Gets high level error message.
    :type message: str
    :ivar target: Gets the source of the error.
     For example it would be "documents" or "document id" in case of invalid document.
    :vartype target: str
    :param inner_error: New Inner Error format which conforms to Cognitive Services API Guidelines
     which is available at
     https://microsoft.sharepoint.com/%3Aw%3A/t/CognitiveServicesPMO/EUoytcrjuJdKpeOKIK_QRC8BPtUYQpKBi8JsWyeDMRsWlQ?e=CPq8ow.
     This contains required properties ErrorCode, message and optional properties target,
     details(key value pair), inner error(this can be nested).
    :type inner_error: ~azure.ai.translation.document.models.InnerTranslationError
    """

    _validation = {
        'code': {'required': True},
        'message': {'required': True},
        'target': {'readonly': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'},
        'inner_error': {'key': 'innerError', 'type': 'InnerTranslationError'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(TranslationError, self).__init__(**kwargs)
        self.code = kwargs['code']
        self.message = kwargs['message']
        self.target = None
        self.inner_error = kwargs.get('inner_error', None)


class TranslationErrorResponse(msrest.serialization.Model):
    """Contains unified error information used for HTTP responses across any Cognitive Service. Instances
can be created either through Microsoft.CloudAI.Containers.HttpStatusExceptionV2 or by returning it directly from
a controller.

    :param error: This contains an outer error with error code, message, details, target and an
     inner error with more descriptive details.
    :type error: ~azure.ai.translation.document.models.TranslationError
    """

    _attribute_map = {
        'error': {'key': 'error', 'type': 'TranslationError'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(TranslationErrorResponse, self).__init__(**kwargs)
        self.error = kwargs.get('error', None)


class TranslationsStatus(msrest.serialization.Model):
    """Translation job Status Response.

    All required parameters must be populated in order to send to Azure.

    :param value: Required. The summary status of individual operation.
    :type value: list[~azure.ai.translation.document.models.TranslationStatus]
    :param next_link: Url for the next page.  Null if no more pages available.
    :type next_link: str
    """

    _validation = {
        'value': {'required': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': '[TranslationStatus]'},
        'next_link': {'key': '@nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(TranslationsStatus, self).__init__(**kwargs)
        self.value = kwargs['value']
        self.next_link = kwargs.get('next_link', None)


class TranslationStatus(msrest.serialization.Model):
    """Translation job status response.

    All required parameters must be populated in order to send to Azure.

    :param id: Required. Id of the operation.
    :type id: str
    :param created_date_time_utc: Required. Operation created date time.
    :type created_date_time_utc: ~datetime.datetime
    :param last_action_date_time_utc: Required. Date time in which the operation's status has been
     updated.
    :type last_action_date_time_utc: ~datetime.datetime
    :param status: Required. List of possible statuses for job or document. Possible values
     include: "NotStarted", "Running", "Succeeded", "Failed", "Cancelled", "Cancelling",
     "ValidationFailed".
    :type status: str or ~azure.ai.translation.document.models.Status
    :param error: This contains an outer error with error code, message, details, target and an
     inner error with more descriptive details.
    :type error: ~azure.ai.translation.document.models.TranslationError
    :param summary: Required.
    :type summary: ~azure.ai.translation.document.models.StatusSummary
    """

    _validation = {
        'id': {'required': True},
        'created_date_time_utc': {'required': True},
        'last_action_date_time_utc': {'required': True},
        'status': {'required': True},
        'summary': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'created_date_time_utc': {'key': 'createdDateTimeUtc', 'type': 'iso-8601'},
        'last_action_date_time_utc': {'key': 'lastActionDateTimeUtc', 'type': 'iso-8601'},
        'status': {'key': 'status', 'type': 'str'},
        'error': {'key': 'error', 'type': 'TranslationError'},
        'summary': {'key': 'summary', 'type': 'StatusSummary'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(TranslationStatus, self).__init__(**kwargs)
        self.id = kwargs['id']
        self.created_date_time_utc = kwargs['created_date_time_utc']
        self.last_action_date_time_utc = kwargs['last_action_date_time_utc']
        self.status = kwargs['status']
        self.error = kwargs.get('error', None)
        self.summary = kwargs['summary']
