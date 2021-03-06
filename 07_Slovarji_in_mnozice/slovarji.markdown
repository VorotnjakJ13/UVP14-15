# Slovarji & množice

---

# Slovarji

---

```python
nujne_telefonske_stevilke = {
  'center za obveščanje': 112,
  'policija': 113,
  'informacije': 1188,
  'točen čas': 195
}
```

---

## Zakaj uporabljamo slovarje?

---

### Primer: slovarji

```python
slo_ang = {
  'abak': 'abacus',
  'abalienacija': 'abalienation',
  'abderit': 'abderite',
  ...
  'žvrkljati': 'whisk'
}
```

```python
rimske_stevilke = {
    1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V',
    6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX',
    10: 'X', 20: 'XX', 30: 'XXX', 40: 'XL', 50: 'L',
    100: 'C', 500: 'D', 1000: 'M'
}
```

---

### Primer: preštevanje

```python
vrli_parlamentarci = {
    'DeSUS': 10, 'NSi': 5, 'SD': 6, 'SDS': 21,
    'SMC': 36, 'ZaAB': 4, 'ZL': 6
}
```

```python
met_kocke = {
    1: 1/6, 2: 1/6, 3: 1/6, 4: 1/6, 5: 1/6, 6: 1/6
}

met_dveh_kock = {
    2: 1/36, 3: 2/36, 4: 3/36, 5: 4/36, 6: 5/36, 7: 6/36,
    8: 5/36, 9: 4/36, 10: 3/36, 11: 2/36, 12: 1/36
}
```

---

### Primer: redke matrike

```python
matrika = [[0, 0, 1, 0, 0, 0],
           [5, 2, 0, 0, 0, 0],
           [0, 0, 0, 0, 3, 0],
           [0, 0, 0, 0, 0, 0],
           [0, 0, 1, 0, 0, 0],
           [0, 0, 0, 0, 0, 0]]
```

```python
redka_matrika = {
    (0, 2): 1,
    (1, 0): 5,
    (1, 1): 2,
    (2, 4): 3,
    (4, 2): 1
}
```

---

### Primer: omrežja

```python
avtocestni_kriz = {
    'LJ': {'KR': 26, 'CE': 73, 'PO': 51, 'NM': 72},
    'PO': {'LJ': 51, 'KP': 64, 'GO': 63},
    'CE': {'MB': 54, 'LJ': 73},
    'MB': {'CE': 54, 'MS': 60},
    'GO': {'PO': 63},
    'KR': {'LJ': 26},
    'MS': {'MB': 60},
    'NM': {'LJ': 72},
    'KP': {'GO': 64}
}
```

---

### Primer

```python
knjiga = {
    'naslov': 'Prišel je velikanski lev',
    'avtor': 'Kristina Brenkova',
    'ilustrator': 'Polona Lovšin',
    'strani': 31,
    'leto': 2010,
    'ključne besede': ['lev', 'Afrika', 'Matic', 'otroci']
}
```

```python
nakljucni_slovar = {
    1: 'abc',
    (2, '3'): 'D',
    '456': 789
}
```

---


## Kaj so osnovne operacije?

---

### Vgrajene funkcije

```python
>>> s = {'a': 6, 'b': 2, 'c': 3}
```

```python
>>> len(s)
3
```

```python
>>> max(s)
'c'
```
```python
>>> max(s.values())
6
```

```python
>>> sum(s.values())
11
```

---

### Branje

```python
>>> s = {'a': 6, 'b': 2, 'c': 3}
```

```python
>>> s['a']
6
```
```python
>>> s['b']
2
```
---

### Manjkajoči ključi

```python
>>> s = {'a': 6, 'b': 2, 'c': 3}
```

```python
>>> s['d']
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    s['d']
KeyError: 'd'
```
```python
>>> s.get('a')
6
```

```python
>>> s.get('d')
```
```python
>>> s.get('d', 0)
0
```
---

### Pisanje

```python
>>> s = {'a': 6, 'b': 2, 'c': 3}
```
```python
>>> s['b'] = 8
```
```python
>>> s
{'a': 6, 'b': 8, 'c': 3}
```
```python
>>> s['d'] = 10
```
```python
>>> s
{'a': 6, 'b': 8, 'c': 3, 'd': 10}
```

---

### Brisanje

```python
>>> s = {'a': 6, 'b': 2, 'c': 3}
```
```python
>>> del s['b']
```
```python
>>> s
{'a': 6, 'c': 3}
```

---

### Iskanje

```python
>>> s = {'a': 6, 'b': 2, 'c': 3}
```
```python
>>> 'b' in s
True
```
```python
>>> 'd' in s
False
```

---

## Primer: preštevanje pojavitev znakov

```python
def prestej_pojavitve(niz):
    pojavitve = {}
    for znak in niz:
        if znak in pojavitve:
            pojavitve[znak] += 1
        else:
            pojavitve[znak] = 1
    return pojavitve
```

---

## Zanka `for`

---

### Po ključih

