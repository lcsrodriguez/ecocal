# Economic Calendar

<img src="https://img.shields.io/static/v1?label=Languages&message=Python&color=ff0000"/>&nbsp;<img src="https://img.shields.io/static/v1?label=Restriction&message=NO&color=26c601"/> ![GitHub release (latest by date)](https://img.shields.io/github/v/release/lcsrodriguez/ecocal) ![python version | 3.10+](https://img.shields.io/badge/Python%20version-3.10+-magenta) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) ![](https://img.shields.io/badge/Dependabot-enabled-blue)


## Overview

`ecocal` is a light-weight and easy-to-user Python package allowing every developer to retrieve full access to both historical and future insightful and hifhly-detailed economic calendar (worldwide scale).

****

*Disclaimer*: 
- Data scraped and processed from external sources: **[FxStreet](https://www.fxstreet.com/economic-calendar)** website.
- Data provided **AS IS** for information purpose only. 


## Getting started

```shell
git clone https://github.com/lcsrodriguez/ecocal.git
cd ecocal/

python3 -m venv .venv
source .venv/bin/activate

pip3 install -r requirements.txt
pip3 freeze

python3 setup.py sdist bdist_wheel # Build the package from source
```

Run the example script:
```
python3 test/test.py
```

```python
from ecocal import Calendar

ec = Calendar(startHorizon="2023-10-10", 
                      endHorizon="2023-10-12", 
                      withDetails=True
                      )

ec.saveCalendar(withDetails=True)
```


## Project's architecture

```
./
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
└── requirements.txt
```

To reproduce the file tree, run: `tree -L 2 -I '*.csv'`

## License

[MIT](LICENSE)