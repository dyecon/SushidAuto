import pyautogui

#OpenCV must be installed for the "confidence" parameter to take effect
def check(difficulty, dimensions):
    if (difficulty == "0"):
        if dimensions == "0": #2560x1600
            selectionLocation = pyautogui.locateOnScreen('images/textReadArea/2560x1600_easy.png', confidence = 0.8)
            return(selectionLocation)
        if dimensions == "1": #2560x1440
            selectionLocation = pyautogui.locateOnScreen('images/textReadArea/2560x1440_easy.png', confidence = 0.8)
            return(selectionLocation)
        if dimensions == "2": #1920x1080
            selectionLocation = pyautogui.locateOnScreen('images/textReadArea/1920x1080_easy.png', confidence = 0.8)
            return(selectionLocation)
        if dimensions == "3": #1920x1080
            selectionLocation = pyautogui.locateOnScreen('images/textReadArea/2560x1600_easy_mac.png', confidence = 0.8)
            return(selectionLocation)
    
    
    if (difficulty == "1"):
        if dimensions == "0": #2560x1600
            selectionLocation = pyautogui.locateOnScreen('images/textReadArea/2560x1600_medium.png', confidence = 0.8)
            return(selectionLocation)
        if dimensions == "1": #2560x1440
            selectionLocation = pyautogui.locateOnScreen('images/textReadArea/2560x1440_medium.png', confidence = 0.8)
            return(selectionLocation)
        if dimensions == "2": #1920x1080
            selectionLocation = pyautogui.locateOnScreen('images/textReadArea/1920x1080_medium.png', confidence = 0.8)
            return(selectionLocation)
        if dimensions == "3": #1920x1080
            selectionLocation = pyautogui.locateOnScreen('images/textReadArea/2560x1600_medium_mac.png', confidence = 0.8)
            return(selectionLocation)

    
    if (difficulty == "2"):
        if dimensions == "0": #2560x1600
            selectionLocation = pyautogui.locateOnScreen('images/textReadArea/2560x1600_hard.png', confidence = 0.8)
            return(selectionLocation)
        if dimensions == "1": #2560x1440
            selectionLocation = pyautogui.locateOnScreen('images/textReadArea/2560x1440_hard.png', confidence = 0.8)
            return(selectionLocation)
        if dimensions == "2": #1920x1080
            selectionLocation = pyautogui.locateOnScreen('images/textReadArea/1920x1080_hard.png', confidence = 0.8)
            return(selectionLocation)
        if dimensions == "3": #1920x1080
            selectionLocation = pyautogui.locateOnScreen('images/textReadArea/2560x1600_hard_mac.png', confidence = 0.8)
            return(selectionLocation)
    