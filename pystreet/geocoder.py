from abc import ABCMeta, abstractmethod
from atexit import register
from os.path import isfile
from pickle import dump, load

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
    def __init__(self, api_key, cache_path=None):
        """
        Instantiate a new google maps geocoder

        :param api_key: {str} geocoding approved Google API key
        :param cache_path: {str} optional path to specify if caching query responses
            is desired. Make sure to account for the Maps TOS before using this local
            data. Note that caching is not process safe, so if parallelization
            is desired, use multi-threading instead of multi-processing.

        """
        self.api_key = api_key
        self.cache_path = cache_path

        self.cache = self.load_cache(cache_path)

        if self.cache_path is not None:
            register(self.save_cache)

    @property
    def client(self):
        if not getattr(self, "_client", None):
            self._client = googlemaps.Client(key=self.api_key)
        return self._client

    def geocode(self, string):
        if string in self.cache:
            return self.cache[string]

        self.cache[string] = self.client.geocode(string)
        return self.cache[string]

    def load_cache(self, path):
        """
        Loads the pickle file that contains our cache

        """
        if path is None or not isfile(path):
            return {}

        with open(path, "rb") as file:
            return load(file)

    def save_cache(self):
        """
        Save the cache to disk

        Clients should explicitly call this method if they want to make sure the cache
        is saved, since there are some catches with relying on registering application
        exit functions

        """
        if self.cache_path is None:
            raise ValueError("No cache specified during initialization")
        with open(self.cache_path, "wb") as file:
            dump(self.cache, file)
