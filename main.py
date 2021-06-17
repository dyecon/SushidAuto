# coding: utf-8
import sys

###Check if required modules are available
try:
    import PIL
    print("Module 'PIL': Available")
except:
    print("\n Module 'PIL' is unavailable. You can install it with: pip install pillow")
    sys.exit(1)
try:
    import pyocr
    print("Module 'pyocr': Available")
except:
    print("\n Module 'pyocr' is unavailable. You can install it with: pip install pyocr")
    sys.exit(1)
try:
    import cv2
    print("Module 'cv2': Available")
except:
    print("\n Module 'cv2' is unavailable. You can install it with: pip install opencv-python")
    sys.exit(1)
try:
    import pyautogui
    print("Module 'pyautogui': Available")
except:
    print("\n Module 'pyautogui' is unavailable. You can install it with: pip install pyaotogui")
    sys.exit(1)

tools = pyocr.get_available_tools()
if len(tools) >= 1:
    print("Module 'Tesseract-OCR': Available \n")
else:
    print("\n Tesseract-OCR is not installed, or configured incorrectly.")
    print("Windows: Download from https://github.com/UB-Mannheim/tesseract/wiki  \n and add 'C:\Progam Files\Tesseract-OCR' to PATH.")
    print("macOS: Install with 'brew install tesseract")
    sys.exit(1)


import moji
import posCheck as pc
import pyautogui as pa
import time

import random

#Check position
difficulty = input("Select difficulty: \n[0] Easy \n[1] Medium \n[2] Hard")
dimensions = input("Select display dimensions: \n[0] 2560x1600 \n[1] 2560x1440 \n[2] 1920x1080 \n[3] Mac 2560x1600")
locationList = pc.check(difficulty, dimensions)
if locationList == None:
    print ("The specified difficulty/resolution does not exist, or the game window is hidden.")
    time.sleep(2)
    sys.exit(1)
print (locationList)

start = time.time()
pa.mouseDown(x = locationList[0], y = locationList[1], button = 'left')
pa.mouseUp()
pa.typewrite(" ", interval = 0.0)
nowtime = time.time()
while True:
    if time.time() - nowtime > 1.5:
        break
i = 0
while True:
    if time.time() - nowtime > 300:
        break
    print(i)
    img = pa.screenshot(
        imageFilename="screenshot" + str(i) + ".png",    # 保存先ファイル名
        region=(locationList[0], locationList[1], locationList[2], locationList[3])    # 撮影範囲(x,y,width,height)
    )
    string = moji.moji("screenshot" + str(i))
    pa.typewrite(string, interval = random.uniform(0.02,0.075))
    print(string)
    nowtime1 = time.time()
    while True:
        if time.time() - nowtime1 > 0.25:
            break
    i += 1