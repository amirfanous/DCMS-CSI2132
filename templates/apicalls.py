import urllib.request
import json

def getResponse(url):
    operUrl = urllib.request.urlopen(url)
    if(operUrl.getcode()==200):
        data = operUrl.read()
        jsonData = json.loads(data)
    else:
        print("Error receiving data", operUrl.getcode())
    return jsonData

def apicalls():
    urlData = "http://127.0.0.1:5000/api/branches"
    jsonData = getResponse(urlData)
    # print the state id and state name corresponding
    
    for i in jsonData:
        print(f'Branch ID:  {i["branch_id"]} , Branch Location : {i["branch_location"]}')