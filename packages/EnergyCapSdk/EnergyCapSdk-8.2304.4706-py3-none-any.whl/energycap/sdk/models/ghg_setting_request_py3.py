# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class GHGSettingRequest(Model):
    """GHGSettingRequest.

    All required parameters must be populated in order to send to Azure.

    :param factor_id: Required. The GHG factor to set <span
     class='property-internal'>Required</span>
    :type factor_id: int
    :param scope_category_id: Required. The GHG Scope Category to set <span
     class='property-internal'>Required</span>
    :type scope_category_id: int
    """

    _validation = {
        'factor_id': {'required': True},
        'scope_category_id': {'required': True},
    }

    _attribute_map = {
        'factor_id': {'key': 'factorId', 'type': 'int'},
        'scope_category_id': {'key': 'scopeCategoryId', 'type': 'int'},
    }

    def __init__(self, *, factor_id: int, scope_category_id: int, **kwargs) -> None:
        super(GHGSettingRequest, self).__init__(**kwargs)
        self.factor_id = factor_id
        self.scope_category_id = scope_category_id
