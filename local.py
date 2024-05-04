import requests
import urllib.parse
from apikey import API_TOKEN

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = API_TOKEN


while True:
    print("Wellcome to my Navigator")

    print("You need write 2 parameters for create routes.")

    print("All time you can exit just write ( quit ) or ( q )")
    print(50 * "=")
    orig = input("Starting location : ")
    if orig == "quit" or orig == "q":
        break
    dest = input("Destination : ")
    if dest == "quit" or dest == "q":
        break

    url = main_api + \
        urllib.parse.urlencode(
            {"key": key, "from": orig, "to": dest, "unit": "k"})

    json_data = requests.get(url).json()
    json_status = json_data['info']['statuscode']
    json_messages = json_data['info']['messages']

    if json_status == 0:
        print(75 * '==')
        print(f"URL address     : {url}")
        print(75 * '==')
        print(
            f"API Status is   : {json_status} successful route call.\n")

        print(f"Directions from : {orig}")
        print(f"Directions to   : {dest}")
        print(f"Trip duration   : {json_data['route']['formattedTime']} time")
        print(f"Kilometers      : {json_data['route']['distance']} Km")
        print(f"Fuel used       : {json_data['route']['distance']*10/100} ltr")
        print(60 * "==")

        for gps in json_data['route']['legs'][0]['maneuvers']:
            print((gps['narrative']) +
                  " --- " + (str("{:.2f}".format(gps['distance']*1.58) + "km)")))
            print(60 * "==")

    elif json_status == 402:
        print(40 * '**')
        print(
            f"Status coode : {json_status} Invalid user imputs for one or both locations.")
        print(f"MapQuest message {json_messages}")
        print(40 * '**')
        break
    else:
        print(40 * '**')
        print(f"MapQuest message {json_messages}")
        print(f"Status code: {json_status} Refer to.")
        print("URL for help :" +
              "https://developer.mapquest.com/documentation/directions-api/status-codes")
        print(40 * '**')
