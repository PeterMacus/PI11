fmena = open("mena.txt", "r", encoding="utf-8")  #otvorí súbor mena.txt na čitanie
#fmena = open("C:/dokumenty/men.txt", "r") absolutna cesta k suboru

while True:
    riadok = fmena.readline()
    if riadok == "":
        break
    print(riadok[:-1]) # [:-1] vypíše všetky znaky od nultého po predposledný



fmena.close() #zatvorenie súboru , vždy treba!!!!!!!!!!!!!!