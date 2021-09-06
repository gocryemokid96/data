import string
import random
while 1:
#ввод длины пароля
    n = int(input('Введите длину пароля: '))
    validsymbols = string.ascii_lowercase
#обработка условий возможности содержания цифр, заглавных букв и знаков препинания в пароле
    ci = bool(input('Может ли пароль содержать цифры? 1 - да, Enter - нет: '))
    if ci == 1:
        validsymbols += string.digits
    chl = bool(input('Может ли пароль содержать заглавные буквы? 1 - да, Enter - нет: '))
    if chl == 1:
        validsymbols += string.ascii_uppercase
    cp = bool(input('Может ли пароль содержать знаки пунктуации? 1 - да, Enter - нет: '))
    if cp == 1:
        validsymbols += string.punctuation
    mi = bool(input('Пароль обязательно должен содержать цифры? 1 - да, Enter - нет: '))
    mhl = bool(input('Пароль обязательно должен содержать заглавные буквы? 1 - да, Enter - нет: '))
    mp = bool(input('Пароль обязательно должен содержать знаки пунктуации? 1 - да, Enter - нет: '))
    fi, fhl, fp = 0, 0, 0
    password = []
    x = []
    for i in range(n):
        password.append(random.choice(validsymbols))
#обработка условий обязательного содержания цифр, заглавных букв и знаков препинания
    while len(x) != (int(mi) + int(mp) + int(mhl)):
        if mi == 1 and fi == 0 and ci == 1:
            for i in string.digits:
                if password.count(i) > 0:
                    x.append(i)
                    fi = 1
                    break
        if mhl == 1 and fhl == 0 and chl == 1:
            for i in string.ascii_uppercase:
                if password.count(i) > 0:
                    x.append(i)
                    fhl = 1
                    break
        if mp == 1 and fp == 0 and cp == 1:
            for i in string.punctuation:
                if password.count(i) > 0:
                    x.append(i)
                    fp = 1
                    break
        if len(x) != (int(mi) + int(mp) + int(mhl)):
            password.clear()
            password += x
            while len(password) < n:
                password.append(random.choice(validsymbols))
#ввод обязательных символов в пароле
    x2 = [item for item in input('Введите обязательные символы через пробел (не более ' + str(n - len(x)) + '): ' ).split()]
    if len(x2) < (n - len(x)):
        for i in x2:
            if len(i) > 1:
                x2.remove(i)
            if x.count(i) > 0:
                x2.remove(i)
        x += x2
        password.clear()
        password += x
        while len(password) < n:
            password.append(random.choice(validsymbols))
        random.shuffle(password)
    else:
        print('Введено слишком много символов')
#человекочитаемость
    word = []
    list1 = [["pet", "top", "cry"], ["cake", "rest", "baby"], ["young", "mouse", "night"], ["random", "flower", "beamer"], ["orderly", "article", 'obscure'], ["attitude", "division", "soulmate"]]
    r = bool(input('Сделать пароль более читаемым? 1 - да, Enter - нет: '))
    if r == 1:
        n1 = n - len(x)
        if n1 <= 2:
            print('Не получится сделать более читаемый пароль')
        else:
            password.clear()
            if 3 <= n1 <= 8:
                word = list1[n1 - 3][random.randint(0, 2)]
                password += word
                word = ""
            if n1 > 8:
                for i in range(n1 // 8):
                    word = list1[5][random.randint(0, 2)]
                    password += word
                    word = ""
                if n1 % 8 > 2:
                    word = list1[(n1 % 8) - 3][random.randint(0, 2)]
                    password += word
                    word = ""
                elif 0 < n1 % 8 <= 2:
                    for i in range (n1 % 8):
                        password += random.choice(string.ascii_lowercase)
            password += x
    print('Ваш пароль: ' + ''.join(password))