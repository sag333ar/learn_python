import json

jsonData = '{ "name": "Sagar", "company": "TechCoderLabz", "employeeId": 700, "skills": ["sdds", "sdsd", "gfgfg"] }'

parsedJson = json.loads(jsonData)

print(parsedJson["name"])
print(parsedJson["employeeId"])
print(parsedJson["skills"])

pythonDictionary = {
  "companyName":  "TechCoderLabz",
  "tutorName": "Sagar",
  "employeeId": 700
}

toJsonString = json.dumps(pythonDictionary)

print(toJsonString)