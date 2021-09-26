import pyautogui, time  # Importing pyautogui and time modules

time.sleep(3)           # Delaying the program for 5s, this is the time when you have to click on the textbox of whatsapp/ anyother messaging app

f=open("./texts" , 'r',encoding="utf8")   # Here the path and name of the file (example "texts" or "./TonyKakkar/AnySongName") is given and 'r' means read

for x in f:                     # A for loop to print all the words
    pyautogui.typewrite(x)
    # time.sleep(0.2)             # Time delay given between sending of two consecutive messages if this time is very small your system may hang
    pyautogui.press("enter")    