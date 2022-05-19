names = ["John", "Jerry", "Sun", "Oliver", 'kaka']
# #change a value in the list names
# names[2] = "light"
# #print the list
# print(names)
# #iterate and print each item
# for i in names:
#     print(i[0], "This is the initial of name", i)

#difference between add and append

"""
cars = ["VW", "Toyota", "Ford", "Kia"]
cars.append("Isuzu")
print(cars)
cars_and_names = cars + names
print(cars_and_names)
cars.append(names)
print(cars)
print(len(cars))"""

#dictionaries

#if / elif / else
""" 
equal to == 
not equal is !=  
greater than is >
less than is <
less than or equal to is <=
greater than or equal to is >=
to check if something is literally something is
to check if something is inside a container we use the function in
to check if a string starts with a certain character(s) we use the function startswith()
to check if a string ends with a certain character(s) we use endswith()""" 

emails = ["john@company.com", "jerry@petrol.com", "sue@education.co.za", "tony@me.com"]
user_email = input("Enter your email: ")


if user_email in emails:
    print("Yes")
else:
    print("No")



