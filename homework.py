# emails = ["Jack, 123, jack@gmail.com", "Sun, 500, sun2@yahoo.com", "Achmed, 200, achmed@gmail.com",
#      "Sven, 717, sven@gmail.com"]

# input_email = input("Please enter your email: ")
# input_password = input("Please enter your password: ")

# for i in emails:
#     i = i.split(", ")
#     if i[1] == input_password and i[2] == input_email:
#         print("")
#         print("Welcome...")
#         break
# else:
#     print("Wrong password. Please try again") 
        

# #add more comments
# #meaningful variable names
# #wrong password/user name
# #print a welcome message including the name






#class Investments():
#     def __init__(self, deposits, interest_rate, number_of_years_you_plan_to_invest_for, simple_or_compound):
#         self.deposits = deposits
#         self.interest_rate = interest_rate
#         self.number_of_years_you_plan_to_invest_for = number_of_years_you_plan_to_invest_for
#         self.simple_or_compound = simple_or_compound
#
#
# CORRECTIONS v START HERE
# investment = 1
# bond = 2
# user_choice = input("wht type of calculation do you wanna do please enter 1 for inverstme or 2 for bond: ")
#
# if user_choice == 1:
#     inpu

# print("Choose either 'investment' or 'bond' to proceed: ")
# print("")
# print("investment        - to calculate the amount of interest you'll earn on interest")
# print("bond              - to calculate the amount you'll have to pay on a home loan")
#
# print("")
# input("1 for investment:\n2 for bond: ")


# class Car:
#     def __init__(self, wheels, engine, body):
#         self.wheels = wheels
#         self.engine = engine
#         self.body = body

#     def __str__(self) -> str:
#         return f"Your car has:{wheels} wheels, {engine} Engine, and {body} body"


# wheels = input("Please enter your cars' wheels: ")
# engine = input("Please enter your cars' engine: ")
# body = input("Please enter your cars' body: ")



# car = Car(wheels, engine, body)

# print(car)










## HOMEWORK ##

# List of registered users, emails and their passwords
user_details = ["Jack, 123, jack@gmail.com", "Sun, 500, sun2@yahoo.com", "Achmed, 200, achmed@gmail.com",
     "Sven, 717, sven@gmail.com"]

# Code written for them to login
# Code also checks if they are registered, if they used the correct email and password


input_name = input("Please enter your name: ")
print("")
print(f"Hello {input_name}")
print("")
login = False

input_email = input("Please enter your email: ")
input_password = input("Please enter your password: ")



while login == False:
    for i in user_details:
        i = i.split(", ")
        if i[1] == input_password and i[2] == input_email:
            print("")
            print("Welcome...")
            login = True
            break
    # If there is a user error, it will ask them to try again
    else:
        print("")
        print("Email or password is incorrect. Please try again")
        input_email = input("Please enter your email: ")
        input_password = input("Please enter your password: ")
        

# completeness 4/4
# correctness 3/4
# documentation 1/4
# Styl2 3/4
