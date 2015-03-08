n = 23
p = 2
jeAliNi = True
while p*p < n:
    if n % p == 0:
        jeAliNi = False
        break
    p += 1
if(jeAliNi):
    print(n, "je praštevilo")
else:
    print(n, "ni praštevilo")
