def end():
    print("")
    a = input("Would you like to restart? Y/N ")
    if a == "y" or a == "Y":
        print("")
        print("---------------------BREAK LINE---------------------")
        print("")
        main()
    if a == "n" or a == "N":
        print("Exiting to PySOE")
        print("Finish")
def add(x1,x2):
    y = x1 + x2
    print("Your answer is",y)
    end()
def sub(x1,x2):
    y = x1 - x2
    print("Your answer is",y)
    end()
def mult(x1,x2):
    y = x1 * x2
    print("Your answer is",y)
    end()
def div(x1,x2):
    y = x1 + x2
    print("Your answer is",y)
    end()
def intdiv(x1,x2):
    x1 = int(x1)
    x2 = int(x2)
    y = x1 // x2
    print("Your answer is",y)
    end()
def mod(x1,x2):
    x1 = int(x1)
    x2 = int(x2)
    y = x1 % x2
    print("Your answer is",y)
    end()
def main():
    print("▄████████████████ 6 Function Calc █████████████████▄")
    print("█                                                  █")
    print("█ Welcome to a 6 function calculator, by Carson G. █")
    print("█                                                  █")
    print("▀██████████████████████████████████████████████████▀")
    for i in range(10):
        print("")
    print("Your available operators are: +, -, *, /, //, %")
    print("")
    sk_st = input("Please input your equation for solving. e.g '3 + 2' ")
    sk_li = sk_st.split()
    n1 = sk_li[0]
    op = sk_li[1]
    n2 = sk_li[2]
    n1 = float(n1)
    n2 = float(n2)
    print("")
    if op == '+':
        add(n1,n2)
    elif op == '-':
        sub(n1,n2)
    elif op == '*':
        mult(n1,n2)
    elif op == '/':
        div(n1,n2)
    elif op == '//':
        intdiv(n1,n2)
    elif op == '%':
        mod(n1,n2)
    else:
        print("That is not a valid operator!")
        print("")
        main()
main()





