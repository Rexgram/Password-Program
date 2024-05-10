from pynput.keyboard import Listener
from colorama import Fore as col
from threading import Thread
from time import sleep as sl, sleep
from random import choice
from re import T
import keyboard
import glob
import sys
import os

def main():
    passWheelState0 = ("╔▷ New Password    \n╠▷ Get Password    \n╠▷ Delete Password \n╠▷ Edit            \n╠▷ All Passwords   \n╠▷ Credits         \n╠▷ Settings       \n╚▷ Quit            ")
    passWheelState1 = ("╔▶ New Password    \n╠▷ Get Password    \n╠▷ Delete Password \n╠▷ Edit            \n╠▷ All Passwords   \n╠▷ Credits         \n╠▷ Settings       \n╚▷ Quit            ")
    passWheelState2 = ("╔▷ New Password    \n╠▶ Get Password    \n╠▷ Delete Password \n╠▷ Edit            \n╠▷ All Passwords   \n╠▷ Credits         \n╠▷ Settings       \n╚▷ Quit            ")
    passWheelState3 = ("╔▷ New Password    \n╠▷ Get Password    \n╠▶ Delete Password \n╠▷ Edit            \n╠▷ All Passwords   \n╠▷ Credits         \n╠▷ Settings       \n╚▷ Quit            ")
    passWheelState4 = ("╔▷ New Password    \n╠▷ Get Password    \n╠▷ Delete Password \n╠▶ Edit            \n╠▷ All Passwords   \n╠▷ Credits         \n╠▷ Settings       \n╚▷ Quit            ")
    passWheelState5 = ("╔▷ New Password    \n╠▷ Get Password    \n╠▷ Delete Password \n╠▷ Edit            \n╠▶ All Passwords   \n╠▷ Credits         \n╠▷ Settings       \n╚▷ Quit            ")
    passWheelState6 = ("╔▷ New Password    \n╠▷ Get Password    \n╠▷ Delete Password \n╠▷ Edit            \n╠▷ All Passwords   \n╠▶ Credits         \n╠▷ Settings       \n╚▷ Quit            ")
    passWheelState7 = ("╔▷ New Password    \n╠▷ Get Password    \n╠▷ Delete Password \n╠▷ Edit            \n╠▷ All Passwords   \n╠▷ Credits         \n╠▶ Settings       \n╚▷ Quit            ")
    passWheelState8 = ("╔▷ New Password    \n╠▷ Get Password    \n╠▷ Delete Password \n╠▷ Edit            \n╠▷ All Passwords   \n╠▷ Credits         \n╠▷ Settings       \n╚▶ Quit            ")

    Thread(target=security).start()

    keymath = 0
    renew = 0

    print(passWheelState0)

    while True:
        if renew >= 1:
            reline()
            print(passWheelState0)
            keymath = 0
            renew = 0

        else:
            #try:  # used try so that if program is shite program doesn't crash instantly
                if keyboard.is_pressed('down'):
                    keymath += 1
                    if keymath == 1:
                        reline()
                        print(col.WHITE +passWheelState1)
                        sl(0.2)
                    elif keymath == 2:
                        reline()
                        print(col.WHITE +passWheelState2)
                        sl(0.2)
                    elif keymath == 3:
                        reline()
                        print(col.WHITE +passWheelState3)
                        sl(0.2)
                    elif keymath == 4:
                        reline()
                        print(col.WHITE +passWheelState4)
                        sl(0.2)
                    elif keymath == 5:
                        reline()
                        print(col.WHITE +passWheelState5)
                        sl(0.2) 
                    elif keymath == 6:
                        reline()
                        print(col.WHITE +passWheelState6)
                        sl(0.2) 
                    elif keymath == 7:
                        reline()
                        print(col.WHITE +passWheelState7)
                        sl(0.2)
                    elif keymath == 8:
                        reline()
                        print(col.WHITE +passWheelState8)
                        sl(0.2)
                    elif keymath >= 9:
                        reline()
                        print(col.WHITE +passWheelState1)
                        keymath = 1
                        sl(0.2)
                    else:
                        print(col.RED + "WARNING: CRITCAL ERR OCCURED, RETURNING TO ORIGIN STATE.")
                        reline()
                        print(col.WHITE +passWheelState1)
                        keymath = 1
                        sl(0.2)
                    
                if keyboard.is_pressed('up'):
                    keymath -= 1
                    if keymath <= 0:
                        reline()
                        print(col.WHITE +passWheelState8)
                        keymath = 8
                        sl(0.2)
                    elif keymath == 1:
                        reline()
                        print(col.WHITE +passWheelState1)
                        sl(0.2)
                    elif keymath == 2:
                        reline()
                        print(col.WHITE +passWheelState2)
                        sl(0.2)
                    elif keymath == 3:
                        reline()
                        print(col.WHITE +passWheelState3)
                        sl(0.2)
                    elif keymath == 4:
                        reline()
                        print(col.WHITE +passWheelState4)
                        sl(0.2)
                    elif keymath == 5:
                        reline()
                        print(col.WHITE +passWheelState5)
                        sl(0.2) 
                    elif keymath == 6:
                        reline()
                        print(col.WHITE +passWheelState6)
                        sl(0.2) 
                    elif keymath == 7:
                        reline()
                        print(col.WHITE +passWheelState7)
                        sl(0.2)
                    elif keymath == 8:
                        reline()
                        print(col.WHITE +passWheelState8)
                        sl(0.2)
                    else:
                        print(col.RED + "WARNING: CRITCAL ERR OCCURED, RETURNING TO ORIGIN STATE.")
                        reline()
                        print(col.WHITE +passWheelState1)
                        keymath = 0
                        sl(0.2)
                if keyboard.is_pressed('enter'):
                    reline()
                    if keymath <= 1:
                        newPassword()
                        renew = 1
                        
                        sl(0.5)
                        pass
                    elif keymath == 2:
                        getPassword()
                        renew = 1
                        
                        sl(0.5)
                        continue
                    elif keymath == 3:
                        deletePassword()
                        renew = 1
                        
                        sl(0.5)
                        continue
                    elif keymath == 4:
                        editAny()
                        renew = 1
                        
                        sl(0.5)
                        continue
                    elif keymath == 5:
                        showAllPasswords()
                        renew = 1
                        
                        sl(0.5)
                    elif keymath == 6:
                        settings()
                        renew = 1
                         
                        sl(0.5)
                    elif keymath == 7:
                        credits()
                        renew = 1
                        
                        sl(0.5)
                        continue 
                    elif keymath == 8:
                        os._exit(1)
                    else:
                        print(col.RED + "WARNING: CRITCAL ERR(1) OCCURED, RETURNING TO ORIGIN STATE. (press enter to continue)")
                        keyboard.wait('enter')
                        reline()
                        print(col.WHITE + passWheelState0)
                        keymath = 0
                        sl(0.5)
                            
            #except:
                #print(col.RED + "WARNING: CRITCAL ERR OCCURED, RETURNING TO ORIGIN STATE. (press enter to continue)")  # if program broke, this error will be thrown.
                #input()
                #reline()
                #print(col.WHITE + passWheelState0)
                #keymath = 0
                #sl(0.5)

            #continue
            #scroll wheel------------

