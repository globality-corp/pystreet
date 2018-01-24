"""
Street address validators.

"""
import re
from abc import ABCMeta, abstractmethod

from pystreet.automaton import boundary_check, build_automaton, normalize
from pystreet.data import iter_country_names


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

    def __init__(self, boundary_check=boundary_check, regexp=NONSTRICT_REGEXP):
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
        self.automaton = build_automaton(vocabulary=iter_country_names())
        self.boundary_check = boundary_check
        self.regexp = regexp

    def validate(self, string):
        normalized = normalize(string)
        if not self.regexp.search(normalized):
            # Try to minimally identify address-like substructure first
            raise ValueError(f"Could not identify an address-like substructure in string: {string}")

        for end_position, (length, *tail) in self.automaton.iter(normalized):
            end_idx = end_position + 1
            start_idx = end_idx - length

            if not self.boundary_check(string, start_idx, end_idx):
                # Make sure string match aligns with word boundaries
                continue

            # If we reached here, can short circuit and verify address
            return True

        raise ValueError(f"Could not find a country mention in string: {string}")


def nonstrict_address_validator():
    return NonstrictAddressValidator()
