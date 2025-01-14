# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class LoginRequest(Model):
    """LoginRequest.

    All required parameters must be populated in order to send to Azure.

    :param data_source: Required. Datasource <span
     class='property-internal'>Required</span>
    :type data_source: str
    :param password: Required. Password <span
     class='property-internal'>Required</span>
    :type password: str
    :param username: Required. Username <span
     class='property-internal'>Required</span>
    :type username: str
    :param partition: OPTIONAL - Partition
     Usually this is the environment, Staging, Pro, Web.
     An empty or NULL partition will result in all partitions being scanned.
    :type partition: str
    """

    _validation = {
        'data_source': {'required': True},
        'password': {'required': True},
        'username': {'required': True},
    }

    _attribute_map = {
        'data_source': {'key': 'dataSource', 'type': 'str'},
        'password': {'key': 'password', 'type': 'str'},
        'username': {'key': 'username', 'type': 'str'},
        'partition': {'key': 'partition', 'type': 'str'},
    }

    def __init__(self, *, data_source: str, password: str, username: str, partition: str=None, **kwargs) -> None:
        super(LoginRequest, self).__init__(**kwargs)
        self.data_source = data_source
        self.password = password
        self.username = username
        self.partition = partition
