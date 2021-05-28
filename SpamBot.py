import pyautogui, time
time.sleep(5)
f=open("texts" , 'r')
for x in f:
    pyautogui.typewrite(x)
    time.sleep(0.3)
    pyautogui.press("enter")



