
while True:
    c = input('Выберите операцию: ')
    if c in '+-*/':
        break
    else:
        print('Ошибка ввода!')

amount = int(input('Сколько операндов? ')) 
count = 1
number = int(input(f'Введите {count} число: '))
result = number
number_str = str(number)
while (amount - 1) != 0:
    count += 1
    number = int(input(f'Введите {count} число: '))
    amount -= 1     
    if c == '+':
        result += number
    elif c == '-':
        result -= number
    elif c == '*':
        result *= number
    elif c == '/':
        result /= number
    number_str += c + str(number)
print(f'{number_str} = {result}')