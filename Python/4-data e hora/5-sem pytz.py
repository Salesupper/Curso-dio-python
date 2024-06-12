from datetime import datetime as dt, timezone as tz, timedelta as td

data_oslo = dt.now(tz(td(hours=2), 'OSL'))
data_sp = dt.now(tz(td(hours=3), 'SPL'))

print(data_oslo)
print(data_sp)