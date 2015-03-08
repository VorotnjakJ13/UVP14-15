def narisi_karo(n):
    narisi_zgornji_del(n)
    narisi_spodnji_del(n)

def narisi_zgornji_del(n):
    i = 0
    while i < n:
        i_ta_vrstica(n, i)
        i += 1

def narisi_spodnji_del(n):
    i = n - 2
    while i >= 0:
        i_ta_vrstica(n, i)
        i -= 1

def i_ta_vrstica(n, i):
    j = 0   # izpis presledkov
    while j < n - i - 1:
        print(" ", sep="", end="")
        j += 1
    j = 0   # izpis zvezdic
    while j < 2*i + 1:
        print("*", sep="", end="")
        j += 1
    print()  # skok v novo vrstico na koncu 


# narisi_karo(5)
# narisi_karo(8)
    


def narisi_karo2(n):
    i = 0
    while i < n:
        print((n - i - 1)*" " + (2*i + 1)*"*")
        i += 1

    i = n - 2
    while i >= 0:
        print((n - i - 1)*" " + (2*i + 1)*"*")
        i -= 1

# narisi_karo2(5)

def narisi_karo3(n):
    s = ""
    i = 0
    while i < n:
        s += (n - i - 1)*" " + (2*i + 1)*"*" + "\n"
        i += 1

    i = n - 2
    while i >= 0:
        s += (n - i - 1)*" " + (2*i + 1)*"*" + "\n"
        i -= 1
    return s

print(narisi_karo3(4))
