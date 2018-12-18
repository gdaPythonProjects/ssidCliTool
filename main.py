import http_helper
import convert
import sys


if len(sys.argv)==5:
	
	latrange1 = float(sys.argv[1])
	latrange2 = float(sys.argv[2])
	longrange1 = float(sys.argv[3])
	longrange2 = float(sys.argv[4])
	
	http_client = http_helper.HTTP_Helper("credentials.txt")
	content=http_client.GetListOfWiFi(latrange1,latrange2,longrange1,longrange2)	

	converter = convert.Convert()
	listOfWiFiNames = converter.JsonListOfWiFiToListOfWiFiNames(content)

	for element in listOfWiFiNames:
		print(element)
			
elif len(sys.argv)==2:

	print("funcja chwilowo niedostepna- w trakcie budowy")
	
else:
	print("podano nieprawidlowa liczbe parametrow")
	print()
	print("program oferuje 2 opcje")
	print()
	print("w pierwszej opcji wyswielta nazwy sieci Wi-Fi na podstawie wprowadzonych wspolrzednych geograficznych : latrange1 latrange2 longrange1 longrange2 ")
	print()
	print("w drugiej opcji wyswietla lokalizacje sieci Wi-Fi na podstawie wprowadzonej nazwy sieci")