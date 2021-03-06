# Larry To
# Created on: 12/02/2020
# Sample code to read file from google sheet API 

import requests
import config

# All rows in CheckoutLog Table 
sysLog = requests.get(config.googleSheetAPI + "/tabs/CheckoutLog", 
		headers={
			'X-Api-Key': config.serverAPIKey
		})
# print(sysLog.text)

# Filter Data for Room 101 
sysLog = requests.get(config.googleSheetAPI + "/tabs/CheckoutLog/Room/101", 
		headers={
			'X-Api-Key': config.serverAPIKey
		})
print(sysLog.text)