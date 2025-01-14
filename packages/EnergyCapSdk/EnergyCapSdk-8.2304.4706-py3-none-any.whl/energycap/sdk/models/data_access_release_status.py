# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class DataAccessReleaseStatus(Model):
    """DataAccessReleaseStatus.

    :param data_access_release_status_id: Id of the Data Access Release Status
     Possible values are:
     1 - Not Applicable
     2 - Required
     3 - Pending
     4 - Released
     5 - Declined
    :type data_access_release_status_id: int
    :param data_access_release_status_info: Data Access Release Status
     Information
     Possible values are:
     Not Applicable
     Required
     Pending
     Released
     Declined
    :type data_access_release_status_info: str
    """

    _attribute_map = {
        'data_access_release_status_id': {'key': 'dataAccessReleaseStatusId', 'type': 'int'},
        'data_access_release_status_info': {'key': 'dataAccessReleaseStatusInfo', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(DataAccessReleaseStatus, self).__init__(**kwargs)
        self.data_access_release_status_id = kwargs.get('data_access_release_status_id', None)
        self.data_access_release_status_info = kwargs.get('data_access_release_status_info', None)
