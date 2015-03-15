import turtle

def koch(zelva, red, velikost):
    """Nariše Kochovo snežinko danega reda in velikosti z želvo. """

    if red == 0:          # Ravna črta
        zelva.forward(velikost)
    else:
        koch(zelva, red-1, velikost/3)   
        zelva.left(60)
        koch(zelva, red-1, velikost/3)
        zelva.right(120)
        koch(zelva, red-1, velikost/3)
        zelva.left(60)
        koch(zelva, red-1, velikost/3)

def kochova_snezinka(red, velikost, start=(0,0)):
    """Pomožna funkcija za demonstracijo izrisa Kochove snežinke."""
    zaslon = turtle.Screen()
    zelva = turtle.Turtle()
    zelva.hideturtle(); zelva.speed(0)
    zelva.up(); zelva.goto(*start); zelva.down()
    koch(zelva, red, velikost)

    
def test():
    """Demonstracijski program za nekaj prvih redov Kochove snežinke."""
    velikost = 300
    i = 0
    while i < 5:
        kochova_snezinka(i, velikost, start=(-200, 200 - i*100))
        i += 1
                     
def prava_kochova_snezinka(red, velikost, start=(0,0)):
    """Izriše kochovo snežinko danega reda in velikosti.
Risanje začne v podani točki start."""
    zaslon = turtle.Screen()
    zelva = turtle.Turtle()
    zelva.hideturtle(); zelva.speed(0)
    zelva.up(); zelva.goto(*start); zelva.down()
    zelva.left(60)
    i = 0
    while i < 3:
        koch(zelva, red, velikost)
        zelva.right(120)
        i += 1
    
    
    

