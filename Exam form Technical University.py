import random
n = int(input("Enter number: "))
if n <30 or n >100:
    raise ValueError("Ne stava")

list1 = [random.randint(20,600)for i in range(n)]
print(list1)
kratna_na_2 = len([x for x in list1 if x % 2 == 0])
print(kratna_na_2)
minimum = min([x for x in list1 if x % 7 == 3])
print(list1.index(minimum))
list2 = [x for x in list1 if x // 100 == 3 or x // 10 == 5]
print(list2)
index_max = list2.index(max(list2))
print(index_max)
mult = 1
for x in list2:
    if x % 10 == 3:
        mult *= x
print(mult)
