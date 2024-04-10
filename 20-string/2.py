retazec = input("Napíš čo chceš:")
for i, znak in enumerate(retazec):
    print(i, znak)
for i, znak in enumerate(retazec[::-1]):
    print(-i, znak)