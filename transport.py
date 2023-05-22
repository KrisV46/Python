
distance = int(input("Enter km: "))
day_night = input("Enter day or night: ")
day_night = day_night.lower()
price = 0.00
taxiprice = 0.00
if day_night == 'day':
    taxiprice = 0.79
else:
    taxiprice = 0.90
if distance < 20:
    price = 0.70 + distance * taxiprice
elif distance < 100:
    price = distance * 0.09 
else:
    price = distance * 0.06
print (price)
    
    
