import time
import random
def cls():
    for i in range(200):
        print("")

def cool():
    wn = random.randrange(0,27)
    if wn == 1:
        return "█                Now under New Management!               █" #Avg line to line distance: 56
    elif wn == 2:
        return "█                         Kappa!                         █" #Unfortunately, We're using prng to generate these "Random" numbers. Seems like we get the same number a couple times. 
    elif wn == 3:
        return "█                 Now with more sayings!                 █"
    elif wn == 4:
        return "█                      Plot twist!                       █"
    elif wn == 5:
        return "█      Totally not a virus, Trust me i'm a dolphin!      █"
    elif wn == 6:
        return "█                      Now On GitHub!                    █"
    elif wn == 7:
        return "█                       Unsupported!                     █"
    elif wn == 8:
        return "█          01110111 01101111 01110111 00100001           █"
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
    elif wn == 21:
        return "█Symmet---------------------|----------------------rical!█"
    elif wn == 22:
        return "█                IT'S SNOWING OUTSIDE GUYS!              █"
    elif wn == 23:
        return "█                     a day old meme                     █"
    elif wn == 24:
        return "█                    Oh, FiddleSticks!                   █"
    elif wn == 25:
        return "█                       @echo off                        █"
    elif wn == 26:
        return "█                     Coded in Batch!                    █"
    else:
        return "█                     Unimplemented!                     █"
    
def load():
    cls()
    print("▄████████████████████████████████████████████████████████▄")
    print("█▀                                                      ▀█")  
    print("█                       PySOE DEV                        █")
    print("█     (Python Simulated Operating System Enviroment)     █")
    print("█                         v0.03a                         █")
    print("█                   Updated on 12/11/16                  █")
    print(cool())
    print("█▄                                                      ▄█")
    print("▀████████████████████████████████████████████████████████▀")
    for i in range(7):
        print("")
    print("Type '-help' to get started.")
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
        print("-prog or -programs: Lists all available installed programs")
        print("-ext or -extras: Extra side commands")
        print("-inst or -install: Installs a new program into your program list.")
        print("")
        funct()
    elif func == "-time":
        print(time.asctime())
        print("")
        funct()
    elif func == "-inst" or func == "-install":
        print("")
        print("Welcome to the Program Installer.")
        print("")
        print("Please make sure you have the program you want to install in the same directory as pysoe_shell.py")
        print("")
        print("What is the name of the program you will install? (Case Sensitive!) or type 'Cancel to cancel.")
        print("")
        inst = input("-inst: ")
        if inst == "cancel" or inst == "Cancel":
            print()
            funct()
        else:
            f = open("progs.txt","a",encoding='utf-7')
            f.write("\n")
            f.write(inst)
            f.flush()
            print("")
            print("Completed Installation Successfully!")
            print("")
            funct()
    elif func == "-ver" or func == "-version":
        print("PySOE v0.03a Created on 12/11/16")
        print("")
        funct()
    elif func == "-print" or func == "-pr":
        print1 = input("-pr: ")
        print("")
        print(print1)
        print("")
        funct()
    elif func == "-prog" or func == "-programs":
        print("")
        print("Your installed programs are:")
        f = open("progs.txt")
        print(f.read())
        print("")
        print("Run a program? Y/N")
        print("")
        progprompt = input(">")
        if progprompt == "y" or progprompt == "Y":
            print("") 
            print("Input a program name (Case Sensitive) or type 'Cancel' to cancel.")
            prog = input(">")
            if prog == "cancel" or prog == "Cancel":
                funct()
            else:
                print("")
                print("Now Loading",prog)
                time.sleep(2)
                __import__(prog)
        elif progprompt == "n" or progprompt == "N":
            print("")
            funct()
        else:
            print("Unsupported command!")
            funct()
    elif func == "-ext" or func == "-extras":
        print("")
        print("Extra commands are:")
        print("-beep or -boop: Beep")
        print("-his or -history: History of PYOS")
        print("")
        funct()
    elif func == "-beep" or func == "-boop":
        import winsound
        print("")
        Freq = input("Enter Frequency in Hertz: ")
        Dur = input("Enter Length in Milliseconds: ")
        winsound.Beep(int(Freq),int(Dur))
        print("")
        print("done")
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
