
import urllib.request as req
url="https://padax.github.io/taipei-day-trip-resources/taipei-attractions.json"
with req.urlopen(url) as response:
    data=response.read().decode("utf-8")

import json
json_array = json.loads(data)

import os
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__))) 

with open(os.path.join(__location__, 'data.txt'), "w", encoding = "UTF-8") as textFile:
   for item in json_array["result"]["results"]:
        print(item["file"].split("http"))
        record = item['stitle'] + "," + item["longitude"] + "," + item["latitude"] + "," + "http" + item["file"].split("http")[1]
        textFile.write(record + "\n")
        
        
