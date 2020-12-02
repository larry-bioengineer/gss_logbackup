# Periodic Log Backup for Guest Service Station 

## Purpose
The goal of this program is to periodically upload a program to a google sheet. The program is set to run every 5 minute until users press CTR + C. 

## To-Do
1. allow users to input directory 
2. automatically update file name for extracting system log 

## How to perform periodic data backup
1. Add API key in a config file 
2. Run main.py in terminal. 
3. Log/Data will be uploaded to a Google Drive Server

## Data Schema
```
	+--------------+----------+
	| table_name   | fields   |
	+--------------+----------+
	| CheckoutLog  | Datetime
	|              | Room No  |
	|              | Remarks  | 
	+--------------+----------+
	| SystemLog    | Datetime |
	|              | Status   | 
	|              | Message  | 
	+--------------+----------+	
```

## How to access the data from Google Driver Server
To read all data from the API, make `GET` requests to the server REST API. 
1. Add API key to a `config.py` file 
2. Read Rows 
```python
# Install python "requests" module to use this
import requests

# Parsed Format
requests.get("https://sheet.best/api/sheets/cf969697-682a-40e3-bad4-d54803eeeacf")
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
2. (Advance) Filter Rows

