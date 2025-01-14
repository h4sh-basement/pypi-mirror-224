# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MeterDigestSavingsMonthlyResponse(Model):
    """MeterDigestSavingsMonthlyResponse.

    :param meter_id: The meter identifier
    :type meter_id: int
    :param meter_code: The meter code
    :type meter_code: str
    :param meter_info: The meter info
    :type meter_info: str
    :param meter_cap:
    :type meter_cap: ~energycap.sdk.models.MeterCAPResponse
    :param native_use_unit:
    :type native_use_unit: ~energycap.sdk.models.UnitChild
    :param common_use_unit:
    :type common_use_unit: ~energycap.sdk.models.UnitChild
    :param cost_unit:
    :type cost_unit: ~energycap.sdk.models.UnitChild
    :param results: An array of monthly data
    :type results:
     list[~energycap.sdk.models.MeterDigestSavingsMonthlyResponseResults]
    :param updated: The date and time the data was updated
    :type updated: datetime
    """

    _attribute_map = {
        'meter_id': {'key': 'meterId', 'type': 'int'},
        'meter_code': {'key': 'meterCode', 'type': 'str'},
        'meter_info': {'key': 'meterInfo', 'type': 'str'},
        'meter_cap': {'key': 'meterCAP', 'type': 'MeterCAPResponse'},
        'native_use_unit': {'key': 'nativeUseUnit', 'type': 'UnitChild'},
        'common_use_unit': {'key': 'commonUseUnit', 'type': 'UnitChild'},
        'cost_unit': {'key': 'costUnit', 'type': 'UnitChild'},
        'results': {'key': 'results', 'type': '[MeterDigestSavingsMonthlyResponseResults]'},
        'updated': {'key': 'updated', 'type': 'iso-8601'},
    }

    def __init__(self, *, meter_id: int=None, meter_code: str=None, meter_info: str=None, meter_cap=None, native_use_unit=None, common_use_unit=None, cost_unit=None, results=None, updated=None, **kwargs) -> None:
        super(MeterDigestSavingsMonthlyResponse, self).__init__(**kwargs)
        self.meter_id = meter_id
        self.meter_code = meter_code
        self.meter_info = meter_info
        self.meter_cap = meter_cap
        self.native_use_unit = native_use_unit
        self.common_use_unit = common_use_unit
        self.cost_unit = cost_unit
        self.results = results
        self.updated = updated
