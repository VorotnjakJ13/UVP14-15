from kvadratna_izpis import *

def kvadratna_enacba(a, b, c):
    """Izpiše na zaslon analizo rešitev kvadratne enačbe a*x**2 + b*x + c.
Funkcija vedno vrne None."""
    print("Enačba: ", kvadratna_izpis(a,b,c), "= 0")
    if a == 0:
        print("Enačba je linearna.")
        if b == 0:
            if c == 0:
                print("Rešitev je cela realna os.")
            else:
                print("Rešitev je prazna množica.")
        else:
            print("Rešitev linearne enačbe je x = ",-c/b)
    else:
        D = b**2 - 4*a*c
        if D < 0:
            print("Konjugirano kompleksna korena.")
        elif D > 0:
            print("Realna korena.")
        else:
            print("Dvojni realni koren.")


kvadratna_enacba(0, 0, 0)
kvadratna_enacba(0, 0, 1)
kvadratna_enacba(0, 4, 2)
kvadratna_enacba(4, 2, 1)
kvadratna_enacba(1, 2, 1)


