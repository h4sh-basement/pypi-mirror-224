# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AccountCreate(Model):
    """AccountCreate.

    All required parameters must be populated in order to send to Azure.

    :param account_code: Required. The account code <span
     class='property-internal'>Required</span> <span
     class='property-internal'>Must be between 0 and 50 characters</span>
    :type account_code: str
    :param account_info: Required. The account info <span
     class='property-internal'>Required</span> <span
     class='property-internal'>Must be between 0 and 50 characters</span>
    :type account_info: str
    :param account_type_id: Required. The identifier for the account type
     <span class='property-internal'>Required</span>
    :type account_type_id: int
    :param cost_center_id: Required. The identifier for the cost center to
     which the account belongs <span class='property-internal'>Topmost
     (CostCenter)</span> <span class='property-internal'>Required</span>
    :type cost_center_id: int
    :param vendor_id: Required. The identifier for the account's vendor <span
     class='property-internal'>Required</span>
    :type vendor_id: int
    :param customer_id: The identifier for the customer the account serves.
     This is normally only set for chargeback accounts
    :type customer_id: int
    :param contact_id: The identifier for the account's contact
    :type contact_id: int
    :param active: Indicates if the account is active or inactive
    :type active: bool
    :param accrual_enabled: Indicates if the account is used with accruals
    :type accrual_enabled: bool
    :param postal_code: The address postal code
     Required when the country is US or CA <span class='property-internal'>Must
     be between 0 and 32 characters</span>
    :type postal_code: str
    :param city: The address city <span class='property-internal'>Must be
     between 0 and 100 characters</span>
    :type city: str
    :param state: The address state <span class='property-internal'>Must be
     between 0 and 100 characters</span>
    :type state: str
    :param country: Required. The address country <span
     class='property-internal'>Required</span> <span
     class='property-internal'>Must be between 0 and 64 characters</span>
    :type country: str
    :param line1: The address first line <span class='property-internal'>Must
     be between 0 and 100 characters</span>
    :type line1: str
    :param line2: The address second line <span class='property-internal'>Must
     be between 0 and 100 characters</span>
    :type line2: str
    :param line3: The address third line <span class='property-internal'>Must
     be between 0 and 100 characters</span>
    :type line3: str
    :param deposit_paid: The date and time the account deposit was paid
    :type deposit_paid: datetime
    :param deposit_return: The date and time the account deposit was returned
    :type deposit_return: datetime
    :param deposit_note: A note related to the account deposit
    :type deposit_note: str
    :param deposit_amount: The account deposit amount
    :type deposit_amount: float
    :param memo: The account memo
    :type memo: str
    :param service_start: The account's service begin date and time
    :type service_start: datetime
    :param service_end: The account's service end date and time
    :type service_end: datetime
    :param meters: An array of identifiers for meters attached to this account
    :type meters: list[int]
    :param general_ledger_id: The identifier for the account's generalLedgerId
    :type general_ledger_id: int
    :param account_description: A description of the account <span
     class='property-internal'>Must be between 0 and 4000 characters</span>
    :type account_description: str
    """

    _validation = {
        'account_code': {'required': True, 'max_length': 50, 'min_length': 0},
        'account_info': {'required': True, 'max_length': 50, 'min_length': 0},
        'account_type_id': {'required': True},
        'cost_center_id': {'required': True},
        'vendor_id': {'required': True},
        'postal_code': {'max_length': 32, 'min_length': 0},
        'city': {'max_length': 100, 'min_length': 0},
        'state': {'max_length': 100, 'min_length': 0},
        'country': {'required': True, 'max_length': 64, 'min_length': 0},
        'line1': {'max_length': 100, 'min_length': 0},
        'line2': {'max_length': 100, 'min_length': 0},
        'line3': {'max_length': 100, 'min_length': 0},
        'account_description': {'max_length': 4000, 'min_length': 0},
    }

    _attribute_map = {
        'account_code': {'key': 'accountCode', 'type': 'str'},
        'account_info': {'key': 'accountInfo', 'type': 'str'},
        'account_type_id': {'key': 'accountTypeId', 'type': 'int'},
        'cost_center_id': {'key': 'costCenterId', 'type': 'int'},
        'vendor_id': {'key': 'vendorId', 'type': 'int'},
        'customer_id': {'key': 'customerId', 'type': 'int'},
        'contact_id': {'key': 'contactId', 'type': 'int'},
        'active': {'key': 'active', 'type': 'bool'},
        'accrual_enabled': {'key': 'accrualEnabled', 'type': 'bool'},
        'postal_code': {'key': 'postalCode', 'type': 'str'},
        'city': {'key': 'city', 'type': 'str'},
        'state': {'key': 'state', 'type': 'str'},
        'country': {'key': 'country', 'type': 'str'},
        'line1': {'key': 'line1', 'type': 'str'},
        'line2': {'key': 'line2', 'type': 'str'},
        'line3': {'key': 'line3', 'type': 'str'},
        'deposit_paid': {'key': 'depositPaid', 'type': 'iso-8601'},
        'deposit_return': {'key': 'depositReturn', 'type': 'iso-8601'},
        'deposit_note': {'key': 'depositNote', 'type': 'str'},
        'deposit_amount': {'key': 'depositAmount', 'type': 'float'},
        'memo': {'key': 'memo', 'type': 'str'},
        'service_start': {'key': 'serviceStart', 'type': 'iso-8601'},
        'service_end': {'key': 'serviceEnd', 'type': 'iso-8601'},
        'meters': {'key': 'meters', 'type': '[int]'},
        'general_ledger_id': {'key': 'generalLedgerId', 'type': 'int'},
        'account_description': {'key': 'accountDescription', 'type': 'str'},
    }

    def __init__(self, *, account_code: str, account_info: str, account_type_id: int, cost_center_id: int, vendor_id: int, country: str, customer_id: int=None, contact_id: int=None, active: bool=None, accrual_enabled: bool=None, postal_code: str=None, city: str=None, state: str=None, line1: str=None, line2: str=None, line3: str=None, deposit_paid=None, deposit_return=None, deposit_note: str=None, deposit_amount: float=None, memo: str=None, service_start=None, service_end=None, meters=None, general_ledger_id: int=None, account_description: str=None, **kwargs) -> None:
        super(AccountCreate, self).__init__(**kwargs)
        self.account_code = account_code
        self.account_info = account_info
        self.account_type_id = account_type_id
        self.cost_center_id = cost_center_id
        self.vendor_id = vendor_id
        self.customer_id = customer_id
        self.contact_id = contact_id
        self.active = active
        self.accrual_enabled = accrual_enabled
        self.postal_code = postal_code
        self.city = city
        self.state = state
        self.country = country
        self.line1 = line1
        self.line2 = line2
        self.line3 = line3
        self.deposit_paid = deposit_paid
        self.deposit_return = deposit_return
        self.deposit_note = deposit_note
        self.deposit_amount = deposit_amount
        self.memo = memo
        self.service_start = service_start
        self.service_end = service_end
        self.meters = meters
        self.general_ledger_id = general_ledger_id
        self.account_description = account_description
