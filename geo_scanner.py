#urillid.requests we import urillib.request because when a person want a raw location of the devices's ip address it will go to URL on internet and take it.

import urllib.request

#because whe the server send raw data into plain text formatted in json , it let the python translate the module into dictionary so it can help to get items like ip, location and city

import json

# get location data function helps to check if there is any machine internet connetion and we use try to check if the wifi is disconnected or the browser is down

def get_location_data():

    try:    

        #url is box name that hold the website we are visiting

        url = "https://ipinfo.io/json"

        with urllib.request.urlopen(url, timeout=5) as response:

        #we read and translate the servers's reply into dictionary by using jsonloads module, response, and utf-8

            data = json.loads(response.read().decode("utf-8"))

            #we use .get to get data that are available in the function. when the python ask for ip adress the get will go in the dictionary to get it 


            return {
                "ip": data.get("ip", "Unknown"),

                "city": data.get("city", "Unknown"),

                "region":data.get("region", "Unknown"),

                "country": data.get("country", "Unknown"),
                "loc": data.get("loc", "Unknown"),
                "org": data.get("org", "Unknown")


            }

            #except as Expection as e: when the system cannot find the internet available instead of producing error it will show unknow or offline and it change the error into a string

    except Exception as e:
        return {
            "ip": "Offline / Unknown",
            "error": str(e)
        }

#we are testing get_location_data()

if __name__ == "__main__":

    location_result = get_location_data()

    print(location_result)




