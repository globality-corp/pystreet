"""
Street address validators.

"""
import re
from abc import ABCMeta, abstractmethod

from pystreet.automaton import boundary_check, build_automaton, match_automaton, normalize
from pystreet.data import iter_country_names, iter_subdivision_names


NONSTRICT_REGEXP = re.compile(
    r"""
    (?:
        (?:\b[0-9]+\s+[a-z]+\W+)   # e.g. '123 foo', '456 bar st.'
    |
        (?:\b[a-z]+\s+[0-9]+[\-\W]+)   # e.g. '', 'foobar 123,' 'foobar 2-4, 111'
    )

    """,
    re.IGNORECASE | re.VERBOSE,
)


class AddressValidator(metaclass=ABCMeta):

    def __call__(self, string):
        return self.validate(string)

    @abstractmethod
    def validate(self, string):
        """
        Validate given string is a street address.

        """


class NonstrictAddressValidator(AddressValidator):

    def __init__(
        self,
        require_country,
        require_subdivision,
        boundary_check=boundary_check,
        regexp=NONSTRICT_REGEXP,
    ):
        """
        Non-strict street address validation.
        This validator is applicable in the broadest scope of global street address
        where nothing further is known about the string to be validated.

        It uses a simple heuristic:

        * Try to find a country mention (by name / ISO alpha-2 or alpha-3 code)
          at word boundaries in string using a string matching automaton.
        * Try to find some sub-structure in string that vaguely "looks like an address"
          This is done using a regular expression which tries to find some combination
          of numeric and alphabetical tokens in string.

        """
        self.require_country = require_country
        self.require_subdivision = require_subdivision
        self.boundary_check = boundary_check
        self.regexp = regexp

        if self.require_country:
            self.country_automaton = build_automaton(vocabulary=iter_country_names())
        if self.require_subdivision:
            self.subdivision_automaton = build_automaton(vocabulary=iter_subdivision_names())

    def validate(self, string):
        normalized = normalize(string)
        if not self.regexp.search(normalized):
            # Try to minimally identify address-like substructure first
            raise ValueError(f"Could not identify an address-like substructure in string: {string}")

        if (
            self.require_country and
            not match_automaton(normalized, self.country_automaton, self.boundary_check)
        ):
            raise ValueError(f"Could not find a country mention in string: {string}")

        if (
            self.require_subdivision and
            not match_automaton(normalized, self.subdivision_automaton, self.boundary_check)
        ):
            raise ValueError(f"Could not find a country subdivision mention in string: {string}")

        return True


def nonstrict_address_validator(require_country=True, require_subdivision=False):
    return NonstrictAddressValidator(
        require_country=require_country,
        require_subdivision=require_subdivision,
    )
