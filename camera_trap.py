#os let python manage the incidents or folder path
import os

#cv2 is python library for controlling the webcam and take the picture 
import cv2

#datetime generate the exact timestamp for the photo filename it shows year, month, date, hour, second
from datetime import datetime 


#capture_intruder_photo works when someone entered three times wrong pin and the system take the picture of them. the fucnction_caputure intruder_photo takes the photo of intruder and hide the evendence inside the user's devices.

def capture_intruder_photo(output_dir="incidents"):
    try:

        #os.makedirs tells the system to check if the incidents folder exists in the device, if it does not exist it telly python to create one
        os.makedirs(output_dir, exist_ok=True)

        #craeting a unique timestamp and joining it with folder path

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        file_path = os.path.join(output_dir, f"intruder_{timestamp}.jpg")

        #the camera = cv2.VideoCapture(0) turns on your laptop's built in webcam and cameras are numbered from zero

        camera = cv2.VideoCapture(0)

        #we use if statement if someone is using sentinelLock on desktop without camera or another system has turn it off. the system return none

        if not camera.isOpened():
            return None

        #the camera.read it take the photo and camera.release it closes the camera in the milisecond so that if someone who to use a camera will be able to use it.

        success, frame = camera.read()
        camera.release()


        #the cv2.imwrite saves the photo to file_path

        if success:
            cv2.imwrite(file_path, frame)
            return file_path
        return None

    except Exception as e:
        return None


#we are testing capture_intruder_photo()

if __name__ == "__main__":

    saved_photo = capture_intruder_photo()

    if saved_photo:
        print(f"Intruder photo saved at: {saved_photo}")

    else:
        print("Camera capture failed.")    
