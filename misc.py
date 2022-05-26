# users_details = ["toy, 123, toy@gmil.com", etc..]
#
# prompt user to enter email
# prompt user to enter password
#
# find a way to check if one of the string inside the list of user details contains
# the email and password
#
# hint:
#
# a = ["toy, 123, toy@gmil.com", "man, 000, ma@mi.com"]
#
# pass = "000"
#
# for i in a:
#     i = i.split(", ")
#     if i[1] == pass and i[2] == "ma@mi.com" :
#         print("you're good")


# input_email = input("Please enter your email: ")
# input_password = input("Please enter your password: ")
#
# user_details = ["Jack, 123, jack@gmail.com", "Sun, 500, sun2@yahoo.com", "Achmed, 200, achmed@gmail.com"]
# password =
#
# for i in user_details:
#     i = i.split(",")

# a = ["Jack, 123, jack@gmail.com", "Sun, 500, sun2@yahoo.com", "Achmed, 200, achmed@gmail.com",
#      "Sven, 717, sven@gmail.com"]
#
# input_email = input("Please enter your email: ")
# input_password = input("Please enter your password: ")
#
# for i in a:
#     i = i.split(", ")
#     if i[1] == input_password and i[2] == input_email:
#         print("")
#         print("You're good")


# city_to = int(input("Select the town you want it delivered to: \nEnter 1 to choose Cape Town.. \nEnter 2 to choose Pretoria.. \nEnter 3 to choose Durban.. "))
# city = ['Cape Town', 'Pretoria', 'Durban'][city_to - 1]
# parcel_weight = int(input(f"Select the weight category of the parcel to be delivered to:{city} \nEnter 1 to choose 0kg — 4kg R300.. \nEnter 2 to choose 5kg — 9kg R500.. \nEnter 3 to choose Over 10kg R700.. "))
# weight = ['4kg', '5kg — 9kg', '5kg — 9kg'][parcel_weight - 1]
# price = [300, 500, 700][parcel_weight - 1]
# courier_company = int(input(f"Select the courier company to deliver the parcel weight of {weight} to: {city} \nEnter 1 to choose ABC Couriers.. \nEnter 2 to choose Fast Track.. \nEnter 3 to choose Rest Assured.. "))
# courier = ['ABC Couriers', 'Fast Track', 'Rest Assured'][courier_company - 1]
#
# print('                                                ')
# print('DELIVERY REPORT - Created on 2016/08/26 13:44:35')
# print('***********************************************')
# print(f'TOWN:            {city}')
# print(f'WEIGHT:          {weight}')
# print(f'PRICE:           R{price}')
# print(f'VAT (14%):       R{price * 0.14}')
# print(f'TOTAL DUE:       R{(price) + (price * 0.14)}')
# print(f'COURIER:         {courier}')
# print('***********************************************')

# choosing = int(input("Choose either 'investment' or 'bond' from the menu below to proceed: \nEnter 1 to choose
# investment.. \nEnter 2 to choose bond.. "))


# class Investments():
#     def __init__(self, deposits, interest_rate, number_of_years_you_plan_to_invest_for, simple_or_compound):
#         self.deposits = deposits
#         self.interest_rate = interest_rate
#         self.number_of_years_you_plan_to_invest_for = number_of_years_you_plan_to_invest_for
#         self.simple_or_compound = simple_or_compound
#
#
# investment = 1
# bond = 2
#
#
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
#
#
# wheels = input("Please enter your cars' wheels: ")
# engine = input("Please enter your cars' engine: ")
# body = input("Please enter your cars' body: ")
#
# print("")
# print("Car report: ")
# print("")
# print(f"Your car has {wheels} wheels")
# print(f"Your car has a {engine} engine")
# print(f"Your car has a {body} body")
#
#
# car = Car("wheels", "engine", "body")

# List of registered users' emails
# emails = ["Jack, 123, jack@gmail.com", "Sun, 500, sun2@yahoo.com", "Achmed, 200, achmed@gmail.com",
#     "Sven, 717, sven@gmail.com"]

