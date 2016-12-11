def login():
    print("user: root")
    passw = input("pass: ")
    if passw == "root":
        import PySOE.shell
        pysoe.shell.load()
    else:
        login()
login()
