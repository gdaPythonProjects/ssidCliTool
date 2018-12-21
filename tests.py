import unittest
import http_helper
import os.path
import convert

class Test_WiFi(unittest.TestCase):

	def test_check_auth_file_exists(self):	
		file_exsists = os.path.isfile("credentials.txt")
		self.assertEqual(file_exsists,1)
		
	def test_credentials_valid(self):
	
		http_client = http_helper.HTTP_Helper("credentials.txt")
		json_with_WiFi = str(http_client.GetListOfWiFi(12,13,15,16))
		self.assertTrue(json_with_WiFi.find('success":true') > -1)
	
	def test_convert_json_to_WiFilists(self):
		
		sample_data =  '{"success":true,"totalResults":1,"search_after":100862458,"first":1,"last":1,"resultCount":1,"results":[{"trilat":54.35592270000000070240275817923247814178466796875,"trilong":18.64847565000000173540684045292437076568603515625,"ssid":"natek","qos":0,"transid":"20100622-00000","firsttime":"2010-06-22T19:00:00.000Z","lasttime":"2010-06-22T16:00:00.000Z","lastupdt":"2010-09-14T01:00:00.000Z","housenumber":"7","road":"Jana Heweliusza","city":"Gdańsk","region":"pomorskie","country":"PL","netid":"00:1C:F0:7F:04:A8","name":null,"type":"infra","comment":null,"wep":"W","channel":2,"bcninterval":0,"freenet":"?","dhcp":"?","paynet":"?","userfound":false,"encryption":"wpa"}]}'

		converter = convert.Convert()
		listOfNames = converter.JsonListOfWiFiToListOfWiFiNames(sample_data)
		self.assertEqual(len(listOfNames),1)
		self.assertIn('natek',listOfNames)
		
	
	
	def test_check_WiFi_list_of_Gdansk(self):
	
		latrange1 = 54.253
		latrange2 = 54.4691
		longrange1 = 18.2927
		longrange2 = 19.0873
		
		http_client = http_helper.HTTP_Helper("credentials.txt")
		json_with_WiFi = http_client.GetListOfWiFi(latrange1,latrange2,longrange1,longrange2)
		converter = convert.Convert()
		listOfNames = converter.JsonListOfWiFiToListOfWiFiNames(json_with_WiFi)
		self.assertTrue(len(listOfNames) > 0)
		
	
	def test_convert_json_to_ListOfAddresses(self):
		sample_data =  '{"success":true,"totalResults":1,"search_after":100862458,"first":1,"last":1,"resultCount":1,"results":[{"trilat":54.35592270000000070240275817923247814178466796875,"trilong":18.64847565000000173540684045292437076568603515625,"ssid":"natek","qos":0,"transid":"20100622-00000","firsttime":"2010-06-22T19:00:00.000Z","lasttime":"2010-06-22T16:00:00.000Z","lastupdt":"2010-09-14T01:00:00.000Z","housenumber":"7","road":"Jana Heweliusza","city":"Gdańsk","region":"pomorskie","country":"PL","netid":"00:1C:F0:7F:04:A8","name":null,"type":"infra","comment":null,"wep":"W","channel":2,"bcninterval":0,"freenet":"?","dhcp":"?","paynet":"?","userfound":false,"encryption":"wpa"}]}'
		
		converter = convert.Convert()
		listOfAddresses = converter.JsonListOfWiFiToListOfWiFiAddresses(sample_data)
		self.assertIn("Jana Heweliusza 7 Gdańsk pomorskie PL",listOfAddresses)
		self.assertTrue(len(listOfAddresses) == 1)
		
	def test_check_searching_for_WiFi_name(self):
	
		latrange1 = 54.253
		latrange2 = 54.4691
		longrange1 = 18.2927
		longrange2 = 19.0873
		
		http_client = http_helper.HTTP_Helper("credentials.txt")
		json_with_Gdansk_WiFi = http_client.GetListOfWiFi(latrange1,latrange2,longrange1,longrange2)
		converter = convert.Convert()
		listOfNames = converter.JsonListOfWiFiToListOfWiFiNames(json_with_Gdansk_WiFi)
		
		json_with_some_WiFi_name = http_client.GetListOfWiFiBySSID(listOfNames[0])
		listOfAddresses = converter.JsonListOfWiFiToListOfWiFiAddresses(json_with_some_WiFi_name)
		self.assertTrue(len(listOfAddresses) > 0)
	

if __name__ == '__main__':
	unittest.main()