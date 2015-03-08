def tocka_v_pravokotniku(t, p1, p2):
    """Preveri, če je točka t vsebovana v pravokotniku vzporednem s
koordinatnima osema definiranim z vogali p1 in p2."""
    x,y = t
    x1,y1 = p1
    x2,y2 = p2
    x1,x2 = (x1 if x1 < x2 else x2, x1 if x1 > x2 else x2)
    y1,y2 = (y1 if y1 < y2 else y2, y1 if y1 > y2 else y2)
    return x1 <= x <= x2 and y1 <= x <= y2


print(tocka_v_pravokotniku((1,1), (0,0), (2,2)))
print(tocka_v_pravokotniku((1,1),(0,2), (2,0))) 
print(tocka_v_pravokotniku((10,1),(0,2), (2,0)))      
