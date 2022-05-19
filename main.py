









def car_parts(wheels, body, doors, engine, reliability, safety, mileage):
    
    print('                              ')
    print('CAR REPORT')
    print('******************************')
    print('WHEELS:', wheels)
    print('BODY:', body)
    print('ENGINE:', engine)
    print('RELIABILITY:', reliability)
    print('SAFETY:', safety)
    print('MILEAGE:', mileage)
    print('******************************')

wheels = input("Enter Wheels type: ")
body = input("Enter body type: ")
doors = input("Enter doors amount: ")
engine = input("Enter cyclinder amount: ")
reliability = input("Enter reliability rating: ")
safety = input("Enter safety rating: ")
mileage = input("Enter mileage: ")


car_parts(wheels, body, doors, engine, reliability, safety, mileage)



# class car():
#     def __init__(self, brand, type):
#         self.brand = brand
#         self.type = type

#     def print_car(self):
#         print (f'Your car brand is {self.brand}, and it is a {self.type} type car')

# c1 = car('VW', 'compact')
# c1.print_car()
