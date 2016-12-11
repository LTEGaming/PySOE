import time
import random
def cls():
    for i in range(200):
        print("")

def cool():
    wn = random.randrange(0,21)
    if wn == 1:
        return "█                Now under New Management!               █" #Avg line to line distance: 56
    elif wn == 2:
        return "█                         Kappa!                         █" #Eventually I will fix the spacing.
    elif wn == 3:
        return "█                 Now with more sayings!                 █"
    elif wn == 4:
        return "█                       Plot twist!                      █"
    elif wn == 5:
        return "█      Totally not a virus, Trust me i'm a dolphin!      █"
    elif wn == 6:
        return "█                      Now On GitHub!                    █"
    elif wn == 7:
        return "█                       Unsupported!                     █"
    elif wn == 8:
        return "█            01110111 01101111 01110111 00100001         █"
    elif wn == 9:
        return "█                    >Install Gentoo!                    █"
    elif wn == 10:
        return "█                 Welcome to the botnet!                 █"
    elif wn == 11:
        return "█               Now with Blast Processing!               █"
    elif wn == 12:
        return "█      Your version of Flash Player is out of date!      █"
    elif wn == 13:
        return "█                  Uses UTF-8 Encoding!                  █"
    elif wn == 14:
        return "█                    No Easter Eggs!                     █"
    elif wn == 15:
        return "█Pleasehelpmeivebeentrappedwritingwittylinesforthepastmon█"
    elif wn == 16:
        return "█                     Ignore that!                       █"
    elif wn == 17:
        return "█                  Made With GameMaker!                  █"
    elif wn == 18:
        return "█   I'm really hoping that SOEvm will be finished soon   █"
    elif wn == 19:
        return "█        EOF inside string starting at line 891743       █"
    elif wn == 20:
        return "█             Everything probably still works!           █"
    else:
        return "█                     Unimplemented!                     █"
    
def load():
    cls()
    print("▄████████████████████████████████████████████████████████▄")
    print("█▀                                                      ▀█")  
    print("█                        PySOE                           █")
    print("█     (Python Simulated Operating System Enviroment)     █")
    print("█                       v0.02c                           █")
    print("█                 Updated on 12/11/16                    █")
    print(cool())
    print("█▄                                                      ▄█")
    print("▀████████████████████████████████████████████████████████▀")
    for i in range(7):
        print("")
    funct()
        
def funct():
    func = input()
    if func == "-listcommands" or func == "-help":
        print("-listcommands: Lists Commands")
        print("-help: Lists Commands")
        print("-time: Shows System Time")
        print("-ver or -version: Shows OS version")
        print("-print or -pr: Prints to display")
        print("-prog or -programs: Lists all available integrated programs")
        print("-ext or -extras: Extra side commands")
        print("")
        funct()
    elif func == "-time":
        print(time.asctime())
        print("")
        funct()
    elif func == "-ver" or func == "-version":
        print("PY OS v0.02c Created on 12/11/16")
        print("")
        funct()
    elif func == "-print" or func == "-pr":
        print1 = input("-pr: ")
        print(print1)
        print("")
        funct()
    elif func == "-prog" or func == "-programs":
        print("")
        print("Your installed programs are:")
        print("-soegraph: Primitive Graphing Program")
        print("-soevm: Python Virtual Machine for PySOE")
        print("-soecalc: Primitive Calculator Program")
        print("")
        print("Run a program? Y/N")
        print("")
        progprompt = input(">")
        if progprompt == "y" or progprompt == "Y":
            print("") 
            print("Input a program name.")
            prog = input(">")
            print("Now Loading",prog)
            print("Unimplemented.")
            funct()
        elif progprompt == "n" or progprompt == "N":
            print("")
            funct()
        else:
            print("Unsupported command!")
            funct()
    elif func == "-ext" or func == "-extras":
        print("")
        print("Extra commands are:")
        print("-beep: Beep")
        print("-his or -history: History of PYOS")
        print("")
        funct()
    elif func == "-his" or func == "-history":
        print("")
        print("          The History of PySOE (Python Simulated Operating System Environment)")
        print("")
        print("-------------------------------------------------------------------------------------------")
        print(" The first beginnings of PySOE started somewhere around October of 2015")
        print(" The first version didn't have much, just a fake login screen and")
        print(" a fake loading screen. There were only three commands. These commands inclue")
        print(" -help, -commands, and -ver. Those were all carried over. This program was")
        print(" started in my High School's Computer Science club while I was bored")
        print(" This 'OS' is heavily inspired by DOS, PC-DOS, and MS-DOS which is very")
        print(" evident by my functions that I have made. Most of them come from various")
        print(" DOS'. The first program written for PySOE was 'PYGraph' by Carson Goodwin")
        print(" which was not originally written for PySOE, but was adapted after v0.02c was")
        print(" published to GitHub. This is the most important parts of the whole history of PySOE.")
        print(" Hopefully many changes will come to this, most likely repurposing this High School Project")
        print("")
        print("-------------------------------------------------------------------------------------------")
        funct()
    else:
        print("bad sytnax")
        print("")
        funct()
        
load()
