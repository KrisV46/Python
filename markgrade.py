depozit = float(input("Enter depozit: "))
srok = int(input("Vuvedete meseci: "))
lihva = float(input("Enter lihva: "))
godishna = depozit * lihva
mesechna = godishna / 12
sum = srok * mesechna + srok
print(sum)
