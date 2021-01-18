# Larry To
# Created on: 11/26/2020
# To extrat file from user chosen directory and upload to a google sheet 

# Libraries
import requests
from datetime import datetime, date, timedelta
import time
import config
from pathlib import Path

# Parameters
programPath = "C:\\Program Files (x86)\\Golden News Enterprises Ltd\\Guest Service Station\\log\\"
# programPath = "/Users/lokyiuto/Documents/CEPO/HSX/GuestServiceStation/LogBackUp/log/"
checkoutLogPath = programPath + "Checkout log\\"
systemLogPath = programPath + "System log\\"
feedbackLogPath = programPath + "Feedback log\\"
subcribeLogPath = programPath + "Subscribe log\\"
updateTime = 60.0; # in minutes 


try: 
	while True:

		today = date.today()
		dayString = today.strftime("%m-%d-%Y")
		print("Periodic Data Backup for Guest Service Station at " + datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
		print("Current Update Period is " + str(updateTime) + " minutes")

		# Locate Checkout Data from Directory---------------- 
		results = []
		fileName = dayString + ' checkout.log'
		directory = checkoutLogPath + fileName
		
		if not Path(directory).is_file():
			print("no file found for CHECKOUT LOG Data")
			
		else: 
			with open(directory) as f:
				lines = f.readlines()[1:]
				for line in lines:
					r = line.split("	")

					# append data within 5 min 
					datetimeObject = datetime.strptime(r[0], '%m-%d-%Y %I:%M:%S %p') 
					timeDiff = (datetime.now() - datetimeObject).total_seconds() / 60.0
					if timeDiff <= updateTime:
						results.append({'Datetime': r[0], 'Room': r[1], 'Remarks': r[2].rstrip("\n")})

			# Upload results to Google Sheet 
			if len(results) > 0:
				requests.post(
					config.googleSheetAPI + "/tabs/CheckoutLog",
					headers={
						'X-Api-Key': config.serverAPIKey
					},
					json = results
				)
			print("CHECKOUT data entry uploaded: " + str(len(results)))	

		# Locate System Log Data from Directory------------
		results = []
		fileName = dayString + ' system.log'
		directory = systemLogPath + fileName

		if not Path(directory).is_file():
			print("no file found for SYSTEM LOG Data")
		else:
			with open(directory) as f:
				lines = f.readlines()[1:]
				for line in lines:
					r = line.split("	")
					# append data within update time
					datetimeObject = datetime.strptime(r[0], '%m-%d-%Y %I:%M:%S %p') 
					timeDiff = (datetime.now() - datetimeObject).total_seconds() / 60.0
					if timeDiff <= updateTime:				
						results.append({'Datetime': r[0], 'Status': r[1], 'Message': r[2].rstrip("\n")})

			# Upload results to Google Sheet 
			if len(results) > 0:
				requests.post(
					config.googleSheetAPI + "/tabs/SystemLog",
					headers={
						'X-Api-Key': config.serverAPIKey
					},
					json = results
				)	
			print("SYSTEM LOG data entry uploaded: " + str(len(results)))

					# Locate Subscribe Log Data from Directory------------
		results = []
		fileName = 'subscription.log'
		directory = subcribeLogPath + fileName

		if not Path(directory).is_file():
			print("no file found for Subscription LOG Data")
		else:
			with open(directory) as f:
				lines = f.readlines()[1:]
				for line in lines:
					r = line.split("	")
					# append data within update time
					datetimeObject = datetime.strptime(r[0], '%m-%d-%Y %I:%M:%S %p') 
					timeDiff = (datetime.now() - datetimeObject).total_seconds() / 60.0
					if timeDiff <= updateTime:				
						results.append({'Date': r[0], 'Firstname': r[1], 'Lastname': r[2], 'Prefix': r[3],
							'Email': r[4], 'DiscountSubscription': r[5], 'PromotionSubscription': r[6],
							'SuggestionSubscription': r[7], 'BlogSubscription': r[8].rstrip("\n")})

			# Upload results to Google Sheet 
			if len(results) > 0:
				requests.post(
					config.googleSheetAPI + "/tabs/Subscription",
					headers={
						'X-Api-Key': config.serverAPIKey
					},
					json = results
				)	
			print("Subscription LOG data entry uploaded: " + str(len(results)))

					# Locate Feedback Log Data from Directory------------
		results = []
		fileName = 'feedback.log'
		directory = feedbackLogPath + fileName

		if not Path(directory).is_file():
			print("no file found for Feedback LOG Data")
		else:
			with open(directory) as f:
				lines = f.readlines()[1:]
				for line in lines:
					r = line.split("	")
					# append data within update time
					datetimeObject = datetime.strptime(r[0], '%m-%d-%Y %I:%M:%S %p') 
					timeDiff = (datetime.now() - datetimeObject).total_seconds() / 60.0
					if timeDiff <= updateTime:				
						results.append({'Date': r[0], 'Firstname': r[1], 'Lastname': r[2], 'Prefix': r[3],
							'Email': r[4], 'FilterType': r[5],'Issue': r[6].rstrip("\n")})

			# Upload results to Google Sheet 
			if len(results) > 0:
				requests.post(
					config.googleSheetAPI + "/tabs/CustomerFeedback",
					headers={
						'X-Api-Key': config.serverAPIKey
					},
					json = results
				)	
			print("Feedback LOG data entry uploaded: " + str(len(results)))

		# Program stops for X min then re-run-------------
		print("")
		print("Waiting for next Data Backup...")

		nextUpdateT = datetime.now() + timedelta(minutes=updateTime)
		nextMidNight = datetime.now() + timedelta(days=1)
		nextMidNight = nextMidNight.replace(hour=0, minute=0, second=0, microsecond=0)
		# if update time is after midnight, adjust the update time to right before midnight
		if (nextUpdateT - nextMidNight).total_seconds() > 0:
			time.sleep((nextMidNight - datetime.now()).total_seconds()-1)
		
		else:
			time.sleep(60*updateTime)


except KeyboardInterrupt:
	# press CTRL + C to pause program
	pass

