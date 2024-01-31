def sucet(x, y):
    return x + y

def parne(cislo):
    if cislo % 2 == 0:
        return "parne"
    else:
        return "neparne"

def prvocislo(cislo):
    prvocis = True
    for i in range(2, cislo):
        if cislo % i == 0:
            prvocis = False
    return prvocis


a = int(input("Zadaj a: "))
b = int(input("Zadaj b:"))
sucet = sucet(a, b)
print(f"Súčet čisel {a} + {b} = {sucet} ")
print(f" číslo {a} je {parne(a)}")
print(f" číslo {b} je {parne(a)}")
if prvocislo(a) == True:
    print(f"čislo {a} je prvocislo!")
else:
    print(f"čislo {a} nie je prvocislo!")
if prvocislo(a) == True:
    print(f"čislo {b} je prvocislo!")
else:
    print(f"čislo {b} nie je prvocislo!")