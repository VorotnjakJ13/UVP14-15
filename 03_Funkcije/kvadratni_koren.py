def kvadratni_koren(a, eps=0.0000001):
"""kvadratnikoren(a) izracuna kvadratni koren stevila."""
    x = 0
    y = (x + a/x)/2
    while abs(y-x) > eps:
        x = y
        y = (x + a/x)/2
    return y
