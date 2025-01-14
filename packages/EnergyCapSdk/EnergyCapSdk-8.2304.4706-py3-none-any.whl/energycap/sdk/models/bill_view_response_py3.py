# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class BillViewResponse(Model):
    """BillViewResponse.

    :param bill_id: The bill identifier
    :type bill_id: int
    :param void: Indicates if the bill has been voided
    :type void: bool
    :param from_vendor: Indicates if the bill is from a vendor
    :type from_vendor: bool
    :param creation_method: The method used to create the bill Automatic,
     Manual, Estimated, Simulated, Accrual, or Adjustment
    :type creation_method: str
    :param accrual: Indicates if the bill is an accrual
    :type accrual: bool
    :param accrual_reversed: Indicates if the bill is a reversed accrual
    :type accrual_reversed: bool
    :param batch:
    :type batch: ~energycap.sdk.models.BatchChild
    :param batch_end_date: The date the batch was closed
    :type batch_end_date: datetime
    :param hide_batch_code: Do y'all need to have a batch code?
    :type hide_batch_code: bool
    :param created_by:
    :type created_by: ~energycap.sdk.models.UserChild
    :param created_date: The date and time the bill was created
    :type created_date: datetime
    :param modified_by:
    :type modified_by: ~energycap.sdk.models.UserChild
    :param modified_date: The date and time of the most recent modification
    :type modified_date: datetime
    :param approved: Indicates if the bill has been approved
    :type approved: bool
    :param approve_date: The date and time the bill was approved
    :type approve_date: datetime
    :param approved_by:
    :type approved_by: ~energycap.sdk.models.UserChild
    :param has_been_split: Indicates if the bill has been split
    :type has_been_split: bool
    :param was_split_date: The date and time the bill was split
    :type was_split_date: datetime
    :param export_hold: Indicates if the bill is being withheld from bill
     exports
    :type export_hold: bool
    :param ap_exported: Indicates if the bill has been ap exported
    :type ap_exported: bool
    :param ap_export_date: The date and time the bill was ap exported
    :type ap_export_date: datetime
    :param ap_exported_by:
    :type ap_exported_by: ~energycap.sdk.models.UserChild
    :param gl_exported: Indicates if the bill has been gl exported
    :type gl_exported: bool
    :param gl_exported_by:
    :type gl_exported_by: ~energycap.sdk.models.UserChild
    :param gl_export_date: The date and time the bill was exported to gl
    :type gl_export_date: datetime
    :param check_number: The number of the check that the bill was paid with
    :type check_number: str
    :param check_date: The date and time of the check
    :type check_date: datetime
    :param pay_status: The payment status of the bill
    :type pay_status: str
    :param cleared_date: The date and time that the check cleared
    :type cleared_date: datetime
    :param account:
    :type account: ~energycap.sdk.models.BillViewAccountChild
    :param begin_date: The bill's begin date
    :type begin_date: datetime
    :param end_date: The bill's end date
    :type end_date: datetime
    :param billing_period: The bill's billing period
    :type billing_period: int
    :param days: The bill's number of days
    :type days: int
    :param account_period: The bill's accounting period
    :type account_period: int
    :param account_period_name: The bill's accounting period name
    :type account_period_name: str
    :param hide_account_period: Is account period required?
    :type hide_account_period: bool
    :param hide_account_year: Is account year required?  What is it?
    :type hide_account_year: bool
    :param total_cost: The bill's total cost
    :type total_cost: float
    :param balance: The bill's balance
    :type balance: float
    :param estimated: Indicates if the bill is estimated
    :type estimated: bool
    :param hide_estimated: Is estimated flag required?
    :type hide_estimated: bool
    :param statement_date: The date of the billing statement
    :type statement_date: datetime
    :param hide_statement_date: Is statement date required?
    :type hide_statement_date: bool
    :param due_date: The date and time the bill is due
    :type due_date: datetime
    :param hide_due_date: Is due date required?
    :type hide_due_date: bool
    :param invoice_number: The bill's invoice number
    :type invoice_number: str
    :param hide_invoice_number: Is Invoice Number Required?
    :type hide_invoice_number: bool
    :param control_code: The bill's control code
    :type control_code: str
    :param hide_control_code: Is control code required?
    :type hide_control_code: bool
    :param bill_image_url: The fully qualified url to the bill image
    :type bill_image_url: str
    :param bill_note: Bill note
    :type bill_note: str
    :param next_reading: The bill's next reading date
    :type next_reading: datetime
    :param hide_next_reading: Is next reading date required?
    :type hide_next_reading: bool
    :param prior_bill_id: Bill ID for the bill on this account that
     immediately precedes this bill (used for navigating back to the prior
     bill)
    :type prior_bill_id: int
    :param next_bill_id: Bill ID for the bill on this account that immediately
     follows this bill (used for navigating to the next bill)
    :type next_bill_id: int
    :param bill_history: The bill history
    :type bill_history: list[~energycap.sdk.models.BillHistoryResponse]
    :param meters: The list of meters on the bill
    :type meters: list[~energycap.sdk.models.BillViewMeterChild]
    :param body_lines: The list of body lines on the bill
    :type body_lines: list[~energycap.sdk.models.BodylineChild]
    :param bill_account_meters: The list of account-meter summaries on the
     bill
    :type bill_account_meters:
     list[~energycap.sdk.models.BillAccountMeterChild]
    :param calendarized_history: Calendarized history information for the
     account
    :type calendarized_history:
     list[~energycap.sdk.models.BillCalendarizedHistory]
    :param reversal_details:
    :type reversal_details: ~energycap.sdk.models.BillReversal
    :param excluded_from_accruals: Indicates whether this bill is excluded
     from accruals or not
    :type excluded_from_accruals: bool
    :param analyzing: Indicates whether this bill is currently being analyzed
    :type analyzing: bool
    """

    _attribute_map = {
        'bill_id': {'key': 'billId', 'type': 'int'},
        'void': {'key': 'void', 'type': 'bool'},
        'from_vendor': {'key': 'fromVendor', 'type': 'bool'},
        'creation_method': {'key': 'creationMethod', 'type': 'str'},
        'accrual': {'key': 'accrual', 'type': 'bool'},
        'accrual_reversed': {'key': 'accrualReversed', 'type': 'bool'},
        'batch': {'key': 'batch', 'type': 'BatchChild'},
        'batch_end_date': {'key': 'batchEndDate', 'type': 'iso-8601'},
        'hide_batch_code': {'key': 'hideBatchCode', 'type': 'bool'},
        'created_by': {'key': 'createdBy', 'type': 'UserChild'},
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'modified_by': {'key': 'modifiedBy', 'type': 'UserChild'},
        'modified_date': {'key': 'modifiedDate', 'type': 'iso-8601'},
        'approved': {'key': 'approved', 'type': 'bool'},
        'approve_date': {'key': 'approveDate', 'type': 'iso-8601'},
        'approved_by': {'key': 'approvedBy', 'type': 'UserChild'},
        'has_been_split': {'key': 'hasBeenSplit', 'type': 'bool'},
        'was_split_date': {'key': 'wasSplitDate', 'type': 'iso-8601'},
        'export_hold': {'key': 'exportHold', 'type': 'bool'},
        'ap_exported': {'key': 'apExported', 'type': 'bool'},
        'ap_export_date': {'key': 'apExportDate', 'type': 'iso-8601'},
        'ap_exported_by': {'key': 'apExportedBy', 'type': 'UserChild'},
        'gl_exported': {'key': 'glExported', 'type': 'bool'},
        'gl_exported_by': {'key': 'glExportedBy', 'type': 'UserChild'},
        'gl_export_date': {'key': 'glExportDate', 'type': 'iso-8601'},
        'check_number': {'key': 'checkNumber', 'type': 'str'},
        'check_date': {'key': 'checkDate', 'type': 'iso-8601'},
        'pay_status': {'key': 'payStatus', 'type': 'str'},
        'cleared_date': {'key': 'clearedDate', 'type': 'iso-8601'},
        'account': {'key': 'account', 'type': 'BillViewAccountChild'},
        'begin_date': {'key': 'beginDate', 'type': 'iso-8601'},
        'end_date': {'key': 'endDate', 'type': 'iso-8601'},
        'billing_period': {'key': 'billingPeriod', 'type': 'int'},
        'days': {'key': 'days', 'type': 'int'},
        'account_period': {'key': 'accountPeriod', 'type': 'int'},
        'account_period_name': {'key': 'accountPeriodName', 'type': 'str'},
        'hide_account_period': {'key': 'hideAccountPeriod', 'type': 'bool'},
        'hide_account_year': {'key': 'hideAccountYear', 'type': 'bool'},
        'total_cost': {'key': 'totalCost', 'type': 'float'},
        'balance': {'key': 'balance', 'type': 'float'},
        'estimated': {'key': 'estimated', 'type': 'bool'},
        'hide_estimated': {'key': 'hideEstimated', 'type': 'bool'},
        'statement_date': {'key': 'statementDate', 'type': 'iso-8601'},
        'hide_statement_date': {'key': 'hideStatementDate', 'type': 'bool'},
        'due_date': {'key': 'dueDate', 'type': 'iso-8601'},
        'hide_due_date': {'key': 'hideDueDate', 'type': 'bool'},
        'invoice_number': {'key': 'invoiceNumber', 'type': 'str'},
        'hide_invoice_number': {'key': 'hideInvoiceNumber', 'type': 'bool'},
        'control_code': {'key': 'controlCode', 'type': 'str'},
        'hide_control_code': {'key': 'hideControlCode', 'type': 'bool'},
        'bill_image_url': {'key': 'billImageUrl', 'type': 'str'},
        'bill_note': {'key': 'billNote', 'type': 'str'},
        'next_reading': {'key': 'nextReading', 'type': 'iso-8601'},
        'hide_next_reading': {'key': 'hideNextReading', 'type': 'bool'},
        'prior_bill_id': {'key': 'priorBillId', 'type': 'int'},
        'next_bill_id': {'key': 'nextBillId', 'type': 'int'},
        'bill_history': {'key': 'billHistory', 'type': '[BillHistoryResponse]'},
        'meters': {'key': 'meters', 'type': '[BillViewMeterChild]'},
        'body_lines': {'key': 'bodyLines', 'type': '[BodylineChild]'},
        'bill_account_meters': {'key': 'billAccountMeters', 'type': '[BillAccountMeterChild]'},
        'calendarized_history': {'key': 'calendarizedHistory', 'type': '[BillCalendarizedHistory]'},
        'reversal_details': {'key': 'reversalDetails', 'type': 'BillReversal'},
        'excluded_from_accruals': {'key': 'excludedFromAccruals', 'type': 'bool'},
        'analyzing': {'key': 'analyzing', 'type': 'bool'},
    }

    def __init__(self, *, bill_id: int=None, void: bool=None, from_vendor: bool=None, creation_method: str=None, accrual: bool=None, accrual_reversed: bool=None, batch=None, batch_end_date=None, hide_batch_code: bool=None, created_by=None, created_date=None, modified_by=None, modified_date=None, approved: bool=None, approve_date=None, approved_by=None, has_been_split: bool=None, was_split_date=None, export_hold: bool=None, ap_exported: bool=None, ap_export_date=None, ap_exported_by=None, gl_exported: bool=None, gl_exported_by=None, gl_export_date=None, check_number: str=None, check_date=None, pay_status: str=None, cleared_date=None, account=None, begin_date=None, end_date=None, billing_period: int=None, days: int=None, account_period: int=None, account_period_name: str=None, hide_account_period: bool=None, hide_account_year: bool=None, total_cost: float=None, balance: float=None, estimated: bool=None, hide_estimated: bool=None, statement_date=None, hide_statement_date: bool=None, due_date=None, hide_due_date: bool=None, invoice_number: str=None, hide_invoice_number: bool=None, control_code: str=None, hide_control_code: bool=None, bill_image_url: str=None, bill_note: str=None, next_reading=None, hide_next_reading: bool=None, prior_bill_id: int=None, next_bill_id: int=None, bill_history=None, meters=None, body_lines=None, bill_account_meters=None, calendarized_history=None, reversal_details=None, excluded_from_accruals: bool=None, analyzing: bool=None, **kwargs) -> None:
        super(BillViewResponse, self).__init__(**kwargs)
        self.bill_id = bill_id
        self.void = void
        self.from_vendor = from_vendor
        self.creation_method = creation_method
        self.accrual = accrual
        self.accrual_reversed = accrual_reversed
        self.batch = batch
        self.batch_end_date = batch_end_date
        self.hide_batch_code = hide_batch_code
        self.created_by = created_by
        self.created_date = created_date
        self.modified_by = modified_by
        self.modified_date = modified_date
        self.approved = approved
        self.approve_date = approve_date
        self.approved_by = approved_by
        self.has_been_split = has_been_split
        self.was_split_date = was_split_date
        self.export_hold = export_hold
        self.ap_exported = ap_exported
        self.ap_export_date = ap_export_date
        self.ap_exported_by = ap_exported_by
        self.gl_exported = gl_exported
        self.gl_exported_by = gl_exported_by
        self.gl_export_date = gl_export_date
        self.check_number = check_number
        self.check_date = check_date
        self.pay_status = pay_status
        self.cleared_date = cleared_date
        self.account = account
        self.begin_date = begin_date
        self.end_date = end_date
        self.billing_period = billing_period
        self.days = days
        self.account_period = account_period
        self.account_period_name = account_period_name
        self.hide_account_period = hide_account_period
        self.hide_account_year = hide_account_year
        self.total_cost = total_cost
        self.balance = balance
        self.estimated = estimated
        self.hide_estimated = hide_estimated
        self.statement_date = statement_date
        self.hide_statement_date = hide_statement_date
        self.due_date = due_date
        self.hide_due_date = hide_due_date
        self.invoice_number = invoice_number
        self.hide_invoice_number = hide_invoice_number
        self.control_code = control_code
        self.hide_control_code = hide_control_code
        self.bill_image_url = bill_image_url
        self.bill_note = bill_note
        self.next_reading = next_reading
        self.hide_next_reading = hide_next_reading
        self.prior_bill_id = prior_bill_id
        self.next_bill_id = next_bill_id
        self.bill_history = bill_history
        self.meters = meters
        self.body_lines = body_lines
        self.bill_account_meters = bill_account_meters
        self.calendarized_history = calendarized_history
        self.reversal_details = reversal_details
        self.excluded_from_accruals = excluded_from_accruals
        self.analyzing = analyzing
