# Дано целое положительное число. Вывести числа в порядке справа налево.

try:
  num = int(input("Введите целое положительное число: "))

  if num < 0:
    print("Вы ввели не положительное число!")
  else:
    num_str = str(num) 
    for char in num_str[::-1]: 
      print(char, end='')
      
  print()
      
except:
  print("Что-то пошло не так!")