import turtle
from math import *

def veckotnik(zelva, n, stranica=100):
    """Z želvo nariše n-kotnik s podano dolžino stranice."""
    kot = 360/n
    i = 0
    while i < n:
        zelva.fd(stranica)
        zelva.left(kot)
        i += 1

def skica():
    """Izriše pomožno skico iz predavanj."""
    input("Izris večkotnika. Pritisni tipko ...")

    zaslon = turtle.Screen()
    zelva = turtle.Turtle()
    n = 5
    d = 100
    kot = 360/n
    drugi_kot = (180 - kot)/2
    veckotnik(zelva, n, stranica=d)
    input("Pritisni tipko ...")
    zelva.fd(2*d)          # podaljšaj stranico
    zelva.bk(d/2)          # sredina podaljška
    zelva.left(90)         # obrni se v smeri loka
    zelva.circle(d/2, kot)  # nariši kotni lok
    zelva.left(90)         # obrni s v smeri dotaknjene stranice
    zelva.fd(d/2)          # vrni se v drugi vogal strnice
    zelva.right(kot + drugi_kot) # obrni s proti središču
    radij = d/2 / cos(radians(drugi_kot))  # izračunaj radij
    zelva.fd(radij)        # prva stranica kota
    zelva.right(kot)       # obrat za drugo stranico
    zelva.bk(radij)        # druga stranica kota
    zelva.fd(radij*2/3)    # risanje kotnega loka
    zelva.right(90)
    zelva.circle(radij/3, kot)


def rozica(nlistov, n):
    """Izriše rožico iz n-kotnikov s podanim številom listov."""
    zaslon = turtle.Screen()
    zelva = turtle.Turtle()
    zelva.speed("fastest") # nariše hitreje
    kot = 360/nlistov
    i = 0
    while i < nlistov:
        zelva.left(kot)
        veckotnik(zelva, n)
        i += 1
        
# rozica(15, 5)

def zapolnjen_veckotnik(zelva, n, stranica=100, debelina=2, barva="yellow"):
    """Demonstracija zapolnjevanja n-kotnika."""
    stara_barva = zelva.fillcolor()  # shranimo morebitno nastavljeno barvo
    zelva.fillcolor(barva)           # nastavimo barvo
    zelva.begin_fill()               # začetek poligona
    veckotnik(zelva, n, stranica, debelina)
    zelva.end_fill()                 # konec poligona
    zelva.fillcolor(stara_barva)    # vrnemo nastavitev barvne v prvotno stanje

def poln_kvadrat():
    """Demonstracija zapolnjenega kvadrata."""
    zaslon = turtle.Screen()
    zelva = turtle.Turtle()
    zelva.speed("fastest")
    zapolnjen_veckotnik(zelva, 4)




    


    
