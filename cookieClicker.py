import pyautogui

#pyautogui.displayMousePosition()

pyautogui.PAUSE = 0.00001
pyautogui.moveTo(x=149,y=439)

counter = 0

while pyautogui.position() == (149, 439):
    pyautogui.click()
    counter += 20
    print("Remaining clicks to upgrades: ", 2000000 - counter)
    if counter % 2000000 == 0:
        #pyautogui.click(x=674,y=121)
        pyautogui.click(x=876,y=231)
        pyautogui.click(x=888,y=298)
        pyautogui.click(x=884,y=354)
        counter = 0
        pyautogui.moveTo(x=149,y=439)