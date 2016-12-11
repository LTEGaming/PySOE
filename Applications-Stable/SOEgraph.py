block = "█"
space = " "
lim = 0
writes = "output"
textfile = 0
writecount = 0
origin = "output.txt"

def cls():
    print ("\n" * 50)
cls()

h1 ="100%|"
h2 ="90% |"
h3 ="80% |"
h4 ="70% |"
h5 ="60% |"
h6 ="50% |"
h7 ="40% |"
h8 ="30% |"
h9 ="20% |"
p0 ="10% |"
p1 ="0%  |"
p2 ="--% |______________________________"
def grapfunt():
    global h1
    global h2
    global h3
    global h4
    global h5
    global h6
    global h7
    global h8
    global h9
    global p0
    global p1
    global p2
    global lim
    answer = input("How much will you graph? ")
    if answer == "100":
        h1 = h1+block
        h2 = h2+space
        h3 = h3+space
        h4 = h4+space
        h5 = h5+space
        h6 = h6+space
        h7 = h7+space
        h8 = h8+space
        h9 = h9+space
        p0 = p0+space
        p1 = p1+space
        lim = int(lim) + 1
        prinnt()
    elif answer == "90":
        h1 = h1+space
        h2 = h2+block
        h3 = h3+space
        h4 = h4+space
        h5 = h5+space
        h6 = h6+space
        h7 = h7+space
        h8 = h8+space
        h9 = h9+space
        p0 = p0+space
        p1 = p1+space
        lim = int(lim) + 1
        prinnt()
    elif answer == "80":
        h1 = h1+space
        h2 = h2+space
        h3 = h3+block
        h4 = h4+space
        h5 = h5+space
        h6 = h6+space
        h7 = h7+space
        h8 = h8+space
        h9 = h9+space
        p0 = p0+space
        p1 = p1+space
        lim = int(lim) + 1
        prinnt()
    elif answer == "70":
        h1 = h1+space
        h2 = h2+space
        h3 = h3+space
        h4 = h4+block
        h5 = h5+space
        h6 = h6+space
        h7 = h7+space
        h8 = h8+space
        h9 = h9+space
        p0 = p0+space
        p1 = p1+space
        lim = int(lim) + 1
        prinnt()
    elif answer == "60":
        h1 = h1+space
        h2 = h2+space
        h3 = h3+space
        h4 = h4+space
        h5 = h5+block
        h6 = h6+space
        h7 = h7+space
        h8 = h8+space
        h9 = h9+space
        p0 = p0+space
        p1 = p1+space
        lim = int(lim) + 1
        prinnt()
    elif answer == "50":
        h1 = h1+space
        h2 = h2+space
        h3 = h3+space
        h4 = h4+space
        h5 = h5+space
        h6 = h6+block
        h7 = h7+space
        h8 = h8+space
        h9 = h9+space
        p0 = p0+space
        p1 = p1+space
        lim = int(lim) + 1
        prinnt()
    elif answer == "40":
        h1 = h1+space
        h2 = h2+space
        h3 = h3+space
        h4 = h4+space
        h5 = h5+space
        h6 = h6+space
        h7 = h7+block
        h8 = h8+space
        h9 = h9+space
        p0 = p0+space
        p1 = p1+space
        lim = int(lim) + 1
        prinnt()
    elif answer == "30":
        h1 = h1+space
        h2 = h2+space
        h3 = h3+space
        h4 = h4+space
        h5 = h5+space
        h6 = h6+space
        h7 = h7+space
        h8 = h8+block
        h9 = h9+space
        p0 = p0+space
        p1 = p1+space
        lim = int(lim) + 1
        prinnt()
    elif answer == "20":
        h1 = h1+space
        h2 = h2+space
        h3 = h3+space
        h4 = h4+space
        h5 = h5+space
        h6 = h6+space
        h7 = h7+space
        h8 = h8+space
        h9 = h9+block
        p0 = p0+space
        p1 = p1+space
        lim = int(lim) + 1
        prinnt()
    elif answer == "10":
        h1 = h1+space
        h2 = h2+space
        h3 = h3+space
        h4 = h4+space
        h5 = h5+space
        h6 = h6+space
        h7 = h7+space
        h8 = h8+space
        h9 = h9+space
        p0 = p0+block
        p1 = p1+space
        lim = int(lim) + 1
        prinnt()
    elif answer == "0":
        h1 = h1+space
        h2 = h2+space
        h3 = h3+space
        h4 = h4+space
        h5 = h5+space
        h6 = h6+space
        h7 = h7+space
        h8 = h8+space
        h9 = h9+space
        p0 = p0+space
        p1 = p1+block
        lim = int(lim) + 1
        prinnt()
    else:
        print("Please use 100-0")
        grapfunt()
    
