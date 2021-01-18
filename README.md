# Periodic Log Backup for Guest Service Station 

## Purpose
The goal of this program is to periodically upload a program to a google sheet. The program is set to run every 5 minute until users stop the program. 

## To-Do
1. allow users to input directory 
2. automatically update file name for extracting system log 

## How to perform periodic data backup
1. Add API key and endserver URL in a config file 
2. Run `main.py` in terminal. 
3. Log/Data will be uploaded to a Google Drive Server
4. Press CTR + C to stop the program. 
5. Check Google sheet if the data has added.

## Data Schema
```
+------------------+-------------------------+
| table_name       | fields                  |
+------------------+-------------------------+
| CheckoutLog      | Datetime                |
|                  | Room No                 |
|                  | Remarks                 |
+------------------+-------------------------+
| SystemLog        | Datetime                |
|                  | Status                  |
|                  | Message                 |
+------------------+-------------------------+
| CustomerFeedback | Datetime                |
|                  | Firstname               |
|                  | Lastname                |
|                  | Prefix                  |
|                  | Email                   |
|                  | FilterType              |
|                  | Issue                   |
+------------------+-------------------------+
| Subscription     | Datetime                |
|                  | Firstname               |
|                  | Lastname                |
|                  | Prefix                  |
|                  | Email                   |
|                  | DiscountSubscription    |
|                  | PromotionSubscription   |
|                  | SuggestionSubscription  |
|                  | BlogSubscription        |
+------------------+-------------------------+
```

## How to access the data from Google Driver Server
To read all data from the API, make `GET` requests to the server REST API. 
1. Add API key to a `config.py` file 
2. (Optional) Run `read.py` in terminal for testing. 
2. Read Rows 
```python
# Install python "requests" module to use this
import requests

# Parsed Format
sysLog = requests.get(config.googleSheetAPI + "/tabs/CheckoutLog", 
			headers={
			'X-Api-Key': '<API Key Here>'
		})
```

which API will return a status code. 
```
| 200 - OK                           | Everything worked as expected.                                                                            |
| 400 - Bad Request                  | The request was unacceptable, often due to missing a required parameter or permission to the spreadsheet. |
| 401 - Authentication Failed        | Incorrect authentication credentials                                                                      |
| 402 - Payment Required             | This operation is not allowed in your current plan.                                                       |
| 403 - Forbidden                    | You do not have permission to perform this action.                                                        |
| 404 - Not Found                    | The requested resource doesn't exist.                                                                     |
| 405 - Method Not Allowed           | When calling a endpoint using a not registered method. Ex: POST for the search endpoint                   |
| 402 - Payment required             | You already used all of your plan's requests this month.                                                  |
| 500, 502, 503, 504 - Server Errors | Something went wrong on Sheet.Best's end, we will fix it.                                                 |
```

data can be access through `.text`
```
$ python3 read.py 
[{"Datetime":"11/21/2020 11:41:25","Room":"101","Remarks":null},{"Datetime":"11/21/2020 12:01:13","Room":"205","Remarks":null},{"Datetime":"11/22/2020 0:00:00","Room":"304","Remarks":null},{"Datetime":"11/21/2020 11:41:25","Room":"101","Remarks":"remark1"},{"Datetime":"11/21/2020 12:01:13","Room":"102","Remarks":"remark2"},{"Datetime":"11/21/2020 3:11:19","Room":"807","Remarks":"remark3"},{"Datetime":"11/21/2020 11:41:25","Room":"101","Remarks":"remark1"},{"Datetime":"11/21/2020 12:01:13","Room":"102","Remarks":"remark2"},{"Datetime":"11/21/2020 3:11:19","Room":"807","Remarks":"remark3"}
```

2. (Advance) Filter Rows
Data can filtered using exact values and wildcard matching. (Note: date time cannot be filtered at this stage and so users will need to filter the datetime after requesting all the data) However, users can still filter the data by room number, status (system statuses) and message (system messages). For example, we can perform a `REQUEST` for Room 101 checkout by
```python
import requests 

# Getting rows with 101 as "Room"
sysLog = requests.get(config.googleSheetAPI + "/tabs/CheckoutLog/Room/101", 
		headers={
			'X-Api-Key': config.serverAPIKey
		})
```
