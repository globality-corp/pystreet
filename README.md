# pystreet

Street addresses validation, normalization, and geocoding functionality.


## Installation

To install, simply install this package via pip into your desired virtualenv, e.g:

    pip install pystreet


## Usage

See [tests/](./pystreet/tests/) for more usage examples.

### Validation

For basic validation, you can use a couple of hand-tuned validators that are provided.

The first one is a "non-strict" validator, which will simply try to find a known country mention in the text string (by name or ISO alpha code), and then try to match a compound regular expression to find some "address-like" sub-structure in the string. This is useful for minimally validating global addresses where nothing else is known apriori about the address structure to be expected. Example:

```python
from pystreet.validator import nonstrict_address_validator


validator = nonstrict_address_validator()
validator("1234 Foo bar st. #10, Menlo Park CA United States")
```
