import urllib.request

class HTTP_Helper:
	def __init__(self,credentialsPath):
		f = open(credentialsPath,"r")
		self.authorization = f.read()
		
	def Get(self,url):
		req = urllib.request.Request(url)
		
		req.add_header('Authorization',self.authorization)
		contents = urllib.request.urlopen(req)
		return contents.read().decode('UTF-8')
		
	def GetListOfWiFi(self,latrange1,latrange2,longrange1,longrange2):
		url="https://api.wigle.net/api/v2/network/search?onlymine=false&first=0&latrange1="
		url=url+str(latrange1)+"&latrange2="+str(latrange2)+"&longrange1="+str(longrange1)+"&longrange2="+str(longrange2)+"&freenet=false&paynet=false"
		return self.Get(url)
		
