'''n = int(input("Vuvedete chislo"))
pozitivni = []
negativni = []

for i in range(n):
    m = int(input())
    if m >= 0:
        pozitivni.append(m)
    else:
        negativni.append(m)
print(pozitivni)
print(negativni)
print("Count of pozitivni", len(pozitivni))
print("sum of negativni", sum(negativni))

n = int(input("Enter a number: "))
word = input()
strings =[]
for i in range(n):
    k = int(input())
    strings.append(k)
print(strings)
for i in range(len(strings)-1, -1, -1):
    element = strings[i]
    if word not in element:
        strings.remove(element)
print(strings) ?????????????????????????????????
'''

n = int(input("Enter number: "))
intigers =[]
filtered = []
command = input("Enter a command: ")
for i in range(n):
    k = int(input("Enter something: "))
    intigers.append(k)

if command == 'odd':
    for number in intigers:
        if number % 2 == 0:
            filtered.append(intigers) # DA Q DOVURSHISH
elif command == 'even':            
    for number in intigers:
        if number % 2 != 0:
            filtered. append(intigers)
elif command == "negative":
    for number in intigers:
        if number < 0:
            filtered.append(intigers)
elif command == 'positive':
    for number in intigers:
        if number > 0:
            filtered.append(intigers)
print(filtered)