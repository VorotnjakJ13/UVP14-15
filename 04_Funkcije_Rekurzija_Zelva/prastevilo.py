def je_delitelj(p, n):
    """Vrne True, če obstaja kak nepraštevilski delitelj n, ki
je večji ali enak p."""
    if p*p <= n:
        return n % p == 0 or je_delitelj(p + 1, n)
    return False 

je_delitelj(2, 23)

def je_prastevilo(n):
    """Vrne True, če je n praštevilo."""
    def je_delitelj(p, n):
        if p*p <= n:
            return n % p == 0 or je_delitelj(p + 1, n)
        return False    
    return not je_delitelj(2, n)
