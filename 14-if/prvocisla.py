while True:
    n = int(input("Zadaj N (Pre ukončenie zadaj 0): "))
    for cislo in range(2, (n // 2):
        pocet - 0
        #print("Delitele:", end=" ")
        for delitel in range(1, cislo + 1):
            if cislo % delitel == 0:
                 #print(delitel, end=" ")
                 pocet += 1 #pocet = pocet + 1

        #print("počet delitelov je:", pocet)
        if pocet == 2:
            print(cislo, end=" ")
    print()
    if n == 0:
        break