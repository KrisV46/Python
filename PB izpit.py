'''cat = input()
pol = input()
if cat == 'Siamese' and pol == 'm':
    print(15 * (12 / 6) ,'cat months')
elif cat == 'Siamese' and pol =='f':
    print(16 * (12 / 6) , "cat months")

elif cat == 'British Shorthair' and pol == 'm':
    print(13 * (12 / 6) ,'cat months')
elif cat == 'British Shorthair' and pol =='f':
    print(14 * (12 / 6) , "cat months")
elif cat == 'Persian' and pol == 'm':
    print(14 * (12 / 6) ,'cat months')
elif cat == 'Persian' and pol =='f':
    print(15 * (12 / 6) , "cat months")
elif cat == 'Ragdoll' and pol == 'm':
    print(16 * (12 / 6) ,'cat months')
elif cat == 'Ragdoll' and pol =='f':
    print(17 * (12 / 6) , "cat months")
elif cat == 'American Shorthair' and pol == 'm':
    print(12 * (12 / 6) ,'cat months')
elif cat == 'American Shorthair' and pol =='f':
    print(13 * (12 / 6) , "cat months")
elif cat == 'Siberian' and pol == 'm':
    print(11 * (12 / 6) ,'cat months')
elif cat == 'Siberian' and pol =='f':
    print(12 * (12 / 6) , "cat months")
else:
    print(cat , 'is invalid cat!')'''



import decimal
cat = input()
pol = input()
if cat == 'Siamese' and pol == 'm':
    print(30 ,'cat months')
elif cat == 'Siamese' and pol =='f':
    print(decimal.Decimal(16 * (12 / 6)).normalize() , "cat months")
elif cat == 'British Shorthair' and pol == 'm':
    print(decimal.Decimal(13 * (12 / 6)).normalize() ,'cat months')
elif cat == 'British Shorthair' and pol =='f':
    print(decimal.Decimal(14 * (12 / 6)).normalize() , "cat months")
elif cat == 'Persian' and pol == 'm':
    print(decimal.Decimal(14 * (12 / 6)).normalize() ,'cat months')
elif cat == 'Persian' and pol =='f':
    print(decimal.Decimal(15 * (12 / 6)).normalize() , "cat months")
elif cat == 'Ragdoll' and pol == 'm':
    print(decimal.Decimal(16 * (12 / 6)).normalize() ,'cat months')
elif cat == 'Ragdoll' and pol =='f':
    print(decimal.Decimal(17 * (12 / 6)).normalize() , "cat months")
elif cat == 'American Shorthair' and pol == 'm':
    print(decimal.Decimal(12 * (12 / 6)).normalize() ,'cat months')
elif cat == 'American Shorthair' and pol =='f':
    print(decimal.Decimal(13 * (12 / 6)).normalize() , "cat months")
elif cat == 'Siberian' and pol == 'm':
    print(decimal.Decimal(11 * (12 / 6)).normalize() ,'cat months')
elif cat == 'Siberian' and pol =='f':
    print(decimal.Decimal(12 * (12 / 6)).normalize() , "cat months")
else:
    print(cat , 'is invalid cat!')