#PROGRAM'S DOWN HERE============================================================================================================================================
#PROGRAM'S DOWN HERE============================================================================================================================================
#===============================================================================================================================================================
#DEFINITIONS UP HERE============================================================================================================================================
#DEFINITIONS UP HERE============================================================================================================================================

def newPassword():
    UDFP = os.path.dirname(os.path.abspath(__file__))
    input()#IMPORTANT!! This makes sure that the actually important input doesnt register '' as the full input.
    reline()
    while True:
        print("\033\r[FWhat site do you need a password for?\n")
        newPassname = input()#name of the new password

        charAmount = len(newPassname)

        if charAmount <= 1:#use a longer name man
            print("Please use a longer name!")
            sl(1)
            reline()
            continue
        else:
            print(end='')
    
        if os.path.isfile(UDFP + "/PassHolder/" + newPassname + ".txt"):#does the file already exist?
            print(col.RED + "WARNING!", end='')
            alrExists = input(col.WHITE + " File alread exists! Do you wish to overwrite it? ")
            if alrExists.lower() in ["y", "yes"]:
                print(col.YELLOW + "Overwriting", end='')
                sys.stdout.flush()
                for i in range(3):
                    sl(0.5)
                    print('.', end='', flush=True)
                sl(0.75)
                print(col.GREEN + " Overwritten." + col.WHITE)
        else:
            continue
        with open(UDFP + "\\PassHolder\\" + newPassname + ".txt", 'w') as newPass:#make the file
        #new file----------------

            listKeyboard = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n',
            'o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F',
            'G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X',
            'Y','Z','1','2','3','4','5','6','7','8','9','0','!','@','#','$','%','^',
            '&','*','(',')','_','+','{','}','|',':','"','<','>','?','-','=','[',']',
            ';',',','.','/','`','~']#full keyboard list
            #char-list----------------

            listAlphabetlowercase = ['a','b','c','d','e','f','g','h','i','j',
            'k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']#lowercase alphabet
            
            listAlphabetuppercase = ['A','B','C','D','E','F','G','H','I','J',
            'K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']#uppercase alphabet

            listNumber = ['1','2','3','4','5','6','7','8','9','0']#0-9 list

            listSpecial = ['!','@','#','$','%','^','&','*','(',')','_','+','{',
            '}','|',':','"','<','>','?','-','=','[',']',';',',','.','/','`','~']#special char list
            #req char list----------------

            newPass.write(choice(listKeyboard))
            newPass.write(choice(listAlphabetuppercase))
            newPass.write(choice(listKeyboard))
            newPass.write(choice(listNumber))
            newPass.write(choice(listKeyboard))
            newPass.write(choice(listSpecial))
            newPass.write(choice(listKeyboard))
            #req char gen----------------
        
            for i in range(43):
                newPass.write(choice(listKeyboard))
                newPass.close

        with open(UDFP + "/PassHolder/" + newPassname + ".txt", 'r') as newPassread:
            [print("\nName:", newPassname, "\nPassword:", line.strip(), "\n") for line in newPassread.readlines()]
            input("Enter to Continue-------------------------------------------")
            newPassread.close()
            
            break
            #Generator----------------

