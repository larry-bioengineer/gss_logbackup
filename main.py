# Larry To
# Created on: 11/26/2020
# To extrat file from user chosen directory and upload to a google sheet 

import requests
from datetime import datetime
import time

try: 
	while True:

		# Locate Checkout Data from Directory 
		results = []	
		with open('checkout_log_demo.log') as f:
			lines = f.readlines()
			for line in lines:
				r = line.split(" ")
				results.append({'Date': ' '.join(r[0:3]), 'Room': r[3], 'Remarks': r[4].rstrip("\r\n")})
		print(results)

		# Upload results to Google Sheet 
		requests.post(
			"https://sheet.best/api/sheets/e4d92608-bec0-46f4-b43e-1d558e790c28/tabs/Checkout Log",
			json = results
		)


		# Locate System Log Data from Directory
		results = []
		with open('13-11-2020.log') as f:
			lines = f.readlines()
			for line in lines:
				r = line.split(" 	 ")
				if len(r) == 3:
					results.append({'Date': r[0], 'Status': r[1], 'Message': r[2].rstrip("\r\n")})

		# Upload results to Google Sheet 
		requests.post(
			"https://sheet.best/api/sheets/e4d92608-bec0-46f4-b43e-1d558e790c28/tabs/System Log",
			json = results
		)

		# Program stops for 5 min then re-run 
		time.sleep(60*5)

except KeyboardInterrupt:
	pass

