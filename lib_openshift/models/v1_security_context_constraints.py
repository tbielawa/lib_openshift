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


class V1SecurityContextConstraints(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        V1SecurityContextConstraints - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'kind': 'str',
            'api_version': 'str',
            'metadata': 'V1ObjectMeta',
            'priority': 'int',
            'allow_privileged_container': 'bool',
            'default_add_capabilities': 'list[V1Capability]',
            'required_drop_capabilities': 'list[V1Capability]',
            'allowed_capabilities': 'list[V1Capability]',
            'allow_host_dir_volume_plugin': 'bool',
            'volumes': 'list[V1FSType]',
            'allow_host_network': 'bool',
            'allow_host_ports': 'bool',
            'allow_host_pid': 'bool',
            'allow_host_ipc': 'bool',
            'se_linux_context': 'V1SELinuxContextStrategyOptions',
            'run_as_user': 'V1RunAsUserStrategyOptions',
            'supplemental_groups': 'V1SupplementalGroupsStrategyOptions',
            'fs_group': 'V1FSGroupStrategyOptions',
            'read_only_root_filesystem': 'bool',
            'users': 'list[str]',
            'groups': 'list[str]'
        }

        self.attribute_map = {
            'kind': 'kind',
            'api_version': 'apiVersion',
            'metadata': 'metadata',
            'priority': 'priority',
            'allow_privileged_container': 'allowPrivilegedContainer',
            'default_add_capabilities': 'defaultAddCapabilities',
            'required_drop_capabilities': 'requiredDropCapabilities',
            'allowed_capabilities': 'allowedCapabilities',
            'allow_host_dir_volume_plugin': 'allowHostDirVolumePlugin',
            'volumes': 'volumes',
            'allow_host_network': 'allowHostNetwork',
            'allow_host_ports': 'allowHostPorts',
            'allow_host_pid': 'allowHostPID',
            'allow_host_ipc': 'allowHostIPC',
            'se_linux_context': 'seLinuxContext',
            'run_as_user': 'runAsUser',
            'supplemental_groups': 'supplementalGroups',
            'fs_group': 'fsGroup',
            'read_only_root_filesystem': 'readOnlyRootFilesystem',
            'users': 'users',
            'groups': 'groups'
        }

        self._kind = None
        self._api_version = None
        self._metadata = None
        self._priority = None
        self._allow_privileged_container = None
        self._default_add_capabilities = None
        self._required_drop_capabilities = None
        self._allowed_capabilities = None
        self._allow_host_dir_volume_plugin = None
        self._volumes = None
        self._allow_host_network = None
        self._allow_host_ports = None
        self._allow_host_pid = None
        self._allow_host_ipc = None
        self._se_linux_context = None
        self._run_as_user = None
        self._supplemental_groups = None
        self._fs_group = None
        self._read_only_root_filesystem = None
        self._users = None
        self._groups = None

    @property
    def kind(self):
        """
        Gets the kind of this V1SecurityContextConstraints.
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: http://releases.k8s.io/release-1.2/docs/devel/api-conventions.md#types-kinds

        :return: The kind of this V1SecurityContextConstraints.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """
        Sets the kind of this V1SecurityContextConstraints.
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: http://releases.k8s.io/release-1.2/docs/devel/api-conventions.md#types-kinds

        :param kind: The kind of this V1SecurityContextConstraints.
        :type: str
        """
        self._kind = kind

    @property
    def api_version(self):
        """
        Gets the api_version of this V1SecurityContextConstraints.
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: http://releases.k8s.io/release-1.2/docs/devel/api-conventions.md#resources

        :return: The api_version of this V1SecurityContextConstraints.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """
        Sets the api_version of this V1SecurityContextConstraints.
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: http://releases.k8s.io/release-1.2/docs/devel/api-conventions.md#resources

        :param api_version: The api_version of this V1SecurityContextConstraints.
        :type: str
        """
        self._api_version = api_version

    @property
    def metadata(self):
        """
        Gets the metadata of this V1SecurityContextConstraints.


        :return: The metadata of this V1SecurityContextConstraints.
        :rtype: V1ObjectMeta
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this V1SecurityContextConstraints.


        :param metadata: The metadata of this V1SecurityContextConstraints.
        :type: V1ObjectMeta
        """
        self._metadata = metadata

    @property
    def priority(self):
        """
        Gets the priority of this V1SecurityContextConstraints.
        Priority influences the sort order of SCCs when evaluating which SCCs to try first for a given pod request based on access in the Users and Groups fields.  The higher the int, the higher priority.  If scores for multiple SCCs are equal they will be sorted by name.

        :return: The priority of this V1SecurityContextConstraints.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """
        Sets the priority of this V1SecurityContextConstraints.
        Priority influences the sort order of SCCs when evaluating which SCCs to try first for a given pod request based on access in the Users and Groups fields.  The higher the int, the higher priority.  If scores for multiple SCCs are equal they will be sorted by name.

        :param priority: The priority of this V1SecurityContextConstraints.
        :type: int
        """
        self._priority = priority

    @property
    def allow_privileged_container(self):
        """
        Gets the allow_privileged_container of this V1SecurityContextConstraints.
        AllowPrivilegedContainer determines if a container can request to be run as privileged.

        :return: The allow_privileged_container of this V1SecurityContextConstraints.
        :rtype: bool
        """
        return self._allow_privileged_container

    @allow_privileged_container.setter
    def allow_privileged_container(self, allow_privileged_container):
        """
        Sets the allow_privileged_container of this V1SecurityContextConstraints.
        AllowPrivilegedContainer determines if a container can request to be run as privileged.

        :param allow_privileged_container: The allow_privileged_container of this V1SecurityContextConstraints.
        :type: bool
        """
        self._allow_privileged_container = allow_privileged_container

    @property
    def default_add_capabilities(self):
        """
        Gets the default_add_capabilities of this V1SecurityContextConstraints.
        DefaultAddCapabilities is the default set of capabilities that will be added to the container unless the pod spec specifically drops the capability.  You may not list a capabiility in both DefaultAddCapabilities and RequiredDropCapabilities.

        :return: The default_add_capabilities of this V1SecurityContextConstraints.
        :rtype: list[V1Capability]
        """
        return self._default_add_capabilities

    @default_add_capabilities.setter
    def default_add_capabilities(self, default_add_capabilities):
        """
        Sets the default_add_capabilities of this V1SecurityContextConstraints.
        DefaultAddCapabilities is the default set of capabilities that will be added to the container unless the pod spec specifically drops the capability.  You may not list a capabiility in both DefaultAddCapabilities and RequiredDropCapabilities.

        :param default_add_capabilities: The default_add_capabilities of this V1SecurityContextConstraints.
        :type: list[V1Capability]
        """
        self._default_add_capabilities = default_add_capabilities

    @property
    def required_drop_capabilities(self):
        """
        Gets the required_drop_capabilities of this V1SecurityContextConstraints.
        RequiredDropCapabilities are the capabilities that will be dropped from the container.  These are required to be dropped and cannot be added.

        :return: The required_drop_capabilities of this V1SecurityContextConstraints.
        :rtype: list[V1Capability]
        """
        return self._required_drop_capabilities

    @required_drop_capabilities.setter
    def required_drop_capabilities(self, required_drop_capabilities):
        """
        Sets the required_drop_capabilities of this V1SecurityContextConstraints.
        RequiredDropCapabilities are the capabilities that will be dropped from the container.  These are required to be dropped and cannot be added.

        :param required_drop_capabilities: The required_drop_capabilities of this V1SecurityContextConstraints.
        :type: list[V1Capability]
        """
        self._required_drop_capabilities = required_drop_capabilities

    @property
    def allowed_capabilities(self):
        """
        Gets the allowed_capabilities of this V1SecurityContextConstraints.
        AllowedCapabilities is a list of capabilities that can be requested to add to the container. Capabilities in this field maybe added at the pod author's discretion. You must not list a capability in both AllowedCapabilities and RequiredDropCapabilities.

        :return: The allowed_capabilities of this V1SecurityContextConstraints.
        :rtype: list[V1Capability]
        """
        return self._allowed_capabilities

    @allowed_capabilities.setter
    def allowed_capabilities(self, allowed_capabilities):
        """
        Sets the allowed_capabilities of this V1SecurityContextConstraints.
        AllowedCapabilities is a list of capabilities that can be requested to add to the container. Capabilities in this field maybe added at the pod author's discretion. You must not list a capability in both AllowedCapabilities and RequiredDropCapabilities.

        :param allowed_capabilities: The allowed_capabilities of this V1SecurityContextConstraints.
        :type: list[V1Capability]
        """
        self._allowed_capabilities = allowed_capabilities

    @property
    def allow_host_dir_volume_plugin(self):
        """
        Gets the allow_host_dir_volume_plugin of this V1SecurityContextConstraints.
        AllowHostDirVolumePlugin determines if the policy allow containers to use the HostDir volume plugin

        :return: The allow_host_dir_volume_plugin of this V1SecurityContextConstraints.
        :rtype: bool
        """
        return self._allow_host_dir_volume_plugin

    @allow_host_dir_volume_plugin.setter
    def allow_host_dir_volume_plugin(self, allow_host_dir_volume_plugin):
        """
        Sets the allow_host_dir_volume_plugin of this V1SecurityContextConstraints.
        AllowHostDirVolumePlugin determines if the policy allow containers to use the HostDir volume plugin

        :param allow_host_dir_volume_plugin: The allow_host_dir_volume_plugin of this V1SecurityContextConstraints.
        :type: bool
        """
        self._allow_host_dir_volume_plugin = allow_host_dir_volume_plugin

    @property
    def volumes(self):
        """
        Gets the volumes of this V1SecurityContextConstraints.


        :return: The volumes of this V1SecurityContextConstraints.
        :rtype: list[V1FSType]
        """
        return self._volumes

    @volumes.setter
    def volumes(self, volumes):
        """
        Sets the volumes of this V1SecurityContextConstraints.


        :param volumes: The volumes of this V1SecurityContextConstraints.
        :type: list[V1FSType]
        """
        self._volumes = volumes

    @property
    def allow_host_network(self):
        """
        Gets the allow_host_network of this V1SecurityContextConstraints.
        AllowHostNetwork determines if the policy allows the use of HostNetwork in the pod spec.

        :return: The allow_host_network of this V1SecurityContextConstraints.
        :rtype: bool
        """
        return self._allow_host_network

    @allow_host_network.setter
    def allow_host_network(self, allow_host_network):
        """
        Sets the allow_host_network of this V1SecurityContextConstraints.
        AllowHostNetwork determines if the policy allows the use of HostNetwork in the pod spec.

        :param allow_host_network: The allow_host_network of this V1SecurityContextConstraints.
        :type: bool
        """
        self._allow_host_network = allow_host_network

    @property
    def allow_host_ports(self):
        """
        Gets the allow_host_ports of this V1SecurityContextConstraints.
        AllowHostPorts determines if the policy allows host ports in the containers.

        :return: The allow_host_ports of this V1SecurityContextConstraints.
        :rtype: bool
        """
        return self._allow_host_ports

    @allow_host_ports.setter
    def allow_host_ports(self, allow_host_ports):
        """
        Sets the allow_host_ports of this V1SecurityContextConstraints.
        AllowHostPorts determines if the policy allows host ports in the containers.

        :param allow_host_ports: The allow_host_ports of this V1SecurityContextConstraints.
        :type: bool
        """
        self._allow_host_ports = allow_host_ports

    @property
    def allow_host_pid(self):
        """
        Gets the allow_host_pid of this V1SecurityContextConstraints.
        AllowHostPID determines if the policy allows host pid in the containers.

        :return: The allow_host_pid of this V1SecurityContextConstraints.
        :rtype: bool
        """
        return self._allow_host_pid

    @allow_host_pid.setter
    def allow_host_pid(self, allow_host_pid):
        """
        Sets the allow_host_pid of this V1SecurityContextConstraints.
        AllowHostPID determines if the policy allows host pid in the containers.

        :param allow_host_pid: The allow_host_pid of this V1SecurityContextConstraints.
        :type: bool
        """
        self._allow_host_pid = allow_host_pid

    @property
    def allow_host_ipc(self):
        """
        Gets the allow_host_ipc of this V1SecurityContextConstraints.
        AllowHostIPC determines if the policy allows host ipc in the containers.

        :return: The allow_host_ipc of this V1SecurityContextConstraints.
        :rtype: bool
        """
        return self._allow_host_ipc

    @allow_host_ipc.setter
    def allow_host_ipc(self, allow_host_ipc):
        """
        Sets the allow_host_ipc of this V1SecurityContextConstraints.
        AllowHostIPC determines if the policy allows host ipc in the containers.

        :param allow_host_ipc: The allow_host_ipc of this V1SecurityContextConstraints.
        :type: bool
        """
        self._allow_host_ipc = allow_host_ipc

    @property
    def se_linux_context(self):
        """
        Gets the se_linux_context of this V1SecurityContextConstraints.
        SELinuxContext is the strategy that will dictate what labels will be set in the SecurityContext.

        :return: The se_linux_context of this V1SecurityContextConstraints.
        :rtype: V1SELinuxContextStrategyOptions
        """
        return self._se_linux_context

    @se_linux_context.setter
    def se_linux_context(self, se_linux_context):
        """
        Sets the se_linux_context of this V1SecurityContextConstraints.
        SELinuxContext is the strategy that will dictate what labels will be set in the SecurityContext.

        :param se_linux_context: The se_linux_context of this V1SecurityContextConstraints.
        :type: V1SELinuxContextStrategyOptions
        """
        self._se_linux_context = se_linux_context

    @property
    def run_as_user(self):
        """
        Gets the run_as_user of this V1SecurityContextConstraints.
        RunAsUser is the strategy that will dictate what RunAsUser is used in the SecurityContext.

        :return: The run_as_user of this V1SecurityContextConstraints.
        :rtype: V1RunAsUserStrategyOptions
        """
        return self._run_as_user

    @run_as_user.setter
    def run_as_user(self, run_as_user):
        """
        Sets the run_as_user of this V1SecurityContextConstraints.
        RunAsUser is the strategy that will dictate what RunAsUser is used in the SecurityContext.

        :param run_as_user: The run_as_user of this V1SecurityContextConstraints.
        :type: V1RunAsUserStrategyOptions
        """
        self._run_as_user = run_as_user

    @property
    def supplemental_groups(self):
        """
        Gets the supplemental_groups of this V1SecurityContextConstraints.
        SupplementalGroups is the strategy that will dictate what supplemental groups are used by the SecurityContext.

        :return: The supplemental_groups of this V1SecurityContextConstraints.
        :rtype: V1SupplementalGroupsStrategyOptions
        """
        return self._supplemental_groups

    @supplemental_groups.setter
    def supplemental_groups(self, supplemental_groups):
        """
        Sets the supplemental_groups of this V1SecurityContextConstraints.
        SupplementalGroups is the strategy that will dictate what supplemental groups are used by the SecurityContext.

        :param supplemental_groups: The supplemental_groups of this V1SecurityContextConstraints.
        :type: V1SupplementalGroupsStrategyOptions
        """
        self._supplemental_groups = supplemental_groups

    @property
    def fs_group(self):
        """
        Gets the fs_group of this V1SecurityContextConstraints.
        FSGroup is the strategy that will dictate what fs group is used by the SecurityContext.

        :return: The fs_group of this V1SecurityContextConstraints.
        :rtype: V1FSGroupStrategyOptions
        """
        return self._fs_group

    @fs_group.setter
    def fs_group(self, fs_group):
        """
        Sets the fs_group of this V1SecurityContextConstraints.
        FSGroup is the strategy that will dictate what fs group is used by the SecurityContext.

        :param fs_group: The fs_group of this V1SecurityContextConstraints.
        :type: V1FSGroupStrategyOptions
        """
        self._fs_group = fs_group

    @property
    def read_only_root_filesystem(self):
        """
        Gets the read_only_root_filesystem of this V1SecurityContextConstraints.
        ReadOnlyRootFilesystem when set to true will force containers to run with a read only root file system.  If the container specifically requests to run with a non-read only root file system the SCC should deny the pod. If set to false the container may run with a read only root file system if it wishes but it will not be forced to.

        :return: The read_only_root_filesystem of this V1SecurityContextConstraints.
        :rtype: bool
        """
        return self._read_only_root_filesystem

    @read_only_root_filesystem.setter
    def read_only_root_filesystem(self, read_only_root_filesystem):
        """
        Sets the read_only_root_filesystem of this V1SecurityContextConstraints.
        ReadOnlyRootFilesystem when set to true will force containers to run with a read only root file system.  If the container specifically requests to run with a non-read only root file system the SCC should deny the pod. If set to false the container may run with a read only root file system if it wishes but it will not be forced to.

        :param read_only_root_filesystem: The read_only_root_filesystem of this V1SecurityContextConstraints.
        :type: bool
        """
        self._read_only_root_filesystem = read_only_root_filesystem

    @property
    def users(self):
        """
        Gets the users of this V1SecurityContextConstraints.
        The users who have permissions to use this security context constraints

        :return: The users of this V1SecurityContextConstraints.
        :rtype: list[str]
        """
        return self._users

    @users.setter
    def users(self, users):
        """
        Sets the users of this V1SecurityContextConstraints.
        The users who have permissions to use this security context constraints

        :param users: The users of this V1SecurityContextConstraints.
        :type: list[str]
        """
        self._users = users

    @property
    def groups(self):
        """
        Gets the groups of this V1SecurityContextConstraints.
        The groups that have permission to use this security context constraints

        :return: The groups of this V1SecurityContextConstraints.
        :rtype: list[str]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """
        Sets the groups of this V1SecurityContextConstraints.
        The groups that have permission to use this security context constraints

        :param groups: The groups of this V1SecurityContextConstraints.
        :type: list[str]
        """
        self._groups = groups

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

