from pip._internal import main as pipmain
import site

def install(package):
    pipmain(['install', package])
    
if 'pynput' not in site.getsitepackages() or 'colorama' not in site.getsitepackages() or 'keyboard' not in site.getsitepackages():
    install('colorama')
    install('keyboard')
    install('pynput')
    print(site.getsitepackages())
    
from pynput.keyboard import Listener
from time import sleep as sl, sleep
from colorama import Fore as col
from threading import Thread
from random import choice
from re import T
import keyboard
import glob
import sys
import os

def main():
    passWheelState0 = ("╔▷ New Password    \n╠▷ Get Password    \n╠▷ Delete Password \n╠▷ Edit            \n╠▷ All Passwords   \n╠▷ Credits         \n╚▷ Quit            ")
    passWheelState1 = ("╔▶ New Password    \n╠▷ Get Password    \n╠▷ Delete Password \n╠▷ Edit            \n╠▷ All Passwords   \n╠▷ Credits         \n╚▷ Quit            ")
    passWheelState2 = ("╔▷ New Password    \n╠▶ Get Password    \n╠▷ Delete Password \n╠▷ Edit            \n╠▷ All Passwords   \n╠▷ Credits         \n╚▷ Quit            ")
    passWheelState3 = ("╔▷ New Password    \n╠▷ Get Password    \n╠▶ Delete Password \n╠▷ Edit            \n╠▷ All Passwords   \n╠▷ Credits         \n╚▷ Quit            ")
    passWheelState4 = ("╔▷ New Password    \n╠▷ Get Password    \n╠▷ Delete Password \n╠▶ Edit            \n╠▷ All Passwords   \n╠▷ Credits         \n╚▷ Quit            ")
    passWheelState5 = ("╔▷ New Password    \n╠▷ Get Password    \n╠▷ Delete Password \n╠▷ Edit            \n╠▶ All Passwords   \n╠▷ Credits         \n╚▷ Quit            ")
    passWheelState6 = ("╔▷ New Password    \n╠▷ Get Password    \n╠▷ Delete Password \n╠▷ Edit            \n╠▷ All Passwords   \n╠▶ Credits         \n╚▷ Quit            ")
    passWheelState7 = ("╔▷ New Password    \n╠▷ Get Password    \n╠▷ Delete Password \n╠▷ Edit            \n╠▷ All Passwords   \n╠▷ Credits         \n╚▶ Quit            ")

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
                    elif keymath >= 8:
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
                        print(col.WHITE +passWheelState7)
                        keymath = 7
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
                    else:
                        print(col.RED + "WARNING: CRITCAL ERR OCCURED, RETURNING TO ORIGIN STATE.")
                        reline()
                        print(col.WHITE +passWheelState1)
                        keymath = 0
                        sl(0.2)
                if keyboard.is_pressed('enter'):
                    reline()
                    if keymath <= 1:
                        wait()#IMPORTANT!! This makes sure that the actually important input doesnt register '' as the full input.
                        newPassword()
                        renew = 1                        
                        sl(0.5)
                        pass
                    elif keymath == 2:
                        wait()
                        getPassword()
                        renew = 1
                        sl(0.5)
                        continue
                    elif keymath == 3:
                        wait()
                        deletePassword()
                        renew = 1
                        sl(0.5)
                        continue
                    elif keymath == 4:
                        wait()
                        editAny()
                        renew = 1
                        sl(0.5)
                        continue
                    elif keymath == 5:
                        wait()
                        showAllPasswords()
                        renew = 1
                        sl(0.5)
                    elif keymath == 6:
                        wait()
                        credits()
                        renew = 1
                        sl(0.5)
                    elif keymath == 7:
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
            #scroll wheel

#PROGRAM'S DOWN HERE============================================================================================================================================
#PROGRAM'S DOWN HERE============================================================================================================================================
#===============================================================================================================================================================
#DEFINITIONS UP HERE============================================================================================================================================
#DEFINITIONS UP HERE============================================================================================================================================

