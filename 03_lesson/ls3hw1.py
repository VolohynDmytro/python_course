result = None

num1_input = int(input("Введите число для делениея: "))

num2_input = int(input("Введите делитель(кроме нуля): "))

if num2_input != 0:

    operation = input("Выберите операцию: \b Деление '/' \b Умножение '*' \b Сочитание '+' \b Вычитание '-' ")

    if operation == '*':
        result = num1_input * num2_input
        print(result)
    elif operation == '/':
        result = num1_input / num2_input
        print(result)
    elif operation == '+':
        result = num1_input + num2_input
        print(result)
    elif operation == '-':
        result = num1_input - num2_input
        print(result)

else:
    print('ДЕЛИТЕЛЬ НЕ ДОЛЖЕН РАВНЯТЬСЯ НУЛЮ')