# Larry To
# Created on: 11/26/2020
# To extrat file from user chosen directory and upload to a google sheet 

# Libraries
import requests
from datetime import datetime, date
import time

# Parameters
checkoutLogPath = "C:\\Program Files (x86)\\Golden News Enterprises Ltd\\Guest Service Station\\Checkout log\\"
systemLogPath = "C:\\Program Files (x86)\\Golden News Enterprises Ltd\\Guest Service Station\\log\\"
updateTime = 1.0; # in minutes 

try: 
	while True:

		today = date.today()
		dayString = today.strftime("%d-%m-%Y")
		print("Periodic Data Backup for Guest Service Station at " + datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))

		# Locate Checkout Data from Directory 
		results = []
		fileName = dayString + ' checkout.log'
		directory = checkoutLogPath + fileName
		

		with open('01-12-2020 checkout.log') as f:
			lines = f.readlines()[1:]
			for line in lines:
				r = line.split("	")

				# append data within 5 min 
				datetimeObject = datetime.strptime(r[0], '%m/%d/%Y %I:%M:%S %p') 
				timeDiff = (datetime.now() - datetimeObject).total_seconds() / 60.0
				if timeDiff <= updateTime:
					results.append({'Date': r[0], 'Room': r[1], 'Remarks': r[2].rstrip("\n")})

		# Upload results to Google Sheet 
		if len(results) > 0:
			requests.post(
				"https://sheet.best/api/sheets/e4d92608-bec0-46f4-b43e-1d558e790c28/tabs/Checkout Log",
				json = results
			)
		print("CHECKOUT data entry uploaded: " + str(len(results)))	

		# Locate System Log Data from Directory
		results = []
		fileName = dayString + ' system.log'
		directory = systemLogPath + fileName

		with open('01-12-2020 system.log') as f:
			lines = f.readlines()[1:]
			for line in lines:
				r = line.split("	")
				# append data within 5 min 
				datetimeObject = datetime.strptime(r[0], '%m/%d/%Y %I:%M:%S %p') 
				timeDiff = (datetime.now() - datetimeObject).total_seconds() / 60.0
				if timeDiff <= updateTime:				
					results.append({'Date': r[0], 'Status': r[1], 'Message': r[2].rstrip("\n")})

		# Upload results to Google Sheet 
		if len(results) > 0:
			requests.post(
				"https://sheet.best/api/sheets/e4d92608-bec0-46f4-b43e-1d558e790c28/tabs/System Log",
				json = results
			)
		print("SYSTEM LOG data entry uploaded: " + str(len(results)))



		# Program stops for 5 min then re-run 
		time.sleep(60*updateTime)

except KeyboardInterrupt:
	# press CTRL + C to pause program
	pass

