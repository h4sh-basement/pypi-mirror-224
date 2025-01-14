# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MeterGroupDigestDemandRankingResponse(Model):
    """MeterGroupDigestDemandRankingResponse.

    :param high_cost:
    :type high_cost: float
    :param low_cost:
    :type low_cost: float
    :param average_cost:
    :type average_cost: float
    :param median_cost:
    :type median_cost: float
    :param high_value:
    :type high_value: float
    :param low_value:
    :type low_value: float
    :param average_value:
    :type average_value: float
    :param median_value:
    :type median_value: float
    :param cost_unit:
    :type cost_unit: ~energycap.sdk.models.UnitChild
    :param benchmark_unit:
    :type benchmark_unit: str
    :param benchmark_value_unit:
    :type benchmark_value_unit: str
    :param benchmark_factor_unit:
    :type benchmark_factor_unit: str
    :param results:
    :type results:
     list[~energycap.sdk.models.MeterGroupDigestDemandRankingChild]
    :param meter_group_id:
    :type meter_group_id: int
    :param meter_group_code:
    :type meter_group_code: str
    :param meter_group_info:
    :type meter_group_info: str
    :param meter_group_display:
    :type meter_group_display: str
    :param updated: The date and time the data was updated
    :type updated: datetime
    """

    _attribute_map = {
        'high_cost': {'key': 'highCost', 'type': 'float'},
        'low_cost': {'key': 'lowCost', 'type': 'float'},
        'average_cost': {'key': 'averageCost', 'type': 'float'},
        'median_cost': {'key': 'medianCost', 'type': 'float'},
        'high_value': {'key': 'highValue', 'type': 'float'},
        'low_value': {'key': 'lowValue', 'type': 'float'},
        'average_value': {'key': 'averageValue', 'type': 'float'},
        'median_value': {'key': 'medianValue', 'type': 'float'},
        'cost_unit': {'key': 'costUnit', 'type': 'UnitChild'},
        'benchmark_unit': {'key': 'benchmarkUnit', 'type': 'str'},
        'benchmark_value_unit': {'key': 'benchmarkValueUnit', 'type': 'str'},
        'benchmark_factor_unit': {'key': 'benchmarkFactorUnit', 'type': 'str'},
        'results': {'key': 'results', 'type': '[MeterGroupDigestDemandRankingChild]'},
        'meter_group_id': {'key': 'meterGroupId', 'type': 'int'},
        'meter_group_code': {'key': 'meterGroupCode', 'type': 'str'},
        'meter_group_info': {'key': 'meterGroupInfo', 'type': 'str'},
        'meter_group_display': {'key': 'meterGroupDisplay', 'type': 'str'},
        'updated': {'key': 'updated', 'type': 'iso-8601'},
    }

    def __init__(self, *, high_cost: float=None, low_cost: float=None, average_cost: float=None, median_cost: float=None, high_value: float=None, low_value: float=None, average_value: float=None, median_value: float=None, cost_unit=None, benchmark_unit: str=None, benchmark_value_unit: str=None, benchmark_factor_unit: str=None, results=None, meter_group_id: int=None, meter_group_code: str=None, meter_group_info: str=None, meter_group_display: str=None, updated=None, **kwargs) -> None:
        super(MeterGroupDigestDemandRankingResponse, self).__init__(**kwargs)
        self.high_cost = high_cost
        self.low_cost = low_cost
        self.average_cost = average_cost
        self.median_cost = median_cost
        self.high_value = high_value
        self.low_value = low_value
        self.average_value = average_value
        self.median_value = median_value
        self.cost_unit = cost_unit
        self.benchmark_unit = benchmark_unit
        self.benchmark_value_unit = benchmark_value_unit
        self.benchmark_factor_unit = benchmark_factor_unit
        self.results = results
        self.meter_group_id = meter_group_id
        self.meter_group_code = meter_group_code
        self.meter_group_info = meter_group_info
        self.meter_group_display = meter_group_display
        self.updated = updated
