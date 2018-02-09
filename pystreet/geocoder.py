from abc import ABCMeta, abstractmethod

import googlemaps


class AddressGeocoder(metaclass=ABCMeta):

    def __call__(self, string):
        """
        Geocode address given as string.

        """
        return self.geocode(string)

    @abstractmethod
    def geocode(self, string):
        """
        Geocode given street address string.

        """


class GoogleMapsAddressGeocoder(AddressGeocoder):

    def __init__(self, api_key):
        self.api_key = api_key

    @property
    def client(self):
        if not getattr(self, "_client", None):
            self._client = googlemaps.Client(key=self.api_key)
        return self._client

    def geocode(self, string):
        return self.client.geocode(string)
