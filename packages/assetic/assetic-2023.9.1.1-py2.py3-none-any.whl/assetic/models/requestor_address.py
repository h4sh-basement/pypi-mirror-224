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

##from assetic.models.embedded_resource import EmbeddedResource  # noqa: F401,E501
##from assetic.models.link import Link  # noqa: F401,E501
##from assetic.models.requestor_physical_location import RequestorPhysicalLocation  # noqa: F401,E501
##from assetic.models.requestor_spatial_location import RequestorSpatialLocation  # noqa: F401,E501


class RequestorAddress(object):
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
        'physical_location': 'RequestorPhysicalLocation',
        'spatial_location': 'RequestorSpatialLocation',
        'links': 'list[Link]',
        'embedded': 'list[EmbeddedResource]'
    }

    attribute_map = {
        'physical_location': 'PhysicalLocation',
        'spatial_location': 'SpatialLocation',
        'links': '_links',
        'embedded': '_embedded'
    }

    def __init__(self, physical_location=None, spatial_location=None, links=None, embedded=None):  # noqa: E501
        """RequestorAddress - a model defined in Swagger"""  # noqa: E501

        self._physical_location = None
        self._spatial_location = None
        self._links = None
        self._embedded = None
        self.discriminator = None

        if physical_location is not None:
            self.physical_location = physical_location
        if spatial_location is not None:
            self.spatial_location = spatial_location
        if links is not None:
            self.links = links
        if embedded is not None:
            self.embedded = embedded

    @property
    def physical_location(self):
        """Gets the physical_location of this RequestorAddress.  # noqa: E501


        :return: The physical_location of this RequestorAddress.  # noqa: E501
        :rtype: RequestorPhysicalLocation
        """
        return self._physical_location

    @physical_location.setter
    def physical_location(self, physical_location):
        """Sets the physical_location of this RequestorAddress.


        :param physical_location: The physical_location of this RequestorAddress.  # noqa: E501
        :type: RequestorPhysicalLocation
        """

        self._physical_location = physical_location

    @property
    def spatial_location(self):
        """Gets the spatial_location of this RequestorAddress.  # noqa: E501


        :return: The spatial_location of this RequestorAddress.  # noqa: E501
        :rtype: RequestorSpatialLocation
        """
        return self._spatial_location

    @spatial_location.setter
    def spatial_location(self, spatial_location):
        """Sets the spatial_location of this RequestorAddress.


        :param spatial_location: The spatial_location of this RequestorAddress.  # noqa: E501
        :type: RequestorSpatialLocation
        """

        self._spatial_location = spatial_location

    @property
    def links(self):
        """Gets the links of this RequestorAddress.  # noqa: E501


        :return: The links of this RequestorAddress.  # noqa: E501
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this RequestorAddress.


        :param links: The links of this RequestorAddress.  # noqa: E501
        :type: list[Link]
        """

        self._links = links

    @property
    def embedded(self):
        """Gets the embedded of this RequestorAddress.  # noqa: E501


        :return: The embedded of this RequestorAddress.  # noqa: E501
        :rtype: list[EmbeddedResource]
        """
        return self._embedded

    @embedded.setter
    def embedded(self, embedded):
        """Sets the embedded of this RequestorAddress.


        :param embedded: The embedded of this RequestorAddress.  # noqa: E501
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
        if issubclass(RequestorAddress, dict):
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
        if not isinstance(other, RequestorAddress):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
