def hviezdy(pocet_riadkov, pocet_hviezd):
    for i in range(pocet_riadkov):
        for j in range(pocet_hviezd):
            print("*", end="")
    print()


hviezdy(2, 12)
print("HEllo")
hviezdy(1, 5)
print("World!")
hviezdy(5, 4)