# date_converter

Automatically convert datenum to date string of yyyy-mm-dd, or convert date string to datenumm

## Installation

```bash
$ pip install date_converter
```

## Usage

`date_converter` can be used to convert datenum to date string or date string to datenum automatically as follows:

```python
from date_converter.date_converter import date_converter

dt_num = date_converter('2020-01-01')
dt_str = date_converter(737425)
```

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`date_converter` was created by suuuuperNOVA. It is licensed under the terms of the MIT license.

## Credits

`date_converter` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
