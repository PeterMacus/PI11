# if "a" in "aeiouy":
#     print("samohláska")
slovo = input("Zadaj slovo:")
sa = 0
sp = 0
for i in slovo:
    if i in "aeiouy":
        sa += 1
    else:
        sp += 1

print(f"Samoglasky: {sa}")
print(f"Spoluhlasky: {sp}")