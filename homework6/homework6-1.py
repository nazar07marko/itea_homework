def m():
    a = input("Введіть бажану операцію ")
    b = input("Введіть 1 число ")
    c = input("Введіть 2 число ")
    if a == "+":
        print(f"{int(b)+int(c)}")
    if a == "-":
        print(f"{int(b)-int(c)}")
    if a == "*":
        print(f"{int(b)*int(c)}")
    if a == "/":
        print(f"{int(b)/int(c)}")
    if a == "**":
        print(f"{int(b)**int(c)}")
m()