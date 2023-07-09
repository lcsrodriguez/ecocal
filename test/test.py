from ecocal import *


ec = EconomicCalendar(startHorizon="2023-10-10", endHorizon="2023-10-12")


df_ = ec.getCalendar(withDetails=True)

print(df_)
print(ec.ecocal.shape)