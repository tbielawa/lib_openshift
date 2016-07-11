# coding: utf-8

"""
Copyright 2016 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems


class V1PolicyRule(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        V1PolicyRule - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'verbs': 'list[str]',
            'attribute_restrictions': 'str',
            'api_groups': 'list[str]',
            'resources': 'list[str]',
            'resource_names': 'list[str]',
            'non_resource_ur_ls': 'list[str]'
        }

        self.attribute_map = {
            'verbs': 'verbs',
            'attribute_restrictions': 'attributeRestrictions',
            'api_groups': 'apiGroups',
            'resources': 'resources',
            'resource_names': 'resourceNames',
            'non_resource_ur_ls': 'nonResourceURLs'
        }

        self._verbs = None
        self._attribute_restrictions = None
        self._api_groups = None
        self._resources = None
        self._resource_names = None
        self._non_resource_ur_ls = None

    @property
    def verbs(self):
        """
        Gets the verbs of this V1PolicyRule.
        Verbs is a list of Verbs that apply to ALL the ResourceKinds and AttributeRestrictions contained in this rule.  VerbAll represents all kinds.

        :return: The verbs of this V1PolicyRule.
        :rtype: list[str]
        """
        return self._verbs

    @verbs.setter
    def verbs(self, verbs):
        """
        Sets the verbs of this V1PolicyRule.
        Verbs is a list of Verbs that apply to ALL the ResourceKinds and AttributeRestrictions contained in this rule.  VerbAll represents all kinds.

        :param verbs: The verbs of this V1PolicyRule.
        :type: list[str]
        """
        self._verbs = verbs

    @property
    def attribute_restrictions(self):
        """
        Gets the attribute_restrictions of this V1PolicyRule.
        AttributeRestrictions will vary depending on what the Authorizer/AuthorizationAttributeBuilder pair supports. If the Authorizer does not recognize how to handle the AttributeRestrictions, the Authorizer should report an error.

        :return: The attribute_restrictions of this V1PolicyRule.
        :rtype: str
        """
        return self._attribute_restrictions

    @attribute_restrictions.setter
    def attribute_restrictions(self, attribute_restrictions):
        """
        Sets the attribute_restrictions of this V1PolicyRule.
        AttributeRestrictions will vary depending on what the Authorizer/AuthorizationAttributeBuilder pair supports. If the Authorizer does not recognize how to handle the AttributeRestrictions, the Authorizer should report an error.

        :param attribute_restrictions: The attribute_restrictions of this V1PolicyRule.
        :type: str
        """
        self._attribute_restrictions = attribute_restrictions

    @property
    def api_groups(self):
        """
        Gets the api_groups of this V1PolicyRule.
        APIGroups is the name of the APIGroup that contains the resources.  If this field is empty, then both kubernetes and origin API groups are assumed. That means that if an action is requested against one of the enumerated resources in either the kubernetes or the origin API group, the request will be allowed

        :return: The api_groups of this V1PolicyRule.
        :rtype: list[str]
        """
        return self._api_groups

    @api_groups.setter
    def api_groups(self, api_groups):
        """
        Sets the api_groups of this V1PolicyRule.
        APIGroups is the name of the APIGroup that contains the resources.  If this field is empty, then both kubernetes and origin API groups are assumed. That means that if an action is requested against one of the enumerated resources in either the kubernetes or the origin API group, the request will be allowed

        :param api_groups: The api_groups of this V1PolicyRule.
        :type: list[str]
        """
        self._api_groups = api_groups

    @property
    def resources(self):
        """
        Gets the resources of this V1PolicyRule.
        Resources is a list of resources this rule applies to.  ResourceAll represents all resources.

        :return: The resources of this V1PolicyRule.
        :rtype: list[str]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """
        Sets the resources of this V1PolicyRule.
        Resources is a list of resources this rule applies to.  ResourceAll represents all resources.

        :param resources: The resources of this V1PolicyRule.
        :type: list[str]
        """
        self._resources = resources

    @property
    def resource_names(self):
        """
        Gets the resource_names of this V1PolicyRule.
        ResourceNames is an optional white list of names that the rule applies to.  An empty set means that everything is allowed.

        :return: The resource_names of this V1PolicyRule.
        :rtype: list[str]
        """
        return self._resource_names

    @resource_names.setter
    def resource_names(self, resource_names):
        """
        Sets the resource_names of this V1PolicyRule.
        ResourceNames is an optional white list of names that the rule applies to.  An empty set means that everything is allowed.

        :param resource_names: The resource_names of this V1PolicyRule.
        :type: list[str]
        """
        self._resource_names = resource_names

    @property
    def non_resource_ur_ls(self):
        """
        Gets the non_resource_ur_ls of this V1PolicyRule.
        NonResourceURLsSlice is a set of partial urls that a user should have access to.  *s are allowed, but only as the full, final step in the path This name is intentionally different than the internal type so that the DefaultConvert works nicely and because the ordering may be different.

        :return: The non_resource_ur_ls of this V1PolicyRule.
        :rtype: list[str]
        """
        return self._non_resource_ur_ls

    @non_resource_ur_ls.setter
    def non_resource_ur_ls(self, non_resource_ur_ls):
        """
        Sets the non_resource_ur_ls of this V1PolicyRule.
        NonResourceURLsSlice is a set of partial urls that a user should have access to.  *s are allowed, but only as the full, final step in the path This name is intentionally different than the internal type so that the DefaultConvert works nicely and because the ordering may be different.

        :param non_resource_ur_ls: The non_resource_ur_ls of this V1PolicyRule.
        :type: list[str]
        """
        self._non_resource_ur_ls = non_resource_ur_ls

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
