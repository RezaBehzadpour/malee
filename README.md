[![Build Status](https://travis-ci.com/RezaBehzadpour/financial-modeling.svg?branch=master)](https://travis-ci.com/RezaBehzadpour/financial-modeling)
[![codecov](https://codecov.io/gh/RezaBehzadpour/financial-modeling/branch/master/graph/badge.svg?token=CNWKBIN7US)](https://codecov.io/gh/RezaBehzadpour/financial-modeling)
[![Documentation Status](https://readthedocs.org/projects/financial-modeling/badge/?version=latest)](https://financial-modeling.readthedocs.io/en/latest/?badge=latest)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
![PyPI](https://img.shields.io/pypi/v/financial-modeling)
![PyPI - Downloads](https://img.shields.io/pypi/dm/financial-modeling)

# Financial Modeling
The `financial_modeling` package contains a collection of financial modeling functions.

Simplicity and ease of understanding for educational use cases is my major goal for this package at the moment. Hence I didn't use any fancy libraries like `numpy` for better performance.  

The source code of this package is available at https://github.com/RezaBehzadpour/financial_modeling

## Install
To install the current release of `financial_modeling`, type the following command in terminal:
```bash
$ pip install -U financial_modeling
```

## How to use?
Here's how you can calculate simple **Arithmetic Return**:  
```python
>>> import financial_modeling as fm
>>> fm.ar(100, 140)
0.4
```

For more information, see the [documentation](https://financial-modeling.readthedocs.io).

## License
[BSD 3-Clause](LICENSE)
