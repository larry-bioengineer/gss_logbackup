# Larry To
# Created on: 12/02/2020
# To read file from google sheet API 

import requests
import config

# All rows in CheckoutLog Table 
sysLog = requests.get(config.googleSheetAPI + "/tabs/CheckoutLog")

print(sysLog.text)

# All rows in CheckoutLog Table 
# sysLog = requests.get(config.googleSheetAPI + "/tabs/CheckoutLog")