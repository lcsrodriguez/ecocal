from ecocal import *


ec = Calendar(startHorizon="2023-10-26",
              endHorizon="2023-11-30",
              withDetails=True,
              nbThreads=20,
              preBuildCalendar=True,
              )
print(ec)
