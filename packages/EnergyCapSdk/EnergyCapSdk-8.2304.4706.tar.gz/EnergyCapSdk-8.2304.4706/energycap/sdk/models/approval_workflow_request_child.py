# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ApprovalWorkflowRequestChild(Model):
    """Bill approval settings.

    All required parameters must be populated in order to send to Azure.

    :param confirm_edit_delete: Required. Whether or not edit / delete should
     be confirmed <span class='property-internal'>Required</span>
    :type confirm_edit_delete: bool
    """

    _validation = {
        'confirm_edit_delete': {'required': True},
    }

    _attribute_map = {
        'confirm_edit_delete': {'key': 'confirmEditDelete', 'type': 'bool'},
    }

    def __init__(self, **kwargs):
        super(ApprovalWorkflowRequestChild, self).__init__(**kwargs)
        self.confirm_edit_delete = kwargs.get('confirm_edit_delete', None)
