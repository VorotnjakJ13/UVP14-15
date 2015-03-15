import turtle

def crtkano(zelva, n, crta=20, prazno=10):
    """Izriše črtkano črto z določeno dolžino črtic in praznin
dolgo n skokov."""
    if n == 0: return
    zelva.down()
    zelva.fd(crta)  # crtica
    zelva.up()
    zelva.fd(prazno)  # presledek
    crtkano(zelva, n - 1, crta, prazno) # rekurzivna "zanka"

def zelvasto(zelva, n, skok=30):
    """Pušča n sledi želve z danim skokom."""
    i = 0
    zelva.shape('turtle')   # navadna zanka
    while i < n:
        zelva.stamp()
        zelva.fd(skok)
        i += 1
        
def test(n):
    """Demonstracija črtkane črte in odtisov želvice."""
    zaslon = turtle.Screen()
    zelva = turtle.Turtle()
    zelva.speed(0)          # = "fastest"
    zelva.hideturtle()      # želvo skrijemo
    zelva.up()
    zelva.goto(-200, 150)   # direktni skok
    crtkano(zelva, n)
    zelva.goto(-200, 100)
    zelvasto(zelva,n)
    print("Položaj želve je:", zelva.position())
    
test(15)