def newPassword():
    UDFP = os.path.dirname(os.path.abspath(__file__))
    reline()
    while True:
        print("\033\r[FWhat site do you need a password for?\n")
        newPassname = input().strip().lower() #name of the new password

        charAmount = len(newPassname)

        if charAmount < 2:#use a longer name man
            print("Please use a longer name!")
            sl(1)
            reline()
            continue
        else:
            break
        
    if not os.path.exists(UDFP + "\\PassHolder\\"):
        passwordHolderDir = UDFP + "\\PassHolder\\"
        os.makedirs(passwordHolderDir)
    
    if os.path.isfile(UDFP + "/PassHolder/" + newPassname + ".txt"):#does the file already exist?
        print(col.RED + "WARNING!", end='')
        alrExists = input(col.WHITE + " File alread exists! Do you wish to overwrite it? ")
        if alrExists.lower().strip() in ["y", "yes"]:
            print(col.YELLOW + "Overwriting", end='')
            sys.stdout.flush()
            for i in range(3):
                sl(0.5)
                print('.', end='', flush=True)
            sl(0.75)
            print(col.GREEN + " Overwritten." + col.WHITE)
    else:
        pass
    
    with open(UDFP + "\\PassHolder\\" + newPassname + ".txt", 'w') as newPass:#make the file
    #new file

        listKeyboard = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n',
        'o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F',
        'G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X',
        'Y','Z','1','2','3','4','5','6','7','8','9','0','!','@','#','$','%','^',
        '&','*','(',')','_','+','{','}','|',':','"','<','>','?','-','=','[',']',
        ';',',','.','/','`','~']#full keyboard list
        #char list

        listAlphabetlowercase = ['a','b','c','d','e','f','g','h','i','j',
        'k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']#lowercase alphabet
        
        listAlphabetuppercase = ['A','B','C','D','E','F','G','H','I','J',
        'K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']#uppercase alphabet

        listNumber = ['1','2','3','4','5','6','7','8','9','0']#0 9 list

        listSpecial = ['!','@','#','$','%','^','&','*','(',')','_','+','{',
        '}','|',':','"','<','>','?','-','=','[',']',';',',','.','/','`','~']#special char list
        #req char list

        newPass.write(choice(listKeyboard))
        newPass.write(choice(listAlphabetuppercase))
        newPass.write(choice(listKeyboard))
        newPass.write(choice(listNumber))
        newPass.write(choice(listKeyboard))
        newPass.write(choice(listSpecial))
        newPass.write(choice(listKeyboard))
        #req char gen
    
        for i in range(43):
            newPass.write(choice(listKeyboard))
            newPass.close

    with open(UDFP + "/PassHolder/" + newPassname + ".txt", 'r') as newPassread:
        [print("\nName:", newPassname, "\nPassword:", line.strip(), "\n") for line in newPassread.readlines()]
        input("Enter to Continue ")
        newPassread.close()
            #Generator

def getPassword(): 
    UDFP = os.path.dirname(os.path.abspath(__file__))
    reline()

    #imports

    while True:
        filePassname = input("Enter a password name, or enter EXIT to return to the menu.\n\n").strip().lower()

        if os.path.isfile(UDFP + "/PassHolder/" + filePassname + ".txt"):
            with open(UDFP + "/PassHolder/" + filePassname + ".txt", 'r') as filePass:
                [print("\nName:", filePassname, "\nPassword:", line.strip()) for line in filePass.readlines()]
                filePass.close()
                input("Enter to Continue")
                break

        else:
            print("\nSorry, I couldn't find this file because it either doesn't exist, or isnt in my directory. Please try again, or press N to exit.\n\n")
            continue

def deletePassword():
    UDFP = os.path.dirname(os.path.abspath(__file__))
    reline()

    while True:
        print("\nChoose what file to delete.\n")
        deleteInput = input().strip().lower()

        sure = ["Y", "y"]
        unsure = ["N", "n"]

        if os.path.isfile(UDFP + "/PassHolder/" + deleteInput + ".txt"):
            print("are you sure you want to delete", deleteInput + "? Just remember that this is", col.RED + "PERMANENT", col.WHITE + "and", col.RED + "CANNOT BE UNDONE", col.WHITE + ". (y/n)\n")
            sureCheck = input().strip().lower()
            if sureCheck in sure:
                print("\ndeleting file", end='')
                sys.stdout.flush()
                for i in range(3):
                    sl(0.75)
                    print('.', end='', flush=True)
                sl(0.5)
                print("\n")
                os.remove(UDFP + "/PassHolder/" + deleteInput + ".txt")
                print(col.GREEN + "The file has been deleted.\n" + col.WHITE)
                sl(1)
                reline()
                break

            elif sureCheck in unsure:
                reline()
                print("Your files are safe with me, come again!")
                sl(1)
                reline()
                break

            else:
                print("Sorry, I don't recognize that character. Please try again.")
                sl(1)
                reline()
                continue

        else:
            print("\nSorry, I couldn't find", deleteInput + ", please try again.")
            sl(1)
            reline()
            continue

    #pass print 

