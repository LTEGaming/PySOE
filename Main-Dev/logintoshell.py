def login():
    print("user: root")
    passw = input("pass: ")
    if passw == "root":
        import pysoe_shell
        pysoe_shell.load()
    else:
        login()
login()
