a = input("Ввеліть перше число ")
b = input("Введіть друге число ")
if int(a) and int(b):
    print(f"{a}+{b}={int(a)+int(b)}")
    print(f"{a}-{b}={int(a)-int(b)}")
    print(f"{a}/{b}={int(a)/int(b)}")
    print(f"{a}**2={int(a)**2}")
else:
    print("Вводьте будьласка цілі числа")