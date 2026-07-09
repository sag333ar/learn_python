import json

jsonData = '{ "name": "Sagar", "company": "TechCoderLabz", "employeeId": 700 }'

parsedJson = json.loads(jsonData)

print(parsedJson["name"])
print(parsedJson["employeeId"])

toJson = {
  "companyName":  "TechCoderLabz",
  "tutorName": "Sagar",
  "employeeId": 700
}

toJsonString = json.dumps(toJson)

print(toJsonString)