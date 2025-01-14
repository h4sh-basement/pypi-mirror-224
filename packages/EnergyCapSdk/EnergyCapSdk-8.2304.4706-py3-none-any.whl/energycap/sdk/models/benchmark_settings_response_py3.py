# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class BenchmarkSettingsResponse(Model):
    """BenchmarkSettingsResponse.

    :param benchmark1:
    :type benchmark1: ~energycap.sdk.models.BenchmarkWithUsedCountResponse
    :param benchmark2:
    :type benchmark2: ~energycap.sdk.models.BenchmarkWithUsedCountResponse
    :param benchmark3:
    :type benchmark3: ~energycap.sdk.models.BenchmarkWithUsedCountResponse
    """

    _attribute_map = {
        'benchmark1': {'key': 'benchmark1', 'type': 'BenchmarkWithUsedCountResponse'},
        'benchmark2': {'key': 'benchmark2', 'type': 'BenchmarkWithUsedCountResponse'},
        'benchmark3': {'key': 'benchmark3', 'type': 'BenchmarkWithUsedCountResponse'},
    }

    def __init__(self, *, benchmark1=None, benchmark2=None, benchmark3=None, **kwargs) -> None:
        super(BenchmarkSettingsResponse, self).__init__(**kwargs)
        self.benchmark1 = benchmark1
        self.benchmark2 = benchmark2
        self.benchmark3 = benchmark3
