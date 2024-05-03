import requests
import urllib.parse
from apikey import API_TOKEN

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = API_TOKEN


while True:
    orig = input("Starting location : ")
    if orig == "quit" or orig == "q":
        break
    dest = input("Destination : ")
    if dest == "quit" or dest == "q":
        break

    url = main_api + \
        urllib.parse.urlencode(
            {"key": key, "from": orig, "to": dest, "unit": "k", "locale": "ru_RU"})

    json_data = requests.get(url).json()
    json_status = json_data['info']['statuscode']

    print(f"URL : {url}")

    if json_status == 0:
        print(f"API Status : {str(json_status)}  = A successful route call.\n")

    else:
        json_status != 0
        print("Error")
