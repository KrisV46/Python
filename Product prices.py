product1 = int(input('First price'))
product2 = int(input('Second price'))
product3 = int(input('Third price'))
if product1 >= product2:
    if product1 >= product3:
        print('first product:', product1)
    else:
        print('third product:', product3)
else:
    if product2 >= product3:
        print('second product:', product2)
    else:
        print('third product:',product3)