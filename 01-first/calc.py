num1 = input('Enter a number: ')
num2 = input('Enter another number: ')
sum = float(num1) + float(num2)

if sum.is_integer():
    sum = int(sum)

print('Sum:', sum)