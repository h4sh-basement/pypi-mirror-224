# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class CommodityDigestActualYearlyResponse(Model):
    """CommodityDigestActualYearlyResponse.

    :param global_use_unit:
    :type global_use_unit: ~energycap.sdk.models.UnitChild
    :param cost_unit:
    :type cost_unit: ~energycap.sdk.models.UnitChild
    :param updated: The date and time the data was updated
    :type updated: datetime
    :param results: An array of yearly data
    :type results:
     list[~energycap.sdk.models.CommodityDigestActualYearlyResponseResults]
    :param commodities: An array of yearly data per commodity
    :type commodities:
     list[~energycap.sdk.models.CommodityDigestActualYearlyResponseCommodityData]
    """

    _attribute_map = {
        'global_use_unit': {'key': 'globalUseUnit', 'type': 'UnitChild'},
        'cost_unit': {'key': 'costUnit', 'type': 'UnitChild'},
        'updated': {'key': 'updated', 'type': 'iso-8601'},
        'results': {'key': 'results', 'type': '[CommodityDigestActualYearlyResponseResults]'},
        'commodities': {'key': 'commodities', 'type': '[CommodityDigestActualYearlyResponseCommodityData]'},
    }

    def __init__(self, **kwargs):
        super(CommodityDigestActualYearlyResponse, self).__init__(**kwargs)
        self.global_use_unit = kwargs.get('global_use_unit', None)
        self.cost_unit = kwargs.get('cost_unit', None)
        self.updated = kwargs.get('updated', None)
        self.results = kwargs.get('results', None)
        self.commodities = kwargs.get('commodities', None)
