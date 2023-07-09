# Economic Calendar tool


## Overview

This tool allows the user to get full access to the historical and future economic calendar (worldwide scale).

Public data scraped and processed from the **[FxStreet](https://www.fxstreet.com/economic-calendar)**.


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
from ecocal import EconomicCalendar

ec = EconomicCalendar(startHorizon="2023-10-10", 
                      endHorizon="2023-10-12", 
                      withDetails=True
                      )

ec.saveCalendar(withDetails=True)
```

## License

[MIT](LICENSE)