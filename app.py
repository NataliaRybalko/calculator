operation = input('''
Please type what would you like to do:
+ for addition
- for substraction
/ for division
''')

number_1 = float(input('Enter your first number'))
number_2 = float(input ('Enter your second number'))

if operation == '+':
    print(number_1 + number_2)

elif operation == '-':
    print(number_1 - number_2)

elif operation == '/':
    print(number_1 / number_2)