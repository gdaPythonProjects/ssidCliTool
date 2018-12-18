import json

class Convert:
	def __init__(self):
		pass
		
	def JsonToDict(self,data):
		return json.loads(data)
		
	def JsonListOfWiFiToListOfWiFiNames(self,jsonData):
		dictionary = self.JsonToDict(jsonData)
		listOfNames=[]
		i=0
		while i < len(dictionary["results"]):
			listOfNames.append((dictionary["results"][i]["ssid"]))
			i=i+1
		return listOfNames
		
		