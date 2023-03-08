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

def selectFileFromRoot():
    try:
        os.path.exists('./payload')
    except:
        print("Payload folder not found\nCreating payload folder...\n\n")
        os.mkdir('./payload')
        selectFileFromRoot()

def spamTextsFromFile():
    print('''This option will print every line as a message that is in a file under payload folder of the project\nYou need to select the payload file first''')
    selectFileFromRoot()
    f=open("./payload/texts" , 'r',encoding="utf8")
    for x in f:
        pyautogui.typewrite(x)
        time.sleep(0.2)
        pyautogui.press("enter")


def spamTextsFromInput():
    f=open("./payload/texts" , 'r',encoding="utf8")
    for x in f:
        pyautogui.typewrite(x)
        time.sleep(0.2)
        pyautogui.press("enter")

def main():
    intro()
    opt = inputOpt('''[0] Spam texts from text file\n[1] Spam texts from input\n\n''')
    if opt == 0:
        spamTextsFromFile()
    elif opt == 1:
        spamTextsFromInput()


if __name__ == "__main__":
    main()