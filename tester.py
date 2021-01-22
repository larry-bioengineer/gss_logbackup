# code tester 

# import requests
# from datetime import datetime, date, timedelta
# import time
# import config
# from pathlib import Path

# updateTime = 5.0

# timeDiff = datetime.now() + timedelta(minutes=updateTime)
# timeDiff1 = datetime.now() + timedelta(days=1)
# timeDiff1 = timeDiff1.replace(hour=0, minute=0, second=0, microsecond=0)

# print(timeDiff)
# print(timeDiff1)

# print((timeDiff1 - timeDiff).total_seconds())

# import sys
# sys.
# sys.path.append('/Users/lokyiuto/Downloads')


# from xml.dom import minidom
# mydoc = minidom.parse("/Users/lokyiuto/Downloads/Main.config")

# items = mydoc.getElementsByTagName('appSettings')

# print('\nAll attributes:')
# for elem in items:
#     print(elem.attributes['name'].value)


# import xml.etree.ElementTree as ET
# # import xmltodict
# import json


# parser = ET.parse("Main.config")
# myroot = parser.getroot()

import xmltodict
import pprint
import json
mydict = xmltodict.parse("Main")
print(mydict)