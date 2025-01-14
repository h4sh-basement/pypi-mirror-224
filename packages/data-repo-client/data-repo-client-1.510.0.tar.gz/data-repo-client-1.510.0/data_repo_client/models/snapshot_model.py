# coding: utf-8

"""
    Data Repository API

    <details><summary>This document defines the REST API for the Terra Data Repository.</summary> <p> **Status: design in progress** There are a few top-level endpoints (besides some used by swagger):  * / - generated by swagger: swagger API page that provides this documentation and a live UI for submitting REST requests  * /status - provides the operational status of the service  * /configuration - provides the basic configuration and information about the service  * /api - is the authenticated and authorized Data Repository API  * /ga4gh/drs/v1 - is a transcription of the Data Repository Service API  The API endpoints are organized by interface. Each interface is separately versioned. <p> **Notes on Naming** <p> All of the reference items are suffixed with \\\"Model\\\". Those names are used as the class names in the generated Java code. It is helpful to distinguish these model classes from other related classes, like the DAO classes and the operation classes. </details>   # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from data_repo_client.configuration import Configuration


class SnapshotModel(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'id': 'str',
        'name': 'str',
        'description': 'str',
        'created_date': 'str',
        'consent_code': 'str',
        'source': 'list[SnapshotSourceModel]',
        'tables': 'list[TableModel]',
        'relationships': 'list[RelationshipModel]',
        'profile_id': 'str',
        'data_project': 'str',
        'access_information': 'AccessInfoModel',
        'creation_information': 'SnapshotRequestContentsModel',
        'cloud_platform': 'CloudPlatform',
        'properties': 'object',
        'duos_firecloud_group': 'DuosFirecloudGroupModel',
        'global_file_ids': 'bool',
        'compact_id_prefix': 'str',
        'tags': 'list[str]',
        'resource_locks': 'ResourceLocks'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'created_date': 'createdDate',
        'consent_code': 'consentCode',
        'source': 'source',
        'tables': 'tables',
        'relationships': 'relationships',
        'profile_id': 'profileId',
        'data_project': 'dataProject',
        'access_information': 'accessInformation',
        'creation_information': 'creationInformation',
        'cloud_platform': 'cloudPlatform',
        'properties': 'properties',
        'duos_firecloud_group': 'duosFirecloudGroup',
        'global_file_ids': 'globalFileIds',
        'compact_id_prefix': 'compactIdPrefix',
        'tags': 'tags',
        'resource_locks': 'resourceLocks'
    }

    def __init__(self, id=None, name=None, description=None, created_date=None, consent_code=None, source=None, tables=None, relationships=None, profile_id=None, data_project=None, access_information=None, creation_information=None, cloud_platform=None, properties=None, duos_firecloud_group=None, global_file_ids=False, compact_id_prefix=None, tags=None, resource_locks=None, local_vars_configuration=None):  # noqa: E501
        """SnapshotModel - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._description = None
        self._created_date = None
        self._consent_code = None
        self._source = None
        self._tables = None
        self._relationships = None
        self._profile_id = None
        self._data_project = None
        self._access_information = None
        self._creation_information = None
        self._cloud_platform = None
        self._properties = None
        self._duos_firecloud_group = None
        self._global_file_ids = None
        self._compact_id_prefix = None
        self._tags = None
        self._resource_locks = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if created_date is not None:
            self.created_date = created_date
        if consent_code is not None:
            self.consent_code = consent_code
        if source is not None:
            self.source = source
        if tables is not None:
            self.tables = tables
        if relationships is not None:
            self.relationships = relationships
        if profile_id is not None:
            self.profile_id = profile_id
        if data_project is not None:
            self.data_project = data_project
        if access_information is not None:
            self.access_information = access_information
        if creation_information is not None:
            self.creation_information = creation_information
        if cloud_platform is not None:
            self.cloud_platform = cloud_platform
        if properties is not None:
            self.properties = properties
        if duos_firecloud_group is not None:
            self.duos_firecloud_group = duos_firecloud_group
        if global_file_ids is not None:
            self.global_file_ids = global_file_ids
        if compact_id_prefix is not None:
            self.compact_id_prefix = compact_id_prefix
        if tags is not None:
            self.tags = tags
        if resource_locks is not None:
            self.resource_locks = resource_locks

    @property
    def id(self):
        """Gets the id of this SnapshotModel.  # noqa: E501

        Unique identifier for a dataset, snapshot, etc.   # noqa: E501

        :return: The id of this SnapshotModel.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SnapshotModel.

        Unique identifier for a dataset, snapshot, etc.   # noqa: E501

        :param id: The id of this SnapshotModel.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this SnapshotModel.  # noqa: E501

        Dataset and snapshot names follow this pattern. It is the same as ObjectNameProperty, but has a greater maxLength.   # noqa: E501

        :return: The name of this SnapshotModel.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SnapshotModel.

        Dataset and snapshot names follow this pattern. It is the same as ObjectNameProperty, but has a greater maxLength.   # noqa: E501

        :param name: The name of this SnapshotModel.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 511):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `511`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and not re.search(r'^[a-zA-Z0-9][_a-zA-Z0-9]*$', name)):  # noqa: E501
            raise ValueError(r"Invalid value for `name`, must be a follow pattern or equal to `/^[a-zA-Z0-9][_a-zA-Z0-9]*$/`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this SnapshotModel.  # noqa: E501

        Description of the snapshot  # noqa: E501

        :return: The description of this SnapshotModel.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SnapshotModel.

        Description of the snapshot  # noqa: E501

        :param description: The description of this SnapshotModel.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def created_date(self):
        """Gets the created_date of this SnapshotModel.  # noqa: E501

        Date the snapshot was created  # noqa: E501

        :return: The created_date of this SnapshotModel.  # noqa: E501
        :rtype: str
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """Sets the created_date of this SnapshotModel.

        Date the snapshot was created  # noqa: E501

        :param created_date: The created_date of this SnapshotModel.  # noqa: E501
        :type: str
        """

        self._created_date = created_date

    @property
    def consent_code(self):
        """Gets the consent_code of this SnapshotModel.  # noqa: E501

        Consent code together with PHS ID that will determine user access  # noqa: E501

        :return: The consent_code of this SnapshotModel.  # noqa: E501
        :rtype: str
        """
        return self._consent_code

    @consent_code.setter
    def consent_code(self, consent_code):
        """Sets the consent_code of this SnapshotModel.

        Consent code together with PHS ID that will determine user access  # noqa: E501

        :param consent_code: The consent_code of this SnapshotModel.  # noqa: E501
        :type: str
        """

        self._consent_code = consent_code

    @property
    def source(self):
        """Gets the source of this SnapshotModel.  # noqa: E501

        A singleton collection whose sole element represents the snapshot's source dataset.   # noqa: E501

        :return: The source of this SnapshotModel.  # noqa: E501
        :rtype: list[SnapshotSourceModel]
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this SnapshotModel.

        A singleton collection whose sole element represents the snapshot's source dataset.   # noqa: E501

        :param source: The source of this SnapshotModel.  # noqa: E501
        :type: list[SnapshotSourceModel]
        """

        self._source = source

    @property
    def tables(self):
        """Gets the tables of this SnapshotModel.  # noqa: E501


        :return: The tables of this SnapshotModel.  # noqa: E501
        :rtype: list[TableModel]
        """
        return self._tables

    @tables.setter
    def tables(self, tables):
        """Sets the tables of this SnapshotModel.


        :param tables: The tables of this SnapshotModel.  # noqa: E501
        :type: list[TableModel]
        """

        self._tables = tables

    @property
    def relationships(self):
        """Gets the relationships of this SnapshotModel.  # noqa: E501


        :return: The relationships of this SnapshotModel.  # noqa: E501
        :rtype: list[RelationshipModel]
        """
        return self._relationships

    @relationships.setter
    def relationships(self, relationships):
        """Sets the relationships of this SnapshotModel.


        :param relationships: The relationships of this SnapshotModel.  # noqa: E501
        :type: list[RelationshipModel]
        """

        self._relationships = relationships

    @property
    def profile_id(self):
        """Gets the profile_id of this SnapshotModel.  # noqa: E501

        Unique identifier for a dataset, snapshot, etc.   # noqa: E501

        :return: The profile_id of this SnapshotModel.  # noqa: E501
        :rtype: str
        """
        return self._profile_id

    @profile_id.setter
    def profile_id(self, profile_id):
        """Sets the profile_id of this SnapshotModel.

        Unique identifier for a dataset, snapshot, etc.   # noqa: E501

        :param profile_id: The profile_id of this SnapshotModel.  # noqa: E501
        :type: str
        """

        self._profile_id = profile_id

    @property
    def data_project(self):
        """Gets the data_project of this SnapshotModel.  # noqa: E501

        Project id of the snapshot data project  # noqa: E501

        :return: The data_project of this SnapshotModel.  # noqa: E501
        :rtype: str
        """
        return self._data_project

    @data_project.setter
    def data_project(self, data_project):
        """Sets the data_project of this SnapshotModel.

        Project id of the snapshot data project  # noqa: E501

        :param data_project: The data_project of this SnapshotModel.  # noqa: E501
        :type: str
        """

        self._data_project = data_project

    @property
    def access_information(self):
        """Gets the access_information of this SnapshotModel.  # noqa: E501


        :return: The access_information of this SnapshotModel.  # noqa: E501
        :rtype: AccessInfoModel
        """
        return self._access_information

    @access_information.setter
    def access_information(self, access_information):
        """Sets the access_information of this SnapshotModel.


        :param access_information: The access_information of this SnapshotModel.  # noqa: E501
        :type: AccessInfoModel
        """

        self._access_information = access_information

    @property
    def creation_information(self):
        """Gets the creation_information of this SnapshotModel.  # noqa: E501


        :return: The creation_information of this SnapshotModel.  # noqa: E501
        :rtype: SnapshotRequestContentsModel
        """
        return self._creation_information

    @creation_information.setter
    def creation_information(self, creation_information):
        """Sets the creation_information of this SnapshotModel.


        :param creation_information: The creation_information of this SnapshotModel.  # noqa: E501
        :type: SnapshotRequestContentsModel
        """

        self._creation_information = creation_information

    @property
    def cloud_platform(self):
        """Gets the cloud_platform of this SnapshotModel.  # noqa: E501


        :return: The cloud_platform of this SnapshotModel.  # noqa: E501
        :rtype: CloudPlatform
        """
        return self._cloud_platform

    @cloud_platform.setter
    def cloud_platform(self, cloud_platform):
        """Sets the cloud_platform of this SnapshotModel.


        :param cloud_platform: The cloud_platform of this SnapshotModel.  # noqa: E501
        :type: CloudPlatform
        """

        self._cloud_platform = cloud_platform

    @property
    def properties(self):
        """Gets the properties of this SnapshotModel.  # noqa: E501

        Additional JSON metadata about the snapshot (this does not need to adhere to a particular schema)  # noqa: E501

        :return: The properties of this SnapshotModel.  # noqa: E501
        :rtype: object
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this SnapshotModel.

        Additional JSON metadata about the snapshot (this does not need to adhere to a particular schema)  # noqa: E501

        :param properties: The properties of this SnapshotModel.  # noqa: E501
        :type: object
        """

        self._properties = properties

    @property
    def duos_firecloud_group(self):
        """Gets the duos_firecloud_group of this SnapshotModel.  # noqa: E501


        :return: The duos_firecloud_group of this SnapshotModel.  # noqa: E501
        :rtype: DuosFirecloudGroupModel
        """
        return self._duos_firecloud_group

    @duos_firecloud_group.setter
    def duos_firecloud_group(self, duos_firecloud_group):
        """Sets the duos_firecloud_group of this SnapshotModel.


        :param duos_firecloud_group: The duos_firecloud_group of this SnapshotModel.  # noqa: E501
        :type: DuosFirecloudGroupModel
        """

        self._duos_firecloud_group = duos_firecloud_group

    @property
    def global_file_ids(self):
        """Gets the global_file_ids of this SnapshotModel.  # noqa: E501

        if false, the drs ids will be in the format: v1_<snapshotid>_<fileid> if true, drs ids will be in the format: v2_<fileid>   # noqa: E501

        :return: The global_file_ids of this SnapshotModel.  # noqa: E501
        :rtype: bool
        """
        return self._global_file_ids

    @global_file_ids.setter
    def global_file_ids(self, global_file_ids):
        """Sets the global_file_ids of this SnapshotModel.

        if false, the drs ids will be in the format: v1_<snapshotid>_<fileid> if true, drs ids will be in the format: v2_<fileid>   # noqa: E501

        :param global_file_ids: The global_file_ids of this SnapshotModel.  # noqa: E501
        :type: bool
        """

        self._global_file_ids = global_file_ids

    @property
    def compact_id_prefix(self):
        """Gets the compact_id_prefix of this SnapshotModel.  # noqa: E501

        if present, the drs URIs will be rendered using the compact id format (drs://<compactIdPrefix>:<drsId>) instead of the original format (drs://<hostname>/<drsId>).  The format is [A-Za-z0-9._] and the prefix must be registered at identifiers.org   # noqa: E501

        :return: The compact_id_prefix of this SnapshotModel.  # noqa: E501
        :rtype: str
        """
        return self._compact_id_prefix

    @compact_id_prefix.setter
    def compact_id_prefix(self, compact_id_prefix):
        """Sets the compact_id_prefix of this SnapshotModel.

        if present, the drs URIs will be rendered using the compact id format (drs://<compactIdPrefix>:<drsId>) instead of the original format (drs://<hostname>/<drsId>).  The format is [A-Za-z0-9._] and the prefix must be registered at identifiers.org   # noqa: E501

        :param compact_id_prefix: The compact_id_prefix of this SnapshotModel.  # noqa: E501
        :type: str
        """

        self._compact_id_prefix = compact_id_prefix

    @property
    def tags(self):
        """Gets the tags of this SnapshotModel.  # noqa: E501


        :return: The tags of this SnapshotModel.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this SnapshotModel.


        :param tags: The tags of this SnapshotModel.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def resource_locks(self):
        """Gets the resource_locks of this SnapshotModel.  # noqa: E501


        :return: The resource_locks of this SnapshotModel.  # noqa: E501
        :rtype: ResourceLocks
        """
        return self._resource_locks

    @resource_locks.setter
    def resource_locks(self, resource_locks):
        """Sets the resource_locks of this SnapshotModel.


        :param resource_locks: The resource_locks of this SnapshotModel.  # noqa: E501
        :type: ResourceLocks
        """

        self._resource_locks = resource_locks

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SnapshotModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SnapshotModel):
            return True

        return self.to_dict() != other.to_dict()
