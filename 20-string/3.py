#šifrovanie cezarovou šifrou
ret = input("Zadaj reťazec")
posun = input("ZAdaj posun pre kodovanie:")
#print(ord(ret))
for i in ret:
    print(i,"", ord(i))

ret_kod = ""
for i in range(len(ret)):
    ret_kod += chr(ord(ret[i])+1)

print(f"Zakodovany retazec: {ret_kod}")