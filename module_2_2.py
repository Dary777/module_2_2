first = int(input('Введите любое целое число: '))
second = int(input('Введите любое целое число: '))
third = int(input('Введите любое целое число: '))

if first == second and second == third:
    print(3)
elif first == second or second == third or third == first:
    print(2)
else:
    print(0)
