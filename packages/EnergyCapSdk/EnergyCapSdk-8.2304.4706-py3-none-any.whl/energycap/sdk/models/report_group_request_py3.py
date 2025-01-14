# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ReportGroupRequest(Model):
    """ReportGroupRequest.

    :param report_group_code:
    :type report_group_code: str
    :param report_group_info:
    :type report_group_info: str
    :param report_ids:
    :type report_ids: list[int]
    """

    _attribute_map = {
        'report_group_code': {'key': 'reportGroupCode', 'type': 'str'},
        'report_group_info': {'key': 'reportGroupInfo', 'type': 'str'},
        'report_ids': {'key': 'reportIds', 'type': '[int]'},
    }

    def __init__(self, *, report_group_code: str=None, report_group_info: str=None, report_ids=None, **kwargs) -> None:
        super(ReportGroupRequest, self).__init__(**kwargs)
        self.report_group_code = report_group_code
        self.report_group_info = report_group_info
        self.report_ids = report_ids
