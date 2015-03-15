def izpisi(a, b):
    """Izpiše vsa cela števila na intervalu [a, b]."""
    if a <= b:
        print(a)
        izpisi(a + 1, b)
            
def izpisi2(a, b):
    """Izpiše vsa cela števila na intervalu [a, b]."""
    if a == b:
        print(a)
    elif a < b:
        sredina = (a + b)//2
        izpisi2(a, sredina)
        izpisi2(sredina + 1, b)