def getPassword(): 
    UDFP = os.path.dirname(os.path.abspath(__file__))
    input()

    #imports------------------

    while True:
        filePassname = input("Enter a password name, or press 'HOME' to return to the menu. ")

        if os.path.isfile(UDFP + "/PassHolder/" + filePassname + ".txt"):
            with open(UDFP + "/PassHolder/" + filePassname + ".txt", 'r') as filePass:
                [print("\nName:", filePassname, "\nPassword:", line.strip(), "\n--------------------------------------------------") for line in filePass.readlines()]
                filePass.close()
                break

        else:
            print("\nSorry, I couldn't find this file because it either doesn't exist, or isnt in my directory. Please try again, or press N to exit.\n---------------------------------------------------------------------------------------------------------------------------------\n")
            continue

def deletePassword():
    UDFP = os.path.dirname(os.path.abspath(__file__))

    while True:
        print("--------------------------------------------------\nChoose what file to delete.\n")
        deleteInput = input()

        sure = ["Y", "y"]
        unsure = ["N", "n"]

        if os.path.isfile(UDFP + "/PassHolder/" + deleteInput + ".txt"):
            print("are you sure you want to delete", deleteInput + "? Just remember that this is permanent. (y/n)\n")
            sureCheck = input()
            if sureCheck in sure:
                print("\ndeleting file", end='')
                sys.stdout.flush()
                for i in range(3):
                    sl(0.75)
                    print('.', end='', flush=True)
                sl(0.5)
                print("\n")
                os.remove(UDFP + "/PassHolder/" + deleteInput + ".txt")
                print("The file has been deleted.\n--------------------------------------------------\n\n\n\n\n\n\n\n")
                break

            elif sureCheck in unsure:
                print("Your files are safe with me, come again!\n\n\n\n\n\n\n\n")
                break

            else:
                print("Sorry, I don't recognize that character. Please try again.")
                continue

        else:
            print("\nSorry, I couldn't find", deleteInput + ", please try again.")
            continue

    #pass print---------------

