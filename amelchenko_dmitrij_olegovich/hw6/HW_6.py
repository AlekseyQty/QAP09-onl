#1.Validate
'''Задание оказалось сложным, попробую выполнить его позже'''

#2. Подсчет количества букв
orig_val = input('Введите слова: ')

def letter_count(orig_val) :
    dict_orig_val = {}
    for k in set(orig_val):
        if k == ' ':
            continue
        dict_orig_val[k] = orig_val.count(k)
    return dict_orig_val

dict_orig_val = letter_count(orig_val)
string_dict_orig_val=""

for key,val in dict_orig_val.items():
    string_dict_orig_val = string_dict_orig_val + key + str(val)

print(string_dict_orig_val)

# 3. Простейший калькулятор v0.1

def sum_num(x, y):
    return float(x) + float(y)


def calc_num(x, y):
    return float(x) - float(y)


def multip_num(x, y):
    return float(x) * float(y)


def divi_num(x, y):
    return float(x) / float(y)




while True:
    fun_num = input('1. Сложение \n2. Вычитание \n3. Умножение \n4. Деление \nВведите номер пункта меню: ')

    if fun_num == '':
        fun_num

    elif int(fun_num) > 4:
        fun_num

    elif int(fun_num) == 1:
        x = input('Введите первое число: ')
        y = input('Введите второе число: ')
        sum_num = sum_num(x, y)
        print(f'Ответ: {sum_num}')
        break

    elif int(fun_num) == 2:
        x = input('Введите первое число: ')
        y = input('Введите второе число: ')
        calc_num = calc_num(x, y)
        print(f'Ответ: {calc_num}')
        break

    elif int(fun_num) == 3:
        x = input('Введите первое число: ')
        y = input('Введите второе число: ')
        multip_num = multip_num(x, y)
        print(f'Ответ: {multip_num}')
        break

    elif int(fun_num) == 4:
        x = input('Введите первое число: ')
        y = input('Введите второе число: ')

        if (x, y) == 0:
            print(f'Деление на 0 невозможно!')
            fun_num

    else:
        if int(fun_num) == 4:
            x = input('Введите первое число: ')
            y = input('Введите второе число: ')
            divi_num = divi_num(x, y)
            print(f'Ответ: {divi_num}')
            break
