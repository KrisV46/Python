type_of_dessert = input("Enter the type of dessert: ")
type_of_dessert = type_of_dessert.lower()
if type_of_dessert == 'cake':
    flavour = input("enter the type of the cake ")
    flavour = flavour.lower()
    if flavour == 'chocolate':
        print('Try the Prague cake!')
    else:
        print("How about a honey cake? ")
else:
    print("call us to check availability")