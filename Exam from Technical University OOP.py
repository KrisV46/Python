class Medicine:
    def __init__(self,med_id, med_name, manufacturer, price, quantity):
        self.med_id = med_id
        self.med_name = med_name
        self.manufacturer = manufacturer
        self.price = price
        self.quantity = quantity


    def Display(self):
        print(f'{self.med_id}, {self.med_name}, {self.manufacturer}, {self.price}, {self.quantity}')
    
    def __repr__(self):
        print(f'{self.med_id}, {self.med_name}, {self.manufacturer}, {self.price}, {self.quantity}')
    
    def Search_by_name(self, name):
        for x in medic_list:
            if name == x.med_name:
                print(x)
    def Sale(self, name, quantity):
        for x in medic_list:
            if x.med_name == name and x.quantity == quantity:
                print(x.quantity - quantity)
    def Purchase(self, name, quantity):
        for x in medic_list:
            if x.med_name == name:
                print(x.quantity + quantity)
medic_list = []
while True:
    med_id = int(input("Enter number: "))
    if med_id == 0:
        break
    med_name = input("Enter name: ")
    manufacturer = input("Enter manufacturer: ")
    price = int(input("Enter price: "))
    quantity = int(input("Enter quantity: "))
    medic_list.append(Medicine(med_id,med_name,manufacturer,price, quantity))

def Sort_Meds(sex):
    print(sorted(sex, key= lambda x:x.med_name))

def minimal_quantity_from_manifacurer(manufacturer, medic_list):
    min_quant =[x for x in medic_list if manufacturer == x.manufacturer]
    print(min(min_quant, key = lambda x:x.quantity))


for x in medic_list:
    x.Search_by_name("Aspirin")
    break
#Medicine.Search_by_name(medic_list, "Aspirin")

Medicine.Sale(medic_list, "Nurofen", 5)

Medicine.Purchase(medic_list, "Analgin", 7)

Sort_Meds(medic_list)
