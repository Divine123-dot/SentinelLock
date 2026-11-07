#os library check if the log file exists on the saystem before trying to read

import os

#time library pauses between checks using the method time.sleep when watching a live log file so the script wouldnt  interupted the compuer cpu
import time

#the function scan_log-for_intruder when it wants to inspect it takes the file path of log

def scan_log_for_intruders(log_path: str):

    #when check if log_path exists on computure because we want to know if its there so the system would not crash when it does not exist

    if not os.path.exists(log_path):
        print(f"Log file not found: {log_path}")

        return[]

    #failure_keywords list is a list that contain warning phases linux writes when a user enters a wrong password

    failure_keywords = ["Failed password", "authentication failure", "Invalid user"]

    #suspicious_events list is a list that store the failure keyword when a user tries to log in

    suspicious_events = []

    try:

        #we use r mode inside try block because linux log files are plain text records(unlike binary photos)

        with open(log_path, "r") as log_file:

            # we loop through every line because we want python to read line by line from top to bottom

            for line in log_file:

                for keyword in failure_keywords:
                    if keyword in line:
                        suspicious_events.append(line.strip())

                        break #we break once the python finds the matchong keyword and stops checking and move to the next line 
     #we return the list of cught intruder lines or an empty list reading fails

        
        return suspicious_events
    except Exception as e:

        print(f"Error reading log file: {e}")

        return[]


#we are creating a simple log file to test the scanner

if __name__ == "__main__":

    os.makedirs("incidents", exist_ok=True)
    test_log = "incidents/sample_auth.log"

    #we are writhing 1 normal login line and 2 intruder lines into the test file

    with open (test_log, "w") as f:
        f.write("Nov 07 19:00:01 ubuntu asshd: Accepted password for divine\n")

        f.write("Nov 07 19:01:15 ubuntu asshd: Failed password for divine\n")

        f.write("Nov 7 19:02:00 ubuntu asshd: Invalid user hacker from 192.168.1.50\n")

        #we scan log intruder because if the function scan_log_intruders works it ignore the line one in test_log and catch only line 2 and 3

    detected = scan_log_for_intruders(test_log)

    print(f"Found {len(detected)} suspicious events:")

    for event in detected:

        print(f" -> {event}")



    