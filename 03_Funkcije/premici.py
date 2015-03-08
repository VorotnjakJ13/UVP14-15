def premici(k1, n1, k2, n2):
    """Vrne eno od presečišč premic y = k1*x + n1 in y = k2*x + n2 ali
None."""
    if k1 == k2:
        if n1 == n2: # rešitev je vsak x
            return 0, n1 # presečišče v x = 0.
        return None # ni rešitve
    else:
        x = (n2 - n1)/(k1 - k2)
        y = k1*x + n1
        return x, y

# PAZI: a je uporaba == na tipu float smiselna?

print(premici(1,10, -1, 3))
print(premici(1,1.000001, 1, 1))
print(premici(1,1,1,1))

def premici_epsilon(k1, n1, k2, n2, eps=0.000001):
    """Vrne eno od presečišč premic y = k1*x + n1 in y = k2*x + n2 ali
None."""
    if abs(k1 - k2) < eps:
        if abs(n1 - n2) < eps:
            return 1, k1 + n1
        return None
    else:
        x = (n2 - n1)/(k1 - k2)
        y = k1*x + n1
        return x, y


print(premici_epsilon(1,1.000001, 1, 1, eps=0.001))
