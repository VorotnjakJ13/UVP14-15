def beri(ime, encoding="utf8"):
    with open(ime, encoding=encoding) as f:
        for vrstica in f:
            print(vrstica)


def pisi(ime, vsebina, encoding="utf8"):
    with open(ime, "wt", encoding=encoding) as f:
        f.write(vsebina)
