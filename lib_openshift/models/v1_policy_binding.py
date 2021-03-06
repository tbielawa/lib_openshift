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


class V1PolicyBinding(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        V1PolicyBinding - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'kind': 'str',
            'api_version': 'str',
            'metadata': 'V1ObjectMeta',
            'last_modified': 'str',
            'policy_ref': 'V1ObjectReference',
            'role_bindings': 'list[V1NamedRoleBinding]'
        }

        self.attribute_map = {
            'kind': 'kind',
            'api_version': 'apiVersion',
            'metadata': 'metadata',
            'last_modified': 'lastModified',
            'policy_ref': 'policyRef',
            'role_bindings': 'roleBindings'
        }

        self._kind = None
        self._api_version = None
        self._metadata = None
        self._last_modified = None
        self._policy_ref = None
        self._role_bindings = None

    @property
    def kind(self):
        """
        Gets the kind of this V1PolicyBinding.
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: http://releases.k8s.io/release-1.2/docs/devel/api-conventions.md#types-kinds

        :return: The kind of this V1PolicyBinding.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """
        Sets the kind of this V1PolicyBinding.
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: http://releases.k8s.io/release-1.2/docs/devel/api-conventions.md#types-kinds

        :param kind: The kind of this V1PolicyBinding.
        :type: str
        """
        self._kind = kind

    @property
    def api_version(self):
        """
        Gets the api_version of this V1PolicyBinding.
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: http://releases.k8s.io/release-1.2/docs/devel/api-conventions.md#resources

        :return: The api_version of this V1PolicyBinding.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """
        Sets the api_version of this V1PolicyBinding.
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: http://releases.k8s.io/release-1.2/docs/devel/api-conventions.md#resources

        :param api_version: The api_version of this V1PolicyBinding.
        :type: str
        """
        self._api_version = api_version

    @property
    def metadata(self):
        """
        Gets the metadata of this V1PolicyBinding.
        Standard object's metadata.

        :return: The metadata of this V1PolicyBinding.
        :rtype: V1ObjectMeta
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this V1PolicyBinding.
        Standard object's metadata.

        :param metadata: The metadata of this V1PolicyBinding.
        :type: V1ObjectMeta
        """
        self._metadata = metadata

    @property
    def last_modified(self):
        """
        Gets the last_modified of this V1PolicyBinding.
        LastModified is the last time that any part of the PolicyBinding was created, updated, or deleted

        :return: The last_modified of this V1PolicyBinding.
        :rtype: str
        """
        return self._last_modified

    @last_modified.setter
    def last_modified(self, last_modified):
        """
        Sets the last_modified of this V1PolicyBinding.
        LastModified is the last time that any part of the PolicyBinding was created, updated, or deleted

        :param last_modified: The last_modified of this V1PolicyBinding.
        :type: str
        """
        self._last_modified = last_modified

    @property
    def policy_ref(self):
        """
        Gets the policy_ref of this V1PolicyBinding.
        PolicyRef is a reference to the Policy that contains all the Roles that this PolicyBinding's RoleBindings may reference

        :return: The policy_ref of this V1PolicyBinding.
        :rtype: V1ObjectReference
        """
        return self._policy_ref

    @policy_ref.setter
    def policy_ref(self, policy_ref):
        """
        Sets the policy_ref of this V1PolicyBinding.
        PolicyRef is a reference to the Policy that contains all the Roles that this PolicyBinding's RoleBindings may reference

        :param policy_ref: The policy_ref of this V1PolicyBinding.
        :type: V1ObjectReference
        """
        self._policy_ref = policy_ref

    @property
    def role_bindings(self):
        """
        Gets the role_bindings of this V1PolicyBinding.
        RoleBindings holds all the RoleBindings held by this PolicyBinding, mapped by RoleBinding.Name

        :return: The role_bindings of this V1PolicyBinding.
        :rtype: list[V1NamedRoleBinding]
        """
        return self._role_bindings

    @role_bindings.setter
    def role_bindings(self, role_bindings):
        """
        Sets the role_bindings of this V1PolicyBinding.
        RoleBindings holds all the RoleBindings held by this PolicyBinding, mapped by RoleBinding.Name

        :param role_bindings: The role_bindings of this V1PolicyBinding.
        :type: list[V1NamedRoleBinding]
        """
        self._role_bindings = role_bindings

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

