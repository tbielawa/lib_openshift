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


class V1BuildPostCommitSpec(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        V1BuildPostCommitSpec - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'command': 'list[str]',
            'args': 'list[str]',
            'script': 'str'
        }

        self.attribute_map = {
            'command': 'command',
            'args': 'args',
            'script': 'script'
        }

        self._command = None
        self._args = None
        self._script = None

    @property
    def command(self):
        """
        Gets the command of this V1BuildPostCommitSpec.
        Command is the command to run. It may not be specified with Script. This might be needed if the image doesn't have `/bin/sh`, or if you do not want to use a shell. In all other cases, using Script might be more convenient.

        :return: The command of this V1BuildPostCommitSpec.
        :rtype: list[str]
        """
        return self._command

    @command.setter
    def command(self, command):
        """
        Sets the command of this V1BuildPostCommitSpec.
        Command is the command to run. It may not be specified with Script. This might be needed if the image doesn't have `/bin/sh`, or if you do not want to use a shell. In all other cases, using Script might be more convenient.

        :param command: The command of this V1BuildPostCommitSpec.
        :type: list[str]
        """
        self._command = command

    @property
    def args(self):
        """
        Gets the args of this V1BuildPostCommitSpec.
        Args is a list of arguments that are provided to either Command, Script or the Docker image's default entrypoint. The arguments are placed immediately after the command to be run.

        :return: The args of this V1BuildPostCommitSpec.
        :rtype: list[str]
        """
        return self._args

    @args.setter
    def args(self, args):
        """
        Sets the args of this V1BuildPostCommitSpec.
        Args is a list of arguments that are provided to either Command, Script or the Docker image's default entrypoint. The arguments are placed immediately after the command to be run.

        :param args: The args of this V1BuildPostCommitSpec.
        :type: list[str]
        """
        self._args = args

    @property
    def script(self):
        """
        Gets the script of this V1BuildPostCommitSpec.
        Script is a shell script to be run with `/bin/sh -ic`. It may not be specified with Command. Use Script when a shell script is appropriate to execute the post build hook, for example for running unit tests with `rake test`. If you need control over the image entrypoint, or if the image does not have `/bin/sh`, use Command and/or Args. The `-i` flag is needed to support CentOS and RHEL images that use Software Collections (SCL), in order to have the appropriate collections enabled in the shell. E.g., in the Ruby image, this is necessary to make `ruby`, `bundle` and other binaries available in the PATH.

        :return: The script of this V1BuildPostCommitSpec.
        :rtype: str
        """
        return self._script

    @script.setter
    def script(self, script):
        """
        Sets the script of this V1BuildPostCommitSpec.
        Script is a shell script to be run with `/bin/sh -ic`. It may not be specified with Command. Use Script when a shell script is appropriate to execute the post build hook, for example for running unit tests with `rake test`. If you need control over the image entrypoint, or if the image does not have `/bin/sh`, use Command and/or Args. The `-i` flag is needed to support CentOS and RHEL images that use Software Collections (SCL), in order to have the appropriate collections enabled in the shell. E.g., in the Ruby image, this is necessary to make `ruby`, `bundle` and other binaries available in the PATH.

        :param script: The script of this V1BuildPostCommitSpec.
        :type: str
        """
        self._script = script

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