def editAny():
    UDFP = os.path.dirname(os.path.abspath(__file__))
    split = "-"*56 + "\n"
    x = 0
    
    print(split + "Do you want to change a Password, or a Name?\n")

    if keyboard.is_pressed('down'):
        reline()
        x += 1
        if x == 0:
            print("╔▶ Password")
            print("╚▷ Name    ")
        elif x == 1:
            print("╔▷ Password")
            print("╚▶ Name    ")
        elif x >= 2:
            print("╔▶ Password")
            print("╚▷ Name    ")
        else:
            print(col.RED + "WARNING: CRITCAL ERR(2) OCCURED, RETURNING TO ORIGIN STATE. (press enter to continue)")
    if keyboard.is_pressed('up'):
        reline()
        x -= 1
        if x == 0:
            print("╔▶ Password")
            print("╚▷ Name    ")
        elif x == 1:
            print("╔▷ Password")
            print("╚▶ Name    ")
        elif x <= 0:
            print("╔▷ Password")
            print("╚▶ Name    ")
        else:
            print(col.RED + "WARNING: CRITCAL ERR(2) OCCURED, RETURNING TO ORIGIN STATE. (press enter to continue)")
    if dothething == 1:
        if x == 0:
            passwordChosen = True
        elif x == 1:
            nameChosen = True
    

    if nameChosen:

        while True:
            print(split + "Enter a password's name to change it.\n")

            oldname = input()

            old = os.path.join(UDFP, 'PassHolder', oldname + '.txt')

            print(old)

            if os.path.isfile(old):
                print(split + "Enter the new name.\n")
                newname = input()
                new = os.path.join(UDFP, 'PassHolder', newname + '.txt')
                os.rename(old, new)
                break
            else:
                print("\nPlease enter a valid Password Name.\n")
                continue

    
    elif passwordChosen:

        print("--------------------------------------------------------\nChoose which password to edit. (Q to quit)")

        while True:
            editInput = input()

            kill = ["Q", "q"]

            if editInput in kill:
                print("\n")
        
            else:
                if os.path.isfile(UDFP + "/PassHolder/" + editInput + ".txt"):
                    with open(UDFP + "/PassHolder/" + editInput + ".txt", 'r') as editor:
                        print("\nCurrent Password\n|\n|\nV\n")
                        [print(line.strip(), "\n--------------------------------------------------") for line in editor.readlines()]
                        editor.close
                        with open(UDFP + "/PassHolder/" + editInput + ".txt", 'w') as edited:
                            print("New Password\n|\n|\nV\n")
                            spirit = input()
                            edited.write(spirit)
                            print("--------------------------------------------------\n")
                            edited.close
                            break
                else:
                    print("I couldn't find this file. Please choose a valid file (Q to quit)\n")
                    continue

def showAllPasswords():
    UDFP = os.path.dirname(os.path.abspath(__file__))

    for fileName_relative in glob.glob(UDFP + "/PassHolder/*.txt",recursive=True):
        fileName_absolute = os.path.basename(fileName_relative)
        print("\n-" + fileName_absolute)
    print("","\n\n\n\n\n\n\n\n")

def credits():
    reline()
    prynt("Credits:")
    sl(0.1)
    prynt("Rexgram (Dev)")
    sl(0.2)
    prynt("Stack Overflow (Questions & Help)")
    sl(0.2)
    prynt("Python Discord (Questions & Help)")
    reline()
    sl(1.5)

def settings():
    while True:
        newPassLength = input("How long would you like your passwords? (Default is 50 chars)")
        if newPassLength.strip() in ['']:
            passLength = newPassLength.strip()
        else:
            passLength = newPassLength.strip()
            try:
                passLength = int(newPassLength)
            except TypeError:
                print("Please only use real numbers for the previous question.")
                continue


def prynt(str):
   for c in str + '\n':
     sys.stdout.write(c)
     sys.stdout.flush()
     sl(3./90)

def reline():
    for i in range(10):
        print("\033\r[F\x1B[K")
        print("\033\r[F\033\r[F\x1B[K")

def home():
    while True:
        if keyboard.is_pressed('Home'):
            break

def security():
    pressed_keys = set()

    def ear():
        def on_press(key):
            pressed_keys.add(key)

        def on_release(key):
            pressed_keys.discard(key)

        with Listener(on_press=on_press, on_release=on_release) as listener:
            listener.join()

    def count():
        y = 0
        while True:
            if len(pressed_keys) >= 1:
                y = 0
            sleep(1)
            y += 1
            if y >= 60:
                os._exit(1)

    Thread(target=ear).start()
    Thread(target=count).start()

main()