import turtle, random
from math import *

def drevo(zelva, red, velikost, faktor, kot):
    """Nariše drevo kot fraktal danega reda in velikosti. Faktor
predstavlja zmanjševanje na vejah in kot predstavlja kot med vejama."""
    if red == 0: return
    if red <= 2:    # majhna drevesčka bodo zelena (listi)
        zelva.pencolor("green")
    else:
        zelva.pencolor("brown")
    zelva.pensize(log(2*red))
    zelva.down()
    zelva.forward(velikost)  # osnovna veja
    zelva.right(kot)         # prva izrasla veja
    drevo(zelva, red - 1, velikost*faktor, faktor, kot)
    zelva.left(2*kot)        # druga izrasla veja v drugo stran
    drevo(zelva, red - 1, velikost*faktor, faktor, kot)
    zelva.right(kot)         # vrnitev v koren
    zelva.up()
    zelva.backward(velikost)

def test(n):
    zaslon = turtle.Screen()
    zelva = turtle.Turtle()
    zelva.speed(0); zelva.hideturtle()
    zelva.left(90)     # smer rasti drevesa
    drevo(zelva, n, 80, 0.7, 30) 


