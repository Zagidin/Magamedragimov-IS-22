
#Практическая работа №4.
#Вариант 8.
#Задание 1:

seq = [3.5, 1.7, 2.8, 5.1, 4.3, 7.9, 6.2]
sum_of_num = 0

for num in seq:
  if num % 2 != 0:
    sum_of_num += num
  else:
      break

      print("Сумма всех нечетных чисел: ", sum_of_num)