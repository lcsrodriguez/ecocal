# Economic Calendar

<img src="https://img.shields.io/static/v1?label=Languages&message=Python&color=ff0000"/>&nbsp;<img src="https://img.shields.io/static/v1?label=Restriction&message=NO&color=26c601"/> ![GitHub release (latest by date)](https://img.shields.io/github/v/release/lcsrodriguez/ecocal) ![python version | 3.10+](https://img.shields.io/badge/Python%20version-3.10+-magenta) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![CodeQL](https://github.com/lcsrodriguez/ecocal/actions/workflows/codeql.yml/badge.svg)](https://github.com/lcsrodriguez/ecocal/actions/workflows/codeql.yml)&nbsp;![](https://img.shields.io/badge/Dependabot-enabled-blue)

![PyPI - Downloads](https://img.shields.io/pypi/dw/ecocal)
![PyPI - Format](https://img.shields.io/pypi/format/ecocal)
![PyPI - Implementation](https://img.shields.io/pypi/implementation/ecocal)
![PyPI - License](https://img.shields.io/pypi/l/ecocal)
![PyPI - Version](https://img.shields.io/pypi/v/ecocal)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/ecocal)

## Overview

`ecocal` is a light-weight and easy-to-user Python package allowing every developer to retrieve full access to both historical and future insightful and hifhly-detailed economic calendar (worldwide scale).

****

**DISCLAIMER**: 
- Data extracted from external providers. No warranty on data quality/accuracy.
- Data provided **AS IS** for information purpose only.

## Getting started

> Install from **PyPI**:
1. Install `ecocal` package
    ```shell
    pip3 install ecocal
    ```
2. Execute the example code
    ```python
   from ecocal import *
   
   
   def main() -> None:
       ec = Calendar(startHorizon="2023-10-26",
                     endHorizon="2023-11-30",
                     withDetails=True,
                     nbThreads=20,
                     preBuildCalendar=True,
                     )
       print(ec)
       # On-disk saving of detailed calendar
       ec.saveCalendar()
   
   if __name__ == "__main__":
       main()
    ```
    Code available using:
    - `python examples/main.py`
    - `jupyter-notebook examples/main.ipynb` (dynamic debugging)


> Install from **source**
1. Clone the repository:
    ```shell
    git clone https://github.com/lcsrodriguez/ecocal.git
    cd ecocal/
    ```
2. Create a virtual environment for **clean** environment
    ```shell
    python3 -m venv venv
    source venv/bin/activate
    ```
3. Install the required Python packages
    ```shell
    pip3 install -r requirements.txt
    pip3 freeze
    ```
4. Initiate the project
    ```shell
    make init
    ```

## Project's architecture

```
./
├── CITATION.cff
├── Dockerfile
├── LICENSE
├── Makefile
├── README.md
├── ecocal/
│   ├── Calendar.py
│   ├── Event.py
│   ├── __init__.py
│   ├── constants.py
│   └── utils.py
├── examples/
│   ├── main.ipynb
│   └── main.py
├── requirements.txt
└── setup.py
```

## License & Credits

- **[Lucas RODRIGUEZ](https://lcsrodriguez.github.io)**

The [LICENSE](LICENSE) file contains the full license details.


If you are using this package for research purposes, you can quote it as shown below *(BibTeX format)*:

```shell
@software{RODRIGUEZ_ecocal_2023,
author = {RODRIGUEZ, Lucas},
month = dec,
title = {{ecocal}},
url = {https://github.com/lcsrodriguez/ecocal},
version = {1.2.1},
year = {2023}
}
```
