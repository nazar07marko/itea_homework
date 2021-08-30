a = []
i = 1
while i <= 3:
    b = input(f"Введіть {i} число ")
    a.append(b)
    i=i+1
print(int(a[0])+int(a[1])+int(a[2]))