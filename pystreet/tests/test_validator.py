from hamcrest import assert_that, calling, is_, raises
from parameterized import parameterized

from pystreet.validator import nonstrict_address_validator


@parameterized([
    ("Schlesische Str. 25/26, 10997 Berlin, Germany",),
    ("Goethestrasse 81, Düsseldorf, Germany 40237"),
    ("Al. Prymasa Tysiaclecia 43B / 24, Warszawa, Mazowieckie, Poland 01-242"),
    ("Szachowa 3, Warszawa, mazowieckie, Poland 04-894"),
    ("Guðríðarstígur 2-4, 111, Reykjavík, Iceland"),
    ("Signor Paolo Gaspari Enterprise Hotel CORSO SEMPIONE 91 20149 MILANO MI ITALY"),
    ("8 Homewood Pl #100, Menlo Park, CA 94025 United States",),
    ("560 Mission St #1200, San Francisco, CA 94105 USA",),
])
def test_nonstrict_validator_on_valid_cases(string):
    validator = nonstrict_address_validator()

    assert_that(
        validator(string),
        is_(True),
    )


@parameterized([
    ("foobar",),
    ("foo bar",),
    ("1234",),
    ("123 foobar",),
    ("USA",),
    ("Germany",),
])
def test_nonstrict_validator_with_invalid_cases(string):
    validator = nonstrict_address_validator()

    assert_that(
        calling(validator).with_args(string),
        raises(ValueError),
    )