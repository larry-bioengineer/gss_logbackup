# code tester 

import requests
from datetime import datetime, date, timedelta
import time
import config
from pathlib import Path

updateTime = 5.0

timeDiff = datetime.now() + timedelta(minutes=updateTime)
timeDiff1 = datetime.now() + timedelta(days=1)
timeDiff1 = timeDiff1.replace(hour=0, minute=0, second=0, microsecond=0)

print(timeDiff)
print(timeDiff1)

print((timeDiff1 - timeDiff).total_seconds())