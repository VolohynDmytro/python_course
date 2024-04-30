work: bool = True
while work:
    num1_input = int(input("Введите первое число: "))

    num2_input = int(input("Введите второе число: "))

    operation = input("Выберите операцию: \b Деление '/' \b Умножение '*' \b Сочитание '+' \b Вычитание '-' ")

    if operation == '*':
        result = num1_input * num2_input
        print(result)

    elif operation == '/' and num2_input == 0:
        print('На ноль делится')

    elif operation == '/':
        result = num1_input / num2_input
        print(result)

    elif operation == '+':
        result = num1_input + num2_input
        print(result)

    elif operation == '-':
        result = num1_input - num2_input
        print(result)

    to_continue = input("Хотите ли вы продолжить считать?(y/n): ")
    if to_continue == 'y':
        continue
    else:
        work = False
