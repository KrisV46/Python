points = int(input("Enter points:" ))
bonus = 0
if points < 100:
    bonus = 5
elif points > 100 or points <999:
    bonus = points * 0.2
else:
    bonus = points * 0.1
if points % 2 == 0:
    bonus = bonus + 1
if points % 10 == 5:
    bonus = bonus + 2
print(bonus)
sum = bonus + points
print(sum)
