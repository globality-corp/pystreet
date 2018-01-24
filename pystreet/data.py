"""
Data helpers.

"""
import pycountry


def non_qualified_code(code):
    """
    Some codes, e.g. ISO 3166-2 subdivision codes, are compound and are formatted as
    "{country_code}-{subdivision_code}". For validation cases we often care about
    extracting the non-qualified subdivision code in such cases.

    """
    return code.split("-", 2)[1]


def iter_country_names():
    for country in pycountry.countries:
        if hasattr(country, "official_name"):
            yield country.official_name
        yield country.name
        yield country.alpha_3


def iter_subdivision_names():
    for subdivision in pycountry.subdivisions:
        yield subdivision.name
        yield subdivision.code
        yield non_qualified_code(subdivision.code)
