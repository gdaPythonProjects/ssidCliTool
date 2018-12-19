import json

class Convert:
	def __init__(self):
		pass
		
	def JsonToDict(self,data):
		return json.loads(data)
		
	def JsonListOfWiFiToListOfWiFiNames(self,jsonData):
		dictionary = self.JsonToDict(jsonData)
		listOfNames = []
		i=0
		while i < len(dictionary["results"]):
			listOfNames.append((dictionary["results"][i]["ssid"]))
			i=i+1
		return listOfNames
		
	def JsonListOfWiFiToListOfWiFiAddresses (self,jsonData):
		dictionary = self.JsonToDict(jsonData)
		listOfAddresses = []
		i=0
		while i < len(dictionary["results"]):
			address = str(dictionary["results"][i]["road"]) + " " + str(dictionary["results"][i]["housenumber"]) + " " + str(dictionary["results"][i]["city"]) + " " + str(dictionary["results"][i]["region"]) + " " + str(dictionary["results"][i]["country"])
			listOfAddresses.append(address)
			i=i+1
		return listOfAddresses