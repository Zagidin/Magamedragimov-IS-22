try:
    num = int(input('Введите трёхзначное число: '))
    a, b, c = num // 100, (num // 10) % 10, num % 10
    
    if a != b != c:
        print('Все цифры данного числа различны')
    else:
        print('Все цифры данного числа равны')
    
except:
    print('Не соответствует условию!')