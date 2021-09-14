user = {
    "balance": 0,
    "account": 0
}

print("---------------")
print("***HUVUDMENY***")
print("---------------")

print("1. Skapa konto")
print("2. Adminstrera konto")
print("3. Avsluta")

while True:
    cmd = input("Ange menyval > ")
    
    if cmd == "1":
        def create_user():
            kontonummer = input("Ange kontonummer: ")
            user["account"] = kontonummer
            print("Ditt nya kontonummer är", kontonummer)