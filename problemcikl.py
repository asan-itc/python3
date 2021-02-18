a = -100
b = a
c = 0
d = 0
while a <= 100:
    if (a%13==0) & (a%2==0):
        print(a,a**2)
        d += 1
    a += 1
print(d)
while b <= 100:
    if b%2==1:
        c += 1
        print(b)
    b += 7
print(c)                