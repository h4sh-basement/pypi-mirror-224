# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ToggleVisible(Model):
    """ToggleVisible.

    :param visible:  <span class='property-internal'>Required (defined)</span>
    :type visible: bool
    """

    _attribute_map = {
        'visible': {'key': 'visible', 'type': 'bool'},
    }

    def __init__(self, **kwargs):
        super(ToggleVisible, self).__init__(**kwargs)
        self.visible = kwargs.get('visible', None)
