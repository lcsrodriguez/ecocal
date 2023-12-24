from ecocal import *


ec = Calendar(startHorizon="2020-01-01",
                      endHorizon="2024-12-31",
                      withDetails=True,
                      nbThreads=200
                      )
ec.saveCalendar(True)
