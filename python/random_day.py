from datetime import date
import random

start_date = date.today().replace(day=1, month=1).toordinal()
end_date = date.today().toordinal()
random_day = date.fromordinal(random.randint(start_date, end_date))



print(random_day)