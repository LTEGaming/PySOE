import time
import random
import soecalc
import soevm
import soegraph
def cls():
    for i in range(200):
        print("")

def cool():
    wn = random.randrange(0,20)
    if wn == 1:
        return "█                Now under New Management!               █" #Avg line to line distance: 56
    elif wn == 2:
        return "█                         Kappa!                         █" 
    elif wn == 3:
        return "█                 Now with more sayings!                 █"
    elif wn == 4:
        return "█                       Plot twist!                      █"
    elif wn == 5:
        return "█      Totally not a virus, Trust me i'm a dolphin!      █"
    elif wn == 6:
        return "█      Totally not a virus, Trust me i'm a dolphin!      █"
    elif wn == 7:
        return "█      Totally not a virus, Trust me i'm a dolphin!      █"
    elif wn == 8:
        return "█      Totally not a virus, Trust me i'm a dolphin!      █"
    elif wn == 9:
        return "█      Totally not a virus, Trust me i'm a dolphin!      █"
    elif wn == 10:
        return "█      Totally not a virus, Trust me i'm a dolphin!      █"
    elif wn == 11:
        return "█      Totally not a virus, Trust me i'm a dolphin!      █"
    elif wn == 12:
        return "█      Totally not a virus, Trust me i'm a dolphin!      █"
    elif wn == 13:
        return "█      Totally not a virus, Trust me i'm a dolphin!      █"
    elif wn == 14:
        return "█      Totally not a virus, Trust me i'm a dolphin!      █"
    elif wn == 15:
        return "█      Totally not a virus, Trust me i'm a dolphin!      █"
    elif wn == 16:
        return "█      Totally not a virus, Trust me i'm a dolphin!      █"
    elif wn == 17:
        return "█      Totally not a virus, Trust me i'm a dolphin!      █"
    elif wn == 18:
        return "█      Totally not a virus, Trust me i'm a dolphin!      █"
    elif wn == 19:
        return "█      Totally not a virus, Trust me i'm a dolphin!      █"
    else:
        return "█                     Unimplemented!                     █"
    
def load():
    cls()
    print("▄████████████████████████████████████████████████████████▄")
    print("█▀                                                      ▀█")  
    print("█                        PySOE                           █")
    print("█     (Python Simulated Operating System Enviroment)     █")
    print("█                        v0.02                           █")
    print("█                  Updated on 12/9/16                    █")
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
        print("-beep: Beep")
        print("-ext or -extras: Extra side commands")
        print("-his or -history: History of PYOS")
        print("")
        funct()
    elif func == "-time":
        print(time.asctime())
        print("")
        funct()
    elif func == "-ver" or func == "-version":
        print("PY OS v0.01 Created on 10/14/16")
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
        print("-pygraph or -soegraph: Primitive Graphing Program")
        print("-pyvm or -soevm: Python Virtual Machine for PySOE")
    elif func == "-his" or func == "-history":
        print("")
        print("          The History of PySOE (Python Simulated Operating System Environment)")
        print("")
        print("--------------------------------------------------------------------------------------")
        print(" The first beginnings of PySOE started somewhere around October of 2015")
        print(" The first version didn't have much, just a fake login screen and")
        print(" a fake loading screen. There were only three commands. These commands inclue")
        print(" -help, -commands, and -ver. Those were all carried over. This program was")
        print(" started in my High School's Computer Science club while I was bored")
        print(" This 'OS' is heavily inspired by DOS, PC-DOS, and MS-DOS which is very")
        print(" evident by my functions that I have made. Most of them come from various")
        print(" DOS'. The first program written for PySOE was 'PYGraph' by Carson Goodwin")
        print(" which was not originally written for PySOE, but was adapted after v0.2 was")
        print(" published to GitHub. This is the most important parts of the whole history of PySOE.")
        print(" Hopefully many changes will come to this, most likely repurposing this High School Project")
        print("")
        print("--------------------------------------------------------------------------------------")
        funct()
    else:
        print("bad sytnax")
        print("")
        funct()
        
load()
