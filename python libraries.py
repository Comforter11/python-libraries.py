# Print 10 dates, two weeks apart.
from datetime import datetime, timedelta

today = datetime.today()

# Print 10 dates, two weeks apart.
for d in range(10):
    now_date = today + timedelta(days=14)
    today = now_date
    print(now_date.strftime("%Y %m %d"))
