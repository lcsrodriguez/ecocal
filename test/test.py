from ecocal import *


ec = EconomicCalendar(startHorizon="2023-01-01",
                      endHorizon="2023-12-31",
                      withDetails=True,
                      nbThreads=40
                      )
ec.saveCalendar(True)
