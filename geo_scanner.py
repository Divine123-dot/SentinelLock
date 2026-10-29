#urillid.requests we import urillib.request because when a person want a raw location of the devices's ip address it will go to URL on internet and take it.

import urllib.request

#because whe the server send raw data into plain text formatted in json , it let the python translate the module into dictionary so it can help to get items like ip, location and city

import json

#importing subprocess module, let the python app ask the linux to scan the nearby Wi-Fi routers and MAC addresses even when the internet is offline

import subprocess

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

#the scan nearby wifi function scan all the routers around that place where the device is.

def scan_nearby_wifi():
        

        try:


            #the subprocess.check_output runs nmcli to pick the wifi name(SSID), router MAC address(BSSID) , and SIGNAL 
            
            raw_output =subprocess.check_output(["nmcli", "-t", "-f","SSID,BSSID,SIGNAL", "dev", "wifi"], text=True, timeout=5)

            return raw_output.replace("\\:", ":").strip().splitlines()


        except Exception as e:

            return [f"Wi-Fi scan failed: {str(e)}"]



#we are testing get_location_data()

if __name__ == "__main__":

    location_result = get_location_data()

    print(location_result)


#we are testing the scan_nearby_wifi function to see any available router are the place

    wifi_result = scan_nearby_wifi()
    
    for router in wifi_result:
         

        print(f" - {router}")


