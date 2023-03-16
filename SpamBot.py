import pyautogui, time
import os

banner = r'''
 _________                             __________             __   
 /   _____/ ______   _____      _____   \______   \   ____   _/  |_ 
 \_____  \  \____ \  \__  \    /     \   |    |  _/  /  _ \  \   __\
 /        \ |  |_> >  / __ \_ |  Y Y  \  |    |   \ (  <_> )  |  |  
/_______  / |   __/  (____  / |__|_|  /  |______  /  \____/   |__|  
        \/  |__|          \/        \/          \/                  
__________         ________                                  __     
\______   \___.__. \______ \   _______  ______________      |__|    
 |    |  _<   |  |  |    |  \_/ __ \  \/ /\_  __ \__  \     |  |    
 |    |   \\___  |  |    `   \  ___/\   /  |  | \// __ \_   |  |    
 |______  // ____| /_______  /\___  >\_/   |__|  (____  /\__|  |    
        \/ \/              \/     \/                  \/\______|    
'''

def intro():
    print(banner)
    print("SpamBot is running...")
    print("Press Ctrl-C to quit.\n\n")
    print("Select option ...\n")

def inputOpt(x):
    try:
        return int(input(x))
    except:
        print('\nINVALID INPUT GIVEN\nExiting the program....')
        exit()

import time

def countdown(seconds):
    for i in range(seconds, 0, -1):
        print(i)
        time.sleep(1)
    print("Spamming Started...")

def spamTextsFromFile():
    print('''This option will print every line as a message that is in a file "payload" file at project root\nyou will have 10s to put your cursor onto the text field.''')
    f=open("./payload" , 'r',encoding="utf8")
    countdown(10)
    for x in f:
        pyautogui.typewrite(x)
        pyautogui.press("enter")
    print("Spamming Completed...")


def spamTextsFromInput():
    text = input("Write the text which you want to repeatedly spam and press enter. You will have 10s to put your cursor onto the text field.\n")
    times = inputOpt("How many times you want to spam the text?\n")
    countdown(10)
    for x in range(times):
        pyautogui.typewrite(text)
        pyautogui.press("enter")
    print("Spamming Completed...")

def main():
    intro()
    opt = inputOpt('''[0] Spam texts from text file\n[1] Spam texts from input\n\n''')
    print('TO STOP THE PROGRAM, MOVE THE CURSOR OF YOUR MOUSE TO THE TOP LEFT CORNER OF THE SCREEN\n')
    if opt == 0:
        spamTextsFromFile()
    elif opt == 1:
        spamTextsFromInput()


if __name__ == "__main__":
    main()
