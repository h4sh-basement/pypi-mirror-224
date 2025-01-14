# coding: utf-8

"""
    Assetic Integration API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

##from assetic.models.assessment_form_tab_representation import AssessmentFormTabRepresentation  # noqa: F401,E501
##from assetic.models.document_thumb_nail_representation import DocumentThumbNailRepresentation  # noqa: F401,E501
##from assetic.models.embedded_resource import EmbeddedResource  # noqa: F401,E501
##from assetic.models.link import Link  # noqa: F401,E501


class AssessmentFormPageRepresentation(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'label': 'str',
        'version': 'int',
        'can_add_attachment': 'bool',
        'form_tabs': 'list[AssessmentFormTabRepresentation]',
        'applicable_level': 'str',
        'applicable_level_name': 'str',
        'attached_documents': 'list[DocumentThumbNailRepresentation]',
        'links': 'list[Link]',
        'embedded': 'list[EmbeddedResource]'
    }

    attribute_map = {
        'name': 'Name',
        'label': 'Label',
        'version': 'Version',
        'can_add_attachment': 'CanAddAttachment',
        'form_tabs': 'FormTabs',
        'applicable_level': 'ApplicableLevel',
        'applicable_level_name': 'ApplicableLevelName',
        'attached_documents': 'AttachedDocuments',
        'links': '_links',
        'embedded': '_embedded'
    }

    def __init__(self, name=None, label=None, version=None, can_add_attachment=None, form_tabs=None, applicable_level=None, applicable_level_name=None, attached_documents=None, links=None, embedded=None):  # noqa: E501
        """AssessmentFormPageRepresentation - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._label = None
        self._version = None
        self._can_add_attachment = None
        self._form_tabs = None
        self._applicable_level = None
        self._applicable_level_name = None
        self._attached_documents = None
        self._links = None
        self._embedded = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if label is not None:
            self.label = label
        if version is not None:
            self.version = version
        if can_add_attachment is not None:
            self.can_add_attachment = can_add_attachment
        if form_tabs is not None:
            self.form_tabs = form_tabs
        if applicable_level is not None:
            self.applicable_level = applicable_level
        if applicable_level_name is not None:
            self.applicable_level_name = applicable_level_name
        if attached_documents is not None:
            self.attached_documents = attached_documents
        if links is not None:
            self.links = links
        if embedded is not None:
            self.embedded = embedded

    @property
    def name(self):
        """Gets the name of this AssessmentFormPageRepresentation.  # noqa: E501


        :return: The name of this AssessmentFormPageRepresentation.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AssessmentFormPageRepresentation.


        :param name: The name of this AssessmentFormPageRepresentation.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def label(self):
        """Gets the label of this AssessmentFormPageRepresentation.  # noqa: E501


        :return: The label of this AssessmentFormPageRepresentation.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this AssessmentFormPageRepresentation.


        :param label: The label of this AssessmentFormPageRepresentation.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def version(self):
        """Gets the version of this AssessmentFormPageRepresentation.  # noqa: E501


        :return: The version of this AssessmentFormPageRepresentation.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this AssessmentFormPageRepresentation.


        :param version: The version of this AssessmentFormPageRepresentation.  # noqa: E501
        :type: int
        """

        self._version = version

    @property
    def can_add_attachment(self):
        """Gets the can_add_attachment of this AssessmentFormPageRepresentation.  # noqa: E501


        :return: The can_add_attachment of this AssessmentFormPageRepresentation.  # noqa: E501
        :rtype: bool
        """
        return self._can_add_attachment

    @can_add_attachment.setter
    def can_add_attachment(self, can_add_attachment):
        """Sets the can_add_attachment of this AssessmentFormPageRepresentation.


        :param can_add_attachment: The can_add_attachment of this AssessmentFormPageRepresentation.  # noqa: E501
        :type: bool
        """

        self._can_add_attachment = can_add_attachment

    @property
    def form_tabs(self):
        """Gets the form_tabs of this AssessmentFormPageRepresentation.  # noqa: E501


        :return: The form_tabs of this AssessmentFormPageRepresentation.  # noqa: E501
        :rtype: list[AssessmentFormTabRepresentation]
        """
        return self._form_tabs

    @form_tabs.setter
    def form_tabs(self, form_tabs):
        """Sets the form_tabs of this AssessmentFormPageRepresentation.


        :param form_tabs: The form_tabs of this AssessmentFormPageRepresentation.  # noqa: E501
        :type: list[AssessmentFormTabRepresentation]
        """

        self._form_tabs = form_tabs

    @property
    def applicable_level(self):
        """Gets the applicable_level of this AssessmentFormPageRepresentation.  # noqa: E501


        :return: The applicable_level of this AssessmentFormPageRepresentation.  # noqa: E501
        :rtype: str
        """
        return self._applicable_level

    @applicable_level.setter
    def applicable_level(self, applicable_level):
        """Sets the applicable_level of this AssessmentFormPageRepresentation.


        :param applicable_level: The applicable_level of this AssessmentFormPageRepresentation.  # noqa: E501
        :type: str
        """
        allowed_values = ["None", "GroupAsset", "ComplexAsset", "Component", "ComponentServiceCriteria", "NetworkEntity", "SimpleAsset", "WorkOrder", "WorkRequest", "WorkTask", "AssesmentsResult", "Documents", "AsmtProject", "AsmtTask", "ServiceCriteria"]  # noqa: E501
        if "None" in allowed_values:
            allowed_values.append(None)
        if applicable_level not in allowed_values:
            # Could be an integer enum returned by API
            try:
                int_type = int(applicable_level)
            except ValueError:
                raise ValueError(
                    "Invalid value for `applicable_level` ({0}), must be one of {1}"  # noqa: E501
                    .format(applicable_level, allowed_values)
                )

        self._applicable_level = applicable_level

    @property
    def applicable_level_name(self):
        """Gets the applicable_level_name of this AssessmentFormPageRepresentation.  # noqa: E501


        :return: The applicable_level_name of this AssessmentFormPageRepresentation.  # noqa: E501
        :rtype: str
        """
        return self._applicable_level_name

    @applicable_level_name.setter
    def applicable_level_name(self, applicable_level_name):
        """Sets the applicable_level_name of this AssessmentFormPageRepresentation.


        :param applicable_level_name: The applicable_level_name of this AssessmentFormPageRepresentation.  # noqa: E501
        :type: str
        """

        self._applicable_level_name = applicable_level_name

    @property
    def attached_documents(self):
        """Gets the attached_documents of this AssessmentFormPageRepresentation.  # noqa: E501


        :return: The attached_documents of this AssessmentFormPageRepresentation.  # noqa: E501
        :rtype: list[DocumentThumbNailRepresentation]
        """
        return self._attached_documents

    @attached_documents.setter
    def attached_documents(self, attached_documents):
        """Sets the attached_documents of this AssessmentFormPageRepresentation.


        :param attached_documents: The attached_documents of this AssessmentFormPageRepresentation.  # noqa: E501
        :type: list[DocumentThumbNailRepresentation]
        """

        self._attached_documents = attached_documents

    @property
    def links(self):
        """Gets the links of this AssessmentFormPageRepresentation.  # noqa: E501


        :return: The links of this AssessmentFormPageRepresentation.  # noqa: E501
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this AssessmentFormPageRepresentation.


        :param links: The links of this AssessmentFormPageRepresentation.  # noqa: E501
        :type: list[Link]
        """

        self._links = links

    @property
    def embedded(self):
        """Gets the embedded of this AssessmentFormPageRepresentation.  # noqa: E501


        :return: The embedded of this AssessmentFormPageRepresentation.  # noqa: E501
        :rtype: list[EmbeddedResource]
        """
        return self._embedded

    @embedded.setter
    def embedded(self, embedded):
        """Sets the embedded of this AssessmentFormPageRepresentation.


        :param embedded: The embedded of this AssessmentFormPageRepresentation.  # noqa: E501
        :type: list[EmbeddedResource]
        """

        self._embedded = embedded

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(AssessmentFormPageRepresentation, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AssessmentFormPageRepresentation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
