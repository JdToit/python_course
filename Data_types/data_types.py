# Integers


"""integer1 = 15
integer2 = int(20)
print(type(integer1))
print(dir(integer2))
print(integer1.__add__)"""


# Floating-Point Numbers


"""
floating_point1 =7
floating_point2 = float(20.5)
print(type(floating_point1))
print(dir(floating_point2))"""


# Complex Numbers

"""
print(type(3j))
complex_number1 = 5j
complex_number2 = complex(5j)"""


# Strings
# review "\"
# Escape Sequences in Strings

"""
\	Backslash (\)
'	Single quote (')
"	Double quote (")
\n	ASCII Linefeed (adds newline)
\b	ASCII Backspace"""

# from multiprocessing.sharedctypes import Value


# S =  '"Hey what\'s up"'
###print(S)
"""
string1 = print("this me '("i'm cool)'")
string2 = \"""
Hello, (this is a multi-line
string\"""
print(string1)"""


# Raw Strings


# =raw_string = r"C\\:\Program \"Files\CPUID\HWMonitor"
# print(raw_string)


# Triple-Quoted Strings
# Boolean Type, Boolean Context, and “Truthiness”


"""
boolean_true = True
print(type(boolean_true))
boolean_false2 = bool()
print(boolean_false2 + 1)
print(boolean_true + 1)
if 1 == 2:
    print('Hello')
if 1:
    print(1)"""



# Built-In Functions
# example list (built-in functions):
    # data types
    # data structures
    #

"""
Sample_list = ['data types', 'data structures',]
print(Sample_list + Sample_list)
# print(dir(Sample_list))
# print(dir(bool()))
boolean_true = True
int_from_bool = int(boolean_true)
print(int_from_bool)"""
 


# Math
# review iterable
# review function
# review subscriptable


"""
import math
math_module = math
print(type(math_module))
print(dir(math_module))
# print(math_module[3])
number1 = ""
number2 = -1
number3 = 145
median_of_number = math.log(number2)
p = math.pi
#print(len(), len(number2), number3, p)
print(math.pow(2, 10))

# Type Conversion
string_of_number2 = bool(number2)
print(string_of_number2)"""

"""
list1 = [5, 10, 15]
string_of_list = str(list1)
print(string_of_list)
print(type(string_of_list))

for i in string_of_list:
    print(i)"""


# Iterables and Iterators





"""
list_of_letters = ['1', '1', '5']
string_exercise = "Hello"
for item in range(10):
    print("jean")
for item in string_exercise:
    print("tony")"""

"""
 print(type(list_of_letters))
 print(type(string_exercise))
 print(dir(list_of_letters))
 print(dir(string_exercise))"""

"""
chosen_number = int(input("Please enter a number between 1 and 5: "))



while chosen_number >= 5 or chosen_number <= 0:
    print("This is not a number between 1 and 5. Please try again")
    chosen_number = int(input("Please enter a number between 1 and 5: "))

print("This was a number between 1 and 5")"""
        

# Composite Data Type


# Functions
a = int(input("enter a number: "))
b = int(input("enter a number: "))

addition = (a + b)
print(addition)
    


# Classes, Attributes, and Inheritance
# Input/Output
# Variables, References, and Scope
# Miscellaneous


# s_dic = {'a':[1, 2, 3, 4], 'b': ["hello", "goodbye", "good day"], 'c':[True, False, True], 6 : [20, "hello", True, 120]}

# print(s_dic[6])

# loop through dictionary
# find values 
# 
# and append the string good to each Value

# outside the loop print the whole the dict

# for i in s_dic.items():
#     i[1].append('good')
#     print(i[1])

# print(s_dic)