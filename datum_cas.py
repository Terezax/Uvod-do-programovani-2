from datetime import datetime, timedelta
print(datetime.now())

apollo_start = datetime(1969, 7, 16, 14, 32)
print(apollo_start.strftime("%m/%d/%Y"))

so_start = datetime(2020, 2, 10, 5, 3)
print(so_start.isoweekday())
print(datetime.now() - so_start)



