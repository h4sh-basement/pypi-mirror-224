# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class PlaceResponse(Model):
    """PlaceResponse.

    :param parent:
    :type parent: ~energycap.sdk.models.PlaceChild
    :param place_type:
    :type place_type: ~energycap.sdk.models.PlaceTypeResponse
    :param created_date: The date and time the place was created
    :type created_date: datetime
    :param created_by:
    :type created_by: ~energycap.sdk.models.UserChild
    :param modified_date: The date and time of the most recent modification to
     the place
    :type modified_date: datetime
    :param modified_by:
    :type modified_by: ~energycap.sdk.models.UserChild
    :param address:
    :type address: ~energycap.sdk.models.AddressChild
    :param build_date: The date and time the place was built
    :type build_date: datetime
    :param primary_use:
    :type primary_use: ~energycap.sdk.models.PrimaryUseChild
    :param weather_station:
    :type weather_station: ~energycap.sdk.models.WeatherStationChild
    :param size:
    :type size: ~energycap.sdk.models.PlaceSizeChild
    :param benchmark1:
    :type benchmark1: ~energycap.sdk.models.LatestBenchmarkValue
    :param benchmark2:
    :type benchmark2: ~energycap.sdk.models.LatestBenchmarkValue
    :param benchmark3:
    :type benchmark3: ~energycap.sdk.models.LatestBenchmarkValue
    :param energy_star_enabled: Tells whether energy star is enabled for the
     given place
    :type energy_star_enabled: bool
    :param energy_star_rating:
    :type energy_star_rating: ~energycap.sdk.models.EnergyStarRatingChild
    :param places: An array of child places. A child place is one directly
     beneath the current place on the buildings and meters tree
    :type places: list[~energycap.sdk.models.PlaceChild]
    :param meters: An array of child meters. A child meter is one directly
     beneath the current place on the buildings and meters tree
    :type meters: list[~energycap.sdk.models.MeterChild]
    :param contact:
    :type contact: ~energycap.sdk.models.ContactChild
    :param place_description: A description of the place
    :type place_description: str
    :param wattics_site:
    :type wattics_site: ~energycap.sdk.models.WatticsSite
    :param place_id: The place identifier
    :type place_id: int
    :param place_code: The place code
    :type place_code: str
    :param place_info: The place info
    :type place_info: str
    """

    _attribute_map = {
        'parent': {'key': 'parent', 'type': 'PlaceChild'},
        'place_type': {'key': 'placeType', 'type': 'PlaceTypeResponse'},
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'created_by': {'key': 'createdBy', 'type': 'UserChild'},
        'modified_date': {'key': 'modifiedDate', 'type': 'iso-8601'},
        'modified_by': {'key': 'modifiedBy', 'type': 'UserChild'},
        'address': {'key': 'address', 'type': 'AddressChild'},
        'build_date': {'key': 'buildDate', 'type': 'iso-8601'},
        'primary_use': {'key': 'primaryUse', 'type': 'PrimaryUseChild'},
        'weather_station': {'key': 'weatherStation', 'type': 'WeatherStationChild'},
        'size': {'key': 'size', 'type': 'PlaceSizeChild'},
        'benchmark1': {'key': 'benchmark1', 'type': 'LatestBenchmarkValue'},
        'benchmark2': {'key': 'benchmark2', 'type': 'LatestBenchmarkValue'},
        'benchmark3': {'key': 'benchmark3', 'type': 'LatestBenchmarkValue'},
        'energy_star_enabled': {'key': 'energyStarEnabled', 'type': 'bool'},
        'energy_star_rating': {'key': 'energyStarRating', 'type': 'EnergyStarRatingChild'},
        'places': {'key': 'places', 'type': '[PlaceChild]'},
        'meters': {'key': 'meters', 'type': '[MeterChild]'},
        'contact': {'key': 'contact', 'type': 'ContactChild'},
        'place_description': {'key': 'placeDescription', 'type': 'str'},
        'wattics_site': {'key': 'watticsSite', 'type': 'WatticsSite'},
        'place_id': {'key': 'placeId', 'type': 'int'},
        'place_code': {'key': 'placeCode', 'type': 'str'},
        'place_info': {'key': 'placeInfo', 'type': 'str'},
    }

    def __init__(self, *, parent=None, place_type=None, created_date=None, created_by=None, modified_date=None, modified_by=None, address=None, build_date=None, primary_use=None, weather_station=None, size=None, benchmark1=None, benchmark2=None, benchmark3=None, energy_star_enabled: bool=None, energy_star_rating=None, places=None, meters=None, contact=None, place_description: str=None, wattics_site=None, place_id: int=None, place_code: str=None, place_info: str=None, **kwargs) -> None:
        super(PlaceResponse, self).__init__(**kwargs)
        self.parent = parent
        self.place_type = place_type
        self.created_date = created_date
        self.created_by = created_by
        self.modified_date = modified_date
        self.modified_by = modified_by
        self.address = address
        self.build_date = build_date
        self.primary_use = primary_use
        self.weather_station = weather_station
        self.size = size
        self.benchmark1 = benchmark1
        self.benchmark2 = benchmark2
        self.benchmark3 = benchmark3
        self.energy_star_enabled = energy_star_enabled
        self.energy_star_rating = energy_star_rating
        self.places = places
        self.meters = meters
        self.contact = contact
        self.place_description = place_description
        self.wattics_site = wattics_site
        self.place_id = place_id
        self.place_code = place_code
        self.place_info = place_info
