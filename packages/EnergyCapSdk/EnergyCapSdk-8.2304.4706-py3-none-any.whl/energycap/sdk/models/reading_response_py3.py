# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ReadingResponse(Model):
    """ReadingResponse.

    :param imported_readings_count: The number of successfully imported
     readings
    :type imported_readings_count: int
    :param failed_readings_count: The number of failed reading imports
    :type failed_readings_count: int
    :param failed_readings: Data representing the failed reading imports
    :type failed_readings: list[~energycap.sdk.models.FailedReadingResponse]
    """

    _attribute_map = {
        'imported_readings_count': {'key': 'importedReadingsCount', 'type': 'int'},
        'failed_readings_count': {'key': 'failedReadingsCount', 'type': 'int'},
        'failed_readings': {'key': 'failedReadings', 'type': '[FailedReadingResponse]'},
    }

    def __init__(self, *, imported_readings_count: int=None, failed_readings_count: int=None, failed_readings=None, **kwargs) -> None:
        super(ReadingResponse, self).__init__(**kwargs)
        self.imported_readings_count = imported_readings_count
        self.failed_readings_count = failed_readings_count
        self.failed_readings = failed_readings
