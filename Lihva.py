depozit = float(input("Enter depozit: "))
srok = int(input("Vuvedete meseci: "))
lihva = float(input("Enter lihva: "))
godishna = depozit *(lihva *0.1)  
mesechna = godishna / 12
sum = srok * mesechna + srok
print(sum)