def kvadratna_izpis(a, b, c):
    """Vrne niz z izpisom kvadratne funkcije na lep način"""
    prvi = a != 0                  
    s = ""       
    if prvi:
        if a == 1: s += "x**2"
        elif a == -1: s+= "-x**2"
        else: s+= str(a) + "x**2"   # predznak iz izpisa števila

    prvi = a == 0 and b != 0
    if prvi:
        if b == 1: s += "x"
        elif b == -1: s += "-x"
        else: s += str(b) + "x"     # predznak iz izpisa števila
    else:
        if b == 0: pass
        elif b > 0:
            if b == 1: s += " + x"
            else: s += " + " + str(b) + "x"
        else: # b < 0
            if b == -1: s += " - x"
            else: s += " - " + str(abs(b)) + "x"

    prvi = a == 0 and b == 0
    if prvi:                                
        s += str(c)
    else:
        if c > 0: s += " + " + str(abs(c))
        elif c < 0: s += " - " + str(abs(c))
    return s


##print(kvadratna_izpis(3, 2, 1))
##print(kvadratna_izpis(-2, -3, 0))
##print(kvadratna_izpis(0, 1, -1))
##print(kvadratna_izpis(0, 0, -4))
##print(kvadratna_izpis(0, 4, -5))
##print(kvadratna_izpis(1, -1, -1))


