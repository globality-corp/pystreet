"""
Data helpers.

"""
import pycountry


def iter_country_names():
    for country in pycountry.countries:
        if hasattr(country, "official_name"):
            yield country.official_name
        yield country.name
        yield country.alpha_3