# Code written for them to login
# Code also checks if they are registered, if they used the correct email and password
# input_name = input("Please enter your name: ")
# print("")
# print(f"Hello {input_name}")
# print("")
# input_email = input("Please enter your email: ")
# input_password = input("Please enter your password: ")
#
# for i in emails:
#     i = i.split(", ")
#     if i[1] == input_password and i[2] == input_email:
#         print("")
#         print("Welcome...")
#         break
# else:
#     print("")
#     print("Wrong password. Please try again")

"""
# This will be a program that allows users to choose between accessing investments, or bonds
# Should a user choose investment, they will be able to enter their principle amount, their interest,
the amount of years they want to invest for, and whether they want to use simple or compound interest
# The printout will show their interest accrued, as well as their total amounts.


# First import math for the formula's to come
import math

# Let users choose between investments or bonds using an input method
investment = 1
bond = 2
user_choice = (input("Choose either 'investment' or 'bond' from the menu below to proceed: \n\nInvestment   - to "
                     "calculate the amount of interest you'll earn on interest \nBond         - to calculate the "
                     "amount you'll have to pay on a home loan\n\nEnter 1 for Investment\nEnter 2 for Bond... "))


# else/if code for if they choose investment
# input lines for them to enter their investing information
# printout displaying all their information, their interest, and their total
# also has the formulas for simple as well as compound interest

if user_choice == "1":
    print("")
    print("You have chosen investment")
    amount = float(input("What amount would you like to deposit: "))
    interest_rate = float(input("Enter the interest rate (only the number): "))
    years = float(input("Enter the number of years you plan on investing for: "))
    simple_or_compound = input("Enter whether you would like simple or compound interest: ")
    simple_interest = (amount * years * interest_rate)/100
    ci_future = amount * (math.pow((1 + interest_rate / 100), years))
    compound_interest = ci_future - amount
    print("")
    print("User results:")
    print("")
    print("Amount:   ",                     amount)
    print("Interest rate:   ",    interest_rate)
    print("Number of years:    ", years)
    print("Simple interest is: ", simple_interest)
    if simple_or_compound == "simple interest":
        print("")
        print("User results:")
        print("")
        print("Amount:   ", amount)
        print("Interest rate:   ", interest_rate)
        print("Number of years:    ", years)
        print("Simple interest is: ", simple_interest)
    elif simple_or_compound == "compound interest":
        print("")
        print("User results:")
        print("")
        print("Amount:   ", amount)
        print("Interest rate:   ", interest_rate)
        print("Number of years:    ", years)
        print("Compound interest is: ", compound_interest)

#elif code for if they choose bonds

elif user_choice == "2":
    print("")
    print("You have chosen bonds")

# error message for if there's any user error.
# gives the users the another chance to enter their information correctly

else:
    print("Error. Please try again")
    print("")
    user_choice = (input("Choose either 'investment' or 'bond' from the menu below to proceed: \n\nEnter 1 to choose "
                         "investment.. \nEnter 2 to choose bond.. "))

# code written for if they choose simple interest or compound interest

# if choice == "simple interest":
#     print("")
#     print("User results:")
#     print("")
#     print("Amount:   ", amount)
#     print("Interest rate:   ", interest_rate)
#     print("Number of years:    ", years)
#     print("Simple interest is: ", simple_interest)
# elif choice == "compound interest":
#     print("")
#     print("User results:")
#     print("")
#     print("Amount:   ", amount)
#     print("Interest rate:   ", interest_rate)
#     print("Number of years:    ", years)
#     print("Compound interest is: ", compound_interest)"""

"""
s_dic = {'a': [1, 2, 3, 4], 'b': ["hello", "goodbye", "good day"], 'c': [True, False, True],
         6: [20, "hello", True, 120]}

for i in s_dic.items():
    i[1].append('good')
    print(i[1])

print(s_dic)

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for i in thisdict:
  print(i[0:])"""

dictionary_practice = {'cars': ['Ford', 'Toyota', 'Honda'], 'speed': ['Fast', 'Moderate', 'Slow'],
                       'reliability': ['Great', 'Average', 'Poor']}


