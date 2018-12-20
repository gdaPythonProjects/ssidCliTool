import unittest
import http_helper
import os.path

class Test_WiFi(unittest.TestCase):

	def test_check_auth_file_exists(self):	
		file_exsists = os.path.isfile("credentials.txt")
		self.assertEqual(file_exsists,1)
		
	def test_credentials_valid(self):
	
		http_client = http_helper.HTTP_Helper("credentials.txt")
		json_with_WiFi = str(http_client.GetListOfWiFi(12,13,15,16))
		self.assertTrue(json_with_WiFi.find('success":true') > -1)
		
	#def test_check_WiFi_list_of_Gdansk(self):
	#	self.assertEqual(1,0)
		
	
	

if __name__ == '__main__':
	unittest.main()