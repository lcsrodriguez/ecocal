from ecocal import *


ec = Calendar(startHorizon="2023-10-26",
              endHorizon="2023-10-28",
              withDetails=False,
              nbThreads=20,
              preBuildCalendar=False,
              )
print(ec)
