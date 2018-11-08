import http_helper
import convert

http_client = http_helper.HTTP_Helper("credentials.txt")
content=http_client.GetListOfWiFi(54.3545,54.3570,18.6404,18.649)

file = open("content.html","w")
file.write(content)

converter = convert.Convert()
jsonDict = converter.JsonToDict(content)