def editAny():
    UDFP = os.path.dirname(os.path.abspath(__file__))
    reline()
    x = 0

    passwordChosen = False
    nameChosen = False
    
    print("Do you want to change a Password, or a Name?\n")
    print("╔▶ Password")
    print("╚▷ Name    ")

    while passwordChosen == False and nameChosen == False:
        if keyboard.is_pressed('down'):
            reline()
            x += 1
            if x == 0:
                print("Do you want to change a Password, or a Name?\n")
                print("╔▶ Password")
                print("╚▷ Name    ")
                sl(0.2)
            elif x == 1:
                print("Do you want to change a Password, or a Name?\n")
                print("╔▷ Password")
                print("╚▶ Name    ")
                sl(0.2)
            elif x >= 2:
                print("Do you want to change a Password, or a Name?\n")
                print("╔▶ Password")
                print("╚▷ Name    ")
                x=0
                sl(0.2)
            else:
                print(col.RED + "WARNING: CRITCAL ERR(2) OCCURED, RETURNING TO ORIGIN STATE. (press enter to continue)")
        if keyboard.is_pressed('up'):
            reline()
            x -= 1
            if x == 0:
                print("Do you want to change a Password, or a Name?\n")
                print("╔▶ Password")
                print("╚▷ Name    ")
                sl(0.2)
            elif x == 1:
                print("Do you want to change a Password, or a Name?\n")
                print("╔▷ Password")
                print("╚▶ Name    ")
                sl(0.2)
            elif x <= 0:
                print("Do you want to change a Password, or a Name?\n")
                print("╔▷ Password")
                print("╚▶ Name    ")
                x=1
                sl(0.2)
            else:
                print(col.RED + "WARNING: CRITCAL ERR(2) OCCURED, RETURNING TO ORIGIN STATE. (press enter to continue)")
        if keyboard.is_pressed('enter'):
            wait()
            if x == 0:
                passwordChosen = True
                break
            elif x == 1:
                nameChosen = True
                break
        continue

    if nameChosen:

        while True:
            print("Enter a password's name to change it.\n")

            oldname = input().strip().lower()

            old = os.path.join(UDFP, 'PassHolder', oldname + '.txt')

            print(old)

            if os.path.isfile(old):
                print("Enter the new name.\n")
                newname = input().strip().lower()
                new = os.path.join(UDFP, 'PassHolder', newname + '.txt')
                os.rename(old, new)
                break
            else:
                print("\nPlease enter a valid Password Name.\n")
                continue

    
    elif passwordChosen:

        print("\nChoose which password to edit. (Q to quit)")

        while True:
            editInput = input().strip().lower()

            kill = ["Q", "q"]

            if editInput in kill:
                print("yeah I aint code that yet")
        
            else:
                if os.path.isfile(UDFP + "/PassHolder/" + editInput + ".txt"):
                    with open(UDFP + "/PassHolder/" + editInput + ".txt", 'r') as editor:
                        print("\nCurrent Password\n|\n|\nV\n")
                        [print(line.strip(), "\n") for line in editor.readlines()]
                        editor.close
                        with open(UDFP + "/PassHolder/" + editInput + ".txt", 'w') as edited:
                            print("New Password\n|\n|\nV\n")
                            spirit = input().strip()
                            edited.write(spirit)
                            print("\n")
                            edited.close
                            break
                else:
                    print("I couldn't find this file. Please choose a valid file (Q to quit)\n")
                    continue

def showAllPasswords():
    UDFP = os.path.dirname(os.path.abspath(__file__))
    reline()

    for fileName_relative in glob.glob(UDFP + "/PassHolder/*.txt",recursive=True):
        fileName_absolute = os.path.basename(fileName_relative)
        print("\n " + fileName_absolute)
    input("Press enter to continue")

def credits():
    reline()
    prynt("Credits:")
    sl(0.5)
    prynt("Rexgram (Dev)")
    sl(0.75)
    prynt("Stack Overflow (Questions & Help)")
    sl(0.75)
    prynt("Python Discord (Questions & Help)")
    sl(1)
    reline()

'''def settings():
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
                continue'''

def prynt(str):
   for c in str + '\n':
     sys.stdout.write(c)
     sys.stdout.flush()
     sl(3./90)

def reline():
    os.system('cls' if os.name == 'nt' else 'clear')

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

def wait():
    sl(0.1)
    input()
main()
