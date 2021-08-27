
numbers = []
number_count = int(input("Number of numbers > "))

for i in range(number_count):
    user_number = int(input(f"Number {i+1} > "))
    numbers.append(user_number)

sum_numbers = 0
for i in range(len(numbers)):
    sum_numbers += numbers[i]

length_numbers = len(numbers)
average_numbers = sum_numbers/length_numbers

print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[-1]}")
print(f"The smallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")
print(f"The number of numbers is {length_numbers}")
print(f"The sum of the numbers is {sum_numbers}")
print(f"The average of the numbers is {average_numbers}")


usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

username = input("Enter username >>> ")
if username in usernames:
    print("Access Granted")
else:
    print("Access Denied")
