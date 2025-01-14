# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MeterGroupDigestDemandRankingChild(Model):
    """MeterGroupDigestDemandRankingChild.

    :param cost:
    :type cost: float
    :param value:
    :type value: float
    :param meter_id:
    :type meter_id: int
    :param meter_code:
    :type meter_code: str
    :param meter_info:
    :type meter_info: str
    :param meter_display:
    :type meter_display: str
    :param commodity:
    :type commodity: ~energycap.sdk.models.CommodityChild
    :param include_in_charts:
    :type include_in_charts: bool
    :param active: Indicates whether the Meter is Active
    :type active: bool
    :param is_calculated_meter: Indicates whether the Meter is a calculated
     meter
    :type is_calculated_meter: bool
    :param is_split_parent_meter: Indicates whether the Meter is a parent of a
     split
    :type is_split_parent_meter: bool
    :param is_split_child_meter: Indicates whether the Meter is a child of a
     split
    :type is_split_child_meter: bool
    """

    _attribute_map = {
        'cost': {'key': 'cost', 'type': 'float'},
        'value': {'key': 'value', 'type': 'float'},
        'meter_id': {'key': 'meterId', 'type': 'int'},
        'meter_code': {'key': 'meterCode', 'type': 'str'},
        'meter_info': {'key': 'meterInfo', 'type': 'str'},
        'meter_display': {'key': 'meterDisplay', 'type': 'str'},
        'commodity': {'key': 'commodity', 'type': 'CommodityChild'},
        'include_in_charts': {'key': 'includeInCharts', 'type': 'bool'},
        'active': {'key': 'active', 'type': 'bool'},
        'is_calculated_meter': {'key': 'isCalculatedMeter', 'type': 'bool'},
        'is_split_parent_meter': {'key': 'isSplitParentMeter', 'type': 'bool'},
        'is_split_child_meter': {'key': 'isSplitChildMeter', 'type': 'bool'},
    }

    def __init__(self, *, cost: float=None, value: float=None, meter_id: int=None, meter_code: str=None, meter_info: str=None, meter_display: str=None, commodity=None, include_in_charts: bool=None, active: bool=None, is_calculated_meter: bool=None, is_split_parent_meter: bool=None, is_split_child_meter: bool=None, **kwargs) -> None:
        super(MeterGroupDigestDemandRankingChild, self).__init__(**kwargs)
        self.cost = cost
        self.value = value
        self.meter_id = meter_id
        self.meter_code = meter_code
        self.meter_info = meter_info
        self.meter_display = meter_display
        self.commodity = commodity
        self.include_in_charts = include_in_charts
        self.active = active
        self.is_calculated_meter = is_calculated_meter
        self.is_split_parent_meter = is_split_parent_meter
        self.is_split_child_meter = is_split_child_meter
