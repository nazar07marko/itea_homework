a = {"salt": 2, "meat": 25, "apples": 6, "banana":3, "milk": 4.5, "bread": 2.5}
d = []
h = 0
while h < 3:
    b = list(a.keys())[0]
    for i in a:
        if a[b] < a[i]:
            b = i
    d.append({b: a[b]})
    a.pop(b) 
    h=h+1
print(d)