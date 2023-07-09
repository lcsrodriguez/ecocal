from ecocal import *


ec = EconomicCalendar(startHorizon="2020-01-01",
                      endHorizon="2024-12-31",
                      withDetails=True,
                      nbThreads=200
                      )
ec.saveCalendar(True)