```python
s = {'a': 6, 'b': 2, 'c': 3}
for k in s.keys():
    print(k)
```

```python
b
a
c
```

---

### Po ključih

```python
s = {'a': 6, 'b': 2, 'c': 3}
for k in s:
    print(k)
```

```python
b
a
c
```
---

### Po vrednostih

```python
s = {'a': 6, 'b': 2, 'c': 3}
for v in s.values():
    print(v)
```

```python
6
2
3
```

---

### Po ključih in vrednostih

```python
s = {'a': 6, 'b': 2, 'c': 3}
for k, v in s.items():
    print(k, v)
```

```python
c 3
a 6
b 2
```

---

### Izpeljani slovarji

```python
>>> {n: stevilo_deliteljev(n) for n in range(20, 29)}
{20: 6, 21: 4, 22: 4, 23: 2, 24: 8, 25: 3, 26: 4, 27: 4, 28: 6}```

---


## Primer: iskanje ključa z največjo vrednostjo

```python
def najvecja_vrednost(s):
    # Ideja je podobna kot pri seznamih: po vrsti gledamo vse pare ključev in
    # vrednosti v slovarju - vsakič, ko vidimo še večjo vrednost, si zapomnimo
    # njen ključ.

    # Ker slovarji niso urejeni po vrsti, ne moremo začeti s prvim elementom.
    # Lahko pa si pomagamo z metodo popitem(), ki iz slovarja odstrani naključen
    # ključ in njegovo vrednost.
    max_k, max_v = s.popitem()
    for k, v in s.items():
        if v > max_v:
            max_k, max_v = k, v
    return max_k, max_v
```

---


# Množice

---

```python
def je_prastevilo(n):
    if n <= 2:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True
```
---

```python
majhna_prastevila = {2, 3, 5, 7, ..., 997}

def je_prastevilo(n):
    if n <= majhna_prastevila[-1]:
        return n in majhna_prastevila
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True
```

---

### Vgrajene funkcije


```python
>>> s = {6, 2, 3}
```

```python
>>> len(s)
3
```

```python
>>> max(s)
6
```

```python
>>> sum(s)
11
```

```python
>>> sez = [1, 5, 2, 4, 8, 1, 5, 3, 2, 1]
>>> sum(sez)
32
>>> mn = set(sez)
>>> sum(mn)
23
```

---

### Dodajanje in odstranjevanje elementov

```python
>>> a = {1, 2, 3, 4}
```
```python
>>> a.add(5)
```
```python
>>> a
{1, 2, 3, 4, 5}
```
```python
>>> a.remove(3)
```
```python
>>> a
{1, 2, 4, 5}
```

---

### Matematične operacije

```python
>>> {1, 2, 3, 4} | {3, 4, 5, 6}
{1, 2, 3, 4, 5, 6}
```
```python
>>> {1, 2, 3, 4} & {3, 4, 5, 6}
{3, 4}
```
```python
>>> {1, 2, 3, 4} - {3, 4, 5, 6}
{1, 2}
```
```python
>>> 1 in {1, 2, 3, 4}
True
>>> 2 in {3, 4, 5, 6}
False
```

---

### Zanka `for`

```python
a = {'a', 'b', 'c'}
for x in a:
    print(x)
```
```python
c
a
b
```

```python
def direktna_slika(f, a):
    slika = set()
    for x in a:
        slika.add(f(x))
    return slika
```
```python
>>> direktna_slika(lambda x: x ** 2, {-5, -3, 1, 2})
{1, 4, 9, 25}
```


---

### Izpeljane množice

```python
>>> {x ** 2 for x in range(1, 30) if x % 5 == 3}
{64, 324, 9, 169, 784, 529}
```
```python
>>> {x for x in range(1, 100) if x % 5 == 3 and x % 3 != 0}
{8, 13, 23, 28, 38, 43, 53, 58, 68, 73, 83, 88, 98}
```

```python
def direktna_slika(f, a):
    slika = set()
    for x in a:
        slika.add(f(x))
    return slika
```

```python
def direktna_slika(f, a):
    return {f(x) for x in a}
```

---


## Primer: družabno omrežje

```python
{
    'Borut': {'Janez', 'Miro', 'Karl'},
    'Janez': {'Borut', 'Karl'},
    'Miro': {'Borut', 'Karl'},
    'Karl': {'Borut', 'Janez', 'Miro'},
    'Igor': set(),
}
```

```python
def priporoci_prijatelje(omrezje, oseba):
    novi_prijatelji = set()
    for prijatelj in omrezje[oseba]:
        for prijatelj_prijatelja in omrezje[prijatelj]:
            novi_prijatelji.add(prijatelj_prijatelja)
    return novi_prijatelji - {oseba} - omrezje[oseba]

```

---

# Da ponovimo

### Vrednosti v slovarju so urejene po ključih.
### S slovarji delamo podobno kot s seznami.
### Dostop do ključev v slovarju je zelo hiter.
### Če nas zanimajo le ključi, uporabimo množice.
