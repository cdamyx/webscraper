import json

#testDate = "01/01/2016 00:00"

with open('twitterData.json') as json_data:
    jsonData = json.load(json_data)

    for i in jsonData:
        #if i['date'] < testDate:
        print(i['date'])