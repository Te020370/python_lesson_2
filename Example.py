#Задачи на циклы и оператор условия------
#----------------------------------------

'''
Задача 1
Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
'''
print("Task_1")
i = 0
while i < 5:
    i += 1
    print("String", i, " - 0")
print("____________________")
'''
Задача 2
Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.
'''
print("Task_2")
sum = 0
for i in range(10):
    answer = int(input("Напишите любую цифрy:  "))
    if answer == 5:
        sum +=1
print('Количество 5 равно', sum)
print('____________________')

''' 
Задача 3 
Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран. 
'''
print("Task_3")
sum = 0
for i in range(1,101):
    sum += i
print (sum)
print('____________________')
''' 
Задача 4 
Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран. 
'''
print("Task_4")
result_mult = 1
for i in range(1,11):
    result_mult *= i
print (result_mult)
print('____________________')

''' 
Задача 5 
Вывести цифры числа на каждой строчке. 
'''
print("Task_5")
integer_number = 4554
# print(integer_number%10,integer_number//10)
while integer_number > 0:
    print(integer_number % 10)
    integer_number = integer_number // 10
print('____________________')

''' 
Задача 6 
Найти сумму цифр числа. 
'''
print("Task_6")
number = 505337
sum = 0
while number > 0:
    sum += number % 10
    number = number // 10
print(sum)
print('____________________')

''' 
Задача 7  
Найти произведение цифр числа. 
'''
print("Task_7")
number = 55
multi = 1
while number > 0:
    multi *= number % 10
    number = number // 10
print(multi)
print('____________________')

''' 
Задача 8
Дать ответ на вопрос: есть ли среди цифр числа 5? 
'''
print("Task_8")
integer_number = 12345
while integer_number > 0:
    if integer_number%10 == 5:
        print('Yes')
        break
    integer_number = integer_number//10
else: print('No')
print('____________________')

'''
Задача 9 
Найти максимальную цифру в числе 
'''
print("Task_9")

integer_number = 12345
temp = 0
while integer_number > 0:
    if integer_number%10 > temp:
        temp = integer_number%10
    integer_number =  integer_number//10
print(temp)
print('____________________')

''' 
Задача 10 
Найти количество цифр 5 в числе 
'''
print("Task_10")
integer_number = 12345
count = 0
while integer_number > 0:
    if integer_number%10 == 5:
        count +=1
    integer_number = integer_number//10
print(count)
print('____________________')