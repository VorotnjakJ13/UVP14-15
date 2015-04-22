import os

def ustvari(ime="mape_in_datoteke.txt"):
    with open(ime, "rt", encoding="utf8") as f:
        datoteka = None
        for vrstica in f:
            if vrstica[0] == "-":
                if datoteka is not None:
                    datoteka.close()
                    datoteka = None
                pot = vrstica.lstrip("-").strip()
                print("Delam mapo:", pot)
                os.mkdir(pot)
            elif vrstica[0] == "*":
                if datoteka is not None:
                    datoteka.close()
                pot = vrstica.lstrip("*").strip()
                print("Delam datoteko:", pot)
                datoteka = open(pot, "wt", encoding="utf8")
            elif datoteka is not None:
                datoteka.write(vrstica)
                

# ustvari()


def preglej(mapa="."):
    for pot, mape, datoteke in os.walk(mapa):
        for dat in datoteke:
            kaj = os.path.join(pot, dat)
            _, koncnica = os.path.splitext(dat)
            if koncnica.lower() == ".txt":
                print(kaj)
                print("   ", os.path.getsize(kaj))

preglej()