def prinnt():
    global lim
    global h1
    global h2
    global h3
    global h4
    global h5
    global h6
    global h7
    global h8
    global h9
    global p0
    global p1
    global p2
    global writes
    cls()
    print(h1)
    print(h2)
    print(h3)
    print(h4)
    print(h5)
    print(h6)
    print(h7)
    print(h8)
    print(h9)
    print(p0)
    print(p1)
    print(p2)
    if lim < 30:
        grapfunt()
    else:
        answer = input("Your graph is full. Would you like me to |E|rase it or |S|ave and erase it?")
        if answer == "E":
            cls()
            reset()
        if answer == "S":
            cls()
            save()
                
def reset():
    global lim
    global h1
    global h2
    global h3
    global h4
    global h5
    global h6
    global h7
    global h8
    global h9
    global p0
    global p1
    global p2
    h1 ="100%|"
    h2 ="90% |"
    h3 ="80% |"
    h4 ="70% |"
    h5 ="60% |"
    h6 ="50% |"
    h7 ="40% |"
    h8 ="30% |"
    h9 ="20% |"
    p0 ="10% |"
    p1 ="0%  |"
    p2 ="--% |______________________________"
    lim = 0
    answer5 = input("Would you like to restart your graph? Y/N ")
    if answer5 == "Y":
        grapfunt()
    else:
        exit()

def save():
    global h1
    global h2
    global h3
    global h4
    global h5
    global h6
    global h7
    global h8
    global h9
    global p0
    global p1
    global p2
    global writes
    global textfile
    global writecount
    global origin
    if writecount == 0:
        with open(origin ,'w', encoding='utf-7') as f:
            f.write(h1)
            f.write("\n")
            f.write(h2)
            f.write("\n")
            f.write(h3)
            f.write("\n")
            f.write(h4)
            f.write("\n")
            f.write(h5)
            f.write("\n")
            f.write(h6)
            f.write("\n")
            f.write(h7)
            f.write("\n")
            f.write(h8)
            f.write("\n")
            f.write(h9)
            f.write("\n")
            f.write(p0)
            f.write("\n")
            f.write(p1)
            f.write("\n")
            f.write(p2)
            f.flush()
            print("")
            print("Saved as output.file in current directory.")
            print("")
            print("Please copy this file somewhere else to avoid being overwritten")
            print("")
            writecount=writecount+1
            reset()
    else:
        writes = writes+"-"
        textfile = writes+".txt"
        with open(textfile ,'w', encoding='utf-7') as f:
            f.write(h1)
            f.write("\n")
            f.write(h2)
            f.write("\n")
            f.write(h3)
            f.write("\n")
            f.write(h4)
            f.write("\n")
            f.write(h5)
            f.write("\n")
            f.write(h6)
            f.write("\n")
            f.write(h7)
            f.write("\n")
            f.write(h8)
            f.write("\n")
            f.write(h9)
            f.write("\n")
            f.write(p0)
            f.write("\n")
            f.write(p1)
            f.write("\n")
            f.write(p2)
            f.flush()
            print("")
            print("Saved as", textfile,"in current directory")
            print("")
            print("Please copy this file somewhere else to avoid being overwritten")
            print("")
            reset()

grapfunt()
prinnt()
