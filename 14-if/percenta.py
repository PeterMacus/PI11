max_bodov = 30
pocet_bodov = int(input("Zadaj počet bodov: "))
percenta = (pocet_bodov / max_bodov) * 100
print(f"Ziskal si {round(percenta, 2)}%")
# if percenta >= 90:
#     print(" Vyborny")
# else:
#     if percenta >= 75:
#         print("chvalitebny")
#     else:
#         if percenta >= 50:
#             print("dobry")
#         else:
#             if percenta >= 30:
#                 print("Dostatočny")
#             else:
#                 print("nedostatočný")

if percenta >= 90:
    print("vyborny")
elif 75 <= percenta < 90:
    print("chvalitebny")
elif 50 <= percenta < 75:
    print("dobry")
elif 30 <= percenta < 50:
    print("dostatocny")
else:
    print("nedostatocny")