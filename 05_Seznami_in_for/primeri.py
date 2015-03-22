def delitelji(n):
    """Vrne seznam vseh deliteljev števila n."""
    s = []
    for i in range(1, n+1):
        if n % i == 0:
            s.append(i)
    return s

def horner(pol, x):
    """Izračuna vrednost polinoma v točki s pomočjo Hornerjevega algoritma."""
    rez = 0
    for i in range(len(pol)-1, 0, -1):
        rez += pol[i]
        rez *= x
    return rez + pol[0]

def horner2(pol, x):
    """Izračuna vrednost polinoma v točki s pomočjo Hornerjevega algoritma."""    
    rez = 0
    for koef in reversed(pol):
        rez += koef
        rez *= x
    return rez/x


def horner3(pol, x):
    """Izračuna vrednost polinoma v točki s pomočjo Hornerjevega algoritma."""    
    def hornerR(i):
        if i == len(pol):
            return 0
        if i == 0:
            return hornerR(1) + pol[0]
        return (hornerR(i + 1) + pol[i])*x
    return hornerR(0)

v1 = [1, 2, 3]
v2 = [-1, 1, 4]
pol = [-7, 5, -3, 2]

def skalarni_produkt(v1, v2):
    """Vrne skalarni produkt dveh vektorjev podanih v obliki seznama."""
    n = len(v1)
    vsota = 0
    for i in range(n):
        vsota += v1[i]*v2[i]
    return vsota

def skalarni_produkt2(v1, v2):
    """Vrne skalarni produkt dveh vektorjev podanih v obliki seznama."""
    vsota = 0
    for x, y in zip(v1, v2):
        vsota += x*y
    return vsota

def vsota(v1, v2):
    """Vrne vektor, ki je vsota podanih dveh vektorjev."""    
    rez = []
    for x, y in zip(v1, v2):
        rez.append(x + y)
    return rez

def vrednost_polinoma(pol, x):
    """Izračuna vrednost polinoma v točki na 'klasični način'."""
    vsota = 0
    for i in range(len(pol)):
        vsota += pol[i] * x**i
    return vsota

def vrednost_polinoma2(pol, x):
    """Izračuna vrednost polinoma v točki na 'klasični način'."""
    vsota = 0
    for i, koef in enumerate(pol): 
        vsota += koef * x**i
    return vsota

def obdelaj2(niz):
    """Zamenja velike črke z malimi in obratno ter odstrani števke iz niza."""
    if len(niz) == 0: return ""   # zaustavitveni pogoj
    z, *ostalo = niz              # obdelamo en znak, ostalo v rekurzivnem klicu
    if z.isupper(): znak = z.lower()
    elif z.islower(): znak = z.upper()
    elif z.isdigit(): znak = ""
    else: znak = z
    return znak + obdelaj(ostalo) # rekurzivni klic

besedilo = "To Je 10. BesedilO za 0"

def obdelaj(niz):
    """Zamenja velike črke z malimi in obratno ter odstrani števke iz niza."""
    rez = ""
    for z in niz:
        if z.isupper(): rez += z.lower()
        elif z.islower(): rez += z.upper()
        elif z.isdigit(): rez += ""
        else: rez += z
    return rez

M = [
[1, 3, 4],
[2, 4, 5],
[1, 7, 0]
]

import random

def nakljucna_kvadratna_matrika(dim, minimum=1, maksimum=10):
    """Vrne naključno generirano kvadratno matriko dimenzije 'dim',
s celoštevilskimi vrednostmi na intervalu [minimum, maksimum]."""
    matrika = []
    for i in range(dim):
        vrstica = []
        for j in range(dim):
            vrstica.append(random.randint(minimum, maksimum))
        matrika.append(vrstica)
    return matrika
                           
def nakljucna_kvadratna_matrika2(dim, minimum=1, maksimum=10):
    """Vrne naključno generirano kvadratno matriko dimenzije 'dim',
s celoštevilskimi vrednostmi na intervalu [minimum, maksimum]."""    
    return [
        [random.randint(minimum, maksimum) for stolpec in range(dim)]  # ena vrstica
           for vrstica in range(dim) # ponavljanje vrstic
        ]

def transponiraj(mat):
    """Vrne transponirano matriko 'mat'."""
    m = len(mat); n = len(mat[0])
       # nicelna matrika z dimenzijami transponiranke
    nova = [[0 for j in range(m)] for i in range(n)]
    for i in range(m):    # po vrsticah mat
        for j in range(n):  # po stolpcih mat
            nova[j][i] = mat[i][j]  # transponiran prepis
    return nova


def determinanta(mat):
    """Izračuna determinanto matrike 'mat'."""
    vsota = 0
    if len(mat) == 1:   # matrike 1 x 1d
        return mat[0][0]
    for j, vr in enumerate(mat[0]):
        predznak = 1 if j % 2 == 0 else -1
        vsota += predznak*vr*determinanta(podmatrika(mat, 0, j))
    return vsota

def podmatrika(mat, i, j):
    """Vrne podmatriko matrike 'mat', ki jo dobimo z odstranitvijo
i-te vrstice in j-tega stolpca."""
    m = len(mat); n = len(mat[0])
    return [
        [mat[ii][jj] for jj in range(n) if jj != j] # ii-ta vrstica
            for ii in range(m) if ii != i #
    ] 
    

import turtle
def izris_matrike(mat, sirina=30, visina=20):
    """Izriše matriko v tabeli s pomočjo želvje grafike."""
        # inicializacija, parametri
    odmikX = sirina/2
    odmikY = visina*0.9
    m = len(mat); n = len(mat[0])
    zaslon = turtle.Screen()
    zelva = turtle.Turtle()
    zelva.up(); zelva.speed(0); zelva.hideturtle()
       # izris besedil
    zelva.goto(-n/2*sirina, m/2*visina)
    for i in range(m):
        for j in range(n):
            zelva.goto(-n/2*sirina + j*sirina + odmikX,
                       m/2*visina - i*visina - odmikY)
            zelva.write(mat[i][j], False, align="center",
                        font=("Arial", int(visina*0.8), "normal"))
      # okvir (vodoravne črte)
    zelva.goto(-n/2*sirina, m/2*visina)
    for i in range(m + 1):
        zelva.goto(-n/2*sirina, m/2*visina - i*visina)
        zelva.down()
        zelva.fd(sirina*n)
        zelva.up()
    zelva.right(90)
      # okvir (navpicne črte)
    for j in range(n + 1):
        zelva.goto(-n/2*sirina + j*sirina, m/2*visina)
        zelva.down()
        zelva.fd(visina*m)
        zelva.up()
