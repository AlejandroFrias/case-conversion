![](https://github.com/AlejandroFrias/case-conversion/workflows/CI/badge.svg)
![](https://img.shields.io/pypi/pyversions/case_conversion)
![](https://img.shields.io/pypi/v/case_conversion)
![](https://github.com/AlejandroFrias/case-conversion/blob/gh-pages/coverage.svg?raw=true)

# Case Conversion

This is a port of the Sublime Text 3 plugin [CaseConversion](https://github.com/jdc0589/CaseConversion), by [Davis Clark's](https://github.com/jdc0589), to a regular python package. I couldn't find any other python packages on PyPI at the time (Feb 2016) that could seamlessly convert from any case to any other case without having to specify from what type of case I was converting. This plugin worked really well, so I separated the (non-sublime) python parts of the plugin into this useful python package. I also added Unicode support via python's `unicodedata`.

## Features

- Autodetection of case *(no need to specify explicitly which case you are converting from!)*
- Acronym detection *(no funky splitting on every capital letter of an all caps acronym like `HTTPError`!)*
- Unicode supported (non-ASCII characters are first class citizens!)
- Dependency free!
- Supports Python 3.6+
- Over 95 percent test coverage and full type annotation.
- Every case conversion from/to you ever gonna need:
  - `camelCase`
  - `PascalCase`
  - `snake_case`
  - `dash-case` (aka `kebap-case`, `spinal-case`  or `slug-case`)
  - `CONST_CASE` (aka `SCREAMING_SNAKE_CASE`)
  - `dot.case`
  - `separate words`
  - `slash/case`
  - `backslash\\case`
  - `Ada_Case`
  - `Http-Header-Case`

## Usage

Normal use is self-explanatory.

```python
>>> import case_conversion
>>> case_conversion.dash("FOO_BAR_STRING")
'foo-bar-string'
```

To use acronym detection simply pass in a list of `acronyms` to detect as whole words.

```python
>>> import case_conversion
>>> case_conversion.snake("fooBarHTTPError")
'foo_bar_h_t_t_p_error'  # ewwww :(
>>> case_conversion.snake("fooBarHTTPError", acronyms=['HTTP'])
'foo_bar_http_error'  # pretty :)
```

Unicode is fully supported - even for acronyms.

```python
>>> import case_conversion
>>> case_conversion.const(u"fóó-bar-string")
FÓÓ_BAR_STRING
>>> case_conversion.snake("fooBarHÓÓPError", acronyms=['HÓÓP'])
'foo_bar_hóóp_error'
```



## Install

```
pip install case-conversion
```



## Contribute

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

This package is being developed with [poetry]([https://python-poetry.org/](https://python-poetry.org/)) (-> [docs]([https://python-poetry.org/docs/](https://python-poetry.org/docs/))).

Before opening a pull request, please make sure to:

- update tests as appropriate

- `flake8`, `mypy` and `pytest` are happy



## Credits

Credit goes to [Davis Clark's](https://github.com/jdc0589) as the author of the original plugin and its contributors (Scott Bessler, Curtis Gibby, Matt Morrison). Thanks for their awesome work on making such a robust and awesome case converter.

Further credit goes to @olsonpm for making this package dependency-free.



## Licence

Using [MIT licence](LICENSE.txt) with Davis Clark's Copyright
