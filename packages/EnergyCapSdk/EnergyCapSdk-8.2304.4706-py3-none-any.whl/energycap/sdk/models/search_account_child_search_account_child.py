# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class SearchAccountChildSearchAccountChild(Model):
    """SearchAccountChildSearchAccountChild.

    All required parameters must be populated in order to send to Azure.

    :param account_id: The Account identifier
    :type account_id: int
    :param account_code: Required. The Account code <span
     class='property-internal'>Required</span> <span
     class='property-internal'>Must be between 0 and 32 characters</span>
    :type account_code: str
    :param account_info: Required. The Account info <span
     class='property-internal'>Required</span> <span
     class='property-internal'>Must be between 0 and 50 characters</span>
    :type account_info: str
    :param active: Indicates whether the Account is active or inactive
    :type active: bool
    :param account_type:
    :type account_type: ~energycap.sdk.models.AccountTypeChild
    :param vendor:
    :type vendor: ~energycap.sdk.models.VendorChild
    :param address:
    :type address: ~energycap.sdk.models.AddressChild
    :param parent_path: The collection of cost centers representing the path
     to its parent
    :type parent_path: list[~energycap.sdk.models.CostCenterChild]
    :param has_calculated_meter: Indicates whether the Account has a child
     calculated meter
    :type has_calculated_meter: bool
    :param has_split_parent_meter: Indicates whether the Account is a
     recipient of a split
    :type has_split_parent_meter: bool
    :param has_split_child_meter: Indicates whether the Account has a child
     split meter
    :type has_split_child_meter: bool
    :param previous_account_code: The previous Account code
    :type previous_account_code: str
    """

    _validation = {
        'account_code': {'required': True, 'max_length': 32, 'min_length': 0},
        'account_info': {'required': True, 'max_length': 50, 'min_length': 0},
    }

    _attribute_map = {
        'account_id': {'key': 'accountId', 'type': 'int'},
        'account_code': {'key': 'accountCode', 'type': 'str'},
        'account_info': {'key': 'accountInfo', 'type': 'str'},
        'active': {'key': 'active', 'type': 'bool'},
        'account_type': {'key': 'accountType', 'type': 'AccountTypeChild'},
        'vendor': {'key': 'vendor', 'type': 'VendorChild'},
        'address': {'key': 'address', 'type': 'AddressChild'},
        'parent_path': {'key': 'parentPath', 'type': '[CostCenterChild]'},
        'has_calculated_meter': {'key': 'hasCalculatedMeter', 'type': 'bool'},
        'has_split_parent_meter': {'key': 'hasSplitParentMeter', 'type': 'bool'},
        'has_split_child_meter': {'key': 'hasSplitChildMeter', 'type': 'bool'},
        'previous_account_code': {'key': 'previousAccountCode', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(SearchAccountChildSearchAccountChild, self).__init__(**kwargs)
        self.account_id = kwargs.get('account_id', None)
        self.account_code = kwargs.get('account_code', None)
        self.account_info = kwargs.get('account_info', None)
        self.active = kwargs.get('active', None)
        self.account_type = kwargs.get('account_type', None)
        self.vendor = kwargs.get('vendor', None)
        self.address = kwargs.get('address', None)
        self.parent_path = kwargs.get('parent_path', None)
        self.has_calculated_meter = kwargs.get('has_calculated_meter', None)
        self.has_split_parent_meter = kwargs.get('has_split_parent_meter', None)
        self.has_split_child_meter = kwargs.get('has_split_child_meter', None)
        self.previous_account_code = kwargs.get('previous_account_code', None)
