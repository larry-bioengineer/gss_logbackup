# Larry To
# Created on: 11/26/2020
# To extrat file from user chosen directory and upload to a google sheet 

import requests
from datetime import datetime, date
import time

checkoutLogPath = "C:\\Program Files (x86)\\Golden News Enterprises Ltd\\Guest Service Station\\Checkout log\\"
systemLogPath = "C:\\Program Files (x86)\\Golden News Enterprises Ltd\\Guest Service Station\\log\\"

try: 
	while True:
		today = date.today()
		dayString = today.strftime("%d-%m-%Y")

		# Locate Checkout Data from Directory 
		results = []
		fileName = dayString + ' checkout.log'
		directory = checkoutLogPath + fileName

		with open('checkout log demo.log') as f:
			lines = f.readlines()[1:]
			for line in lines:
				r = line.split("	")				
				results.append({'Date': r[0], 'Room': r[1], 'Remarks': r[2].rstrip("\n")})

		# Upload results to Google Sheet 
		requests.post(
			"https://sheet.best/api/sheets/e4d92608-bec0-46f4-b43e-1d558e790c28/tabs/Checkout Log",
			json = results
		)


		# Locate System Log Data from Directory
		results = []
		fileName = dayString + '.log'
		directory = systemLogPath + fileName

		with open('13-11-2020.log') as f:
			lines = f.readlines()[1:]
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

