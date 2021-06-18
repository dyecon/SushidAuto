# SushidAuto（スシドート）
SUSHIDA Automation with Python

**WARNING**: Use this program at your own risk.

## Overview
SushidAuto uses OCR to directly capture & analyze text from the game. Pyautogui is used to automatically type the words shown in the game.


## Prerequisites
Python3 must be installed on your PC.

Install these Python modules before you run the program:
* PIL:  `pip install pillow`
* PyOCR: `pip install pyocr`
* cv2: `pip install opencv-python`
* PyAutoGui: `pip install pyautogui` (`pip3` for macOS/Linux; additional instructions for Linux [here](https://pyautogui.readthedocs.io/en/latest/install.html))
* Tesseract-OCR
    * **Windows**: Download the installer from 
    https://github.com/UB-Mannheim/tesseract/wiki
    and add "C:\Program Files\Tesseract-OCR" to PATH.
    * **macOS**: Install with `brew install tesseract` 
    * **Ubuntu 20.04**: Install with `sudo apt install tesseract-ocr`

| OS           | Supported Resolution(s) | Difficulty         |
|--------------|-------------------------|--------------------|
| macOS (beta) | 2560×1600               | Easy, Medium, Hard |
| Windows      | 2560×1600               | Easy, Hard         |
|              | 2560×1440               | Easy, Medium, Hard |
|              | 1920×1080               | Easy, Medium, Hard |

## Running the script
From the directory in which the files are saved, run the command:

`python main.py`


## Known Issues:
* macOS users may need to manually start the game
* Script may be slow in macOS