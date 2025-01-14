# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class BillViewMeterChild(Model):
    """BillViewMeterChild.

    :param meter_id: The meter identifier
    :type meter_id: int
    :param meter_code: The meter code
    :type meter_code: str
    :param meter_info: The meter info
    :type meter_info: str
    :param meter_type:
    :type meter_type: ~energycap.sdk.models.MeterTypeChild
    :param commodity:
    :type commodity: ~energycap.sdk.models.CommodityChild
    :param serial_number: The meter's serial number
    :type serial_number: str
    :param rate:
    :type rate: ~energycap.sdk.models.RateChild
    :param place:
    :type place: ~energycap.sdk.models.PlaceChild
    :param general_ledger:
    :type general_ledger: ~energycap.sdk.models.GeneralLedgerChild
    """

    _attribute_map = {
        'meter_id': {'key': 'meterId', 'type': 'int'},
        'meter_code': {'key': 'meterCode', 'type': 'str'},
        'meter_info': {'key': 'meterInfo', 'type': 'str'},
        'meter_type': {'key': 'meterType', 'type': 'MeterTypeChild'},
        'commodity': {'key': 'commodity', 'type': 'CommodityChild'},
        'serial_number': {'key': 'serialNumber', 'type': 'str'},
        'rate': {'key': 'rate', 'type': 'RateChild'},
        'place': {'key': 'place', 'type': 'PlaceChild'},
        'general_ledger': {'key': 'generalLedger', 'type': 'GeneralLedgerChild'},
    }

    def __init__(self, *, meter_id: int=None, meter_code: str=None, meter_info: str=None, meter_type=None, commodity=None, serial_number: str=None, rate=None, place=None, general_ledger=None, **kwargs) -> None:
        super(BillViewMeterChild, self).__init__(**kwargs)
        self.meter_id = meter_id
        self.meter_code = meter_code
        self.meter_info = meter_info
        self.meter_type = meter_type
        self.commodity = commodity
        self.serial_number = serial_number
        self.rate = rate
        self.place = place
        self.general_ledger = general_ledger
