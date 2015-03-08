def je_prastevilo(n):
    """Preveri, če je dano število n praštevilo."""
    p = 2
    jeAliNi = True
    while p*p < n:
        if n % p == 0:
            jeAliNi = False
            break
        p += 1
    return jeAliNi

def prastevila_na_intervalu(a, b):
    """Izpise prastevila na intervalu [a, b]."""
    n = a
    while n <= b:
        if je_prastevilo(n):
            print(n)
        n += 1

prastevila_na_intervalu(10, 20)
