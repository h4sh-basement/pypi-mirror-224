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

##from assetic.models.document_representation import DocumentRepresentation  # noqa: F401,E501
##from assetic.models.embedded_resource import EmbeddedResource  # noqa: F401,E501
##from assetic.models.link import Link  # noqa: F401,E501


class DocumentListRepresentation(object):
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
        'total_results': 'int',
        'total_pages': 'int',
        'page': 'int',
        'resource_list': 'list[DocumentRepresentation]',
        'links': 'list[Link]',
        'embedded': 'list[EmbeddedResource]'
    }

    attribute_map = {
        'total_results': 'TotalResults',
        'total_pages': 'TotalPages',
        'page': 'Page',
        'resource_list': 'ResourceList',
        'links': '_links',
        'embedded': '_embedded'
    }

    def __init__(self, total_results=None, total_pages=None, page=None, resource_list=None, links=None, embedded=None):  # noqa: E501
        """DocumentListRepresentation - a model defined in Swagger"""  # noqa: E501

        self._total_results = None
        self._total_pages = None
        self._page = None
        self._resource_list = None
        self._links = None
        self._embedded = None
        self.discriminator = None

        if total_results is not None:
            self.total_results = total_results
        if total_pages is not None:
            self.total_pages = total_pages
        if page is not None:
            self.page = page
        if resource_list is not None:
            self.resource_list = resource_list
        if links is not None:
            self.links = links
        if embedded is not None:
            self.embedded = embedded

    @property
    def total_results(self):
        """Gets the total_results of this DocumentListRepresentation.  # noqa: E501


        :return: The total_results of this DocumentListRepresentation.  # noqa: E501
        :rtype: int
        """
        return self._total_results

    @total_results.setter
    def total_results(self, total_results):
        """Sets the total_results of this DocumentListRepresentation.


        :param total_results: The total_results of this DocumentListRepresentation.  # noqa: E501
        :type: int
        """

        self._total_results = total_results

    @property
    def total_pages(self):
        """Gets the total_pages of this DocumentListRepresentation.  # noqa: E501


        :return: The total_pages of this DocumentListRepresentation.  # noqa: E501
        :rtype: int
        """
        return self._total_pages

    @total_pages.setter
    def total_pages(self, total_pages):
        """Sets the total_pages of this DocumentListRepresentation.


        :param total_pages: The total_pages of this DocumentListRepresentation.  # noqa: E501
        :type: int
        """

        self._total_pages = total_pages

    @property
    def page(self):
        """Gets the page of this DocumentListRepresentation.  # noqa: E501


        :return: The page of this DocumentListRepresentation.  # noqa: E501
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this DocumentListRepresentation.


        :param page: The page of this DocumentListRepresentation.  # noqa: E501
        :type: int
        """

        self._page = page

    @property
    def resource_list(self):
        """Gets the resource_list of this DocumentListRepresentation.  # noqa: E501


        :return: The resource_list of this DocumentListRepresentation.  # noqa: E501
        :rtype: list[DocumentRepresentation]
        """
        return self._resource_list

    @resource_list.setter
    def resource_list(self, resource_list):
        """Sets the resource_list of this DocumentListRepresentation.


        :param resource_list: The resource_list of this DocumentListRepresentation.  # noqa: E501
        :type: list[DocumentRepresentation]
        """

        self._resource_list = resource_list

    @property
    def links(self):
        """Gets the links of this DocumentListRepresentation.  # noqa: E501


        :return: The links of this DocumentListRepresentation.  # noqa: E501
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this DocumentListRepresentation.


        :param links: The links of this DocumentListRepresentation.  # noqa: E501
        :type: list[Link]
        """

        self._links = links

    @property
    def embedded(self):
        """Gets the embedded of this DocumentListRepresentation.  # noqa: E501


        :return: The embedded of this DocumentListRepresentation.  # noqa: E501
        :rtype: list[EmbeddedResource]
        """
        return self._embedded

    @embedded.setter
    def embedded(self, embedded):
        """Sets the embedded of this DocumentListRepresentation.


        :param embedded: The embedded of this DocumentListRepresentation.  # noqa: E501
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
        if issubclass(DocumentListRepresentation, dict):
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
        if not isinstance(other, DocumentListRepresentation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
