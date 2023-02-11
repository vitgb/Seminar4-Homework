# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. 
# n - кол-во элементов первого множества. 
# m - кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18

# 6 12

n = int(input('Enter number of elements of the first set: '))
m = int(input('Enter number of elements of the second set: '))

list1 = [0]*n
list2 = [0]*m

for i in range(len(list1)):
    list1[i] = int(input(f"Enter the value of {i}'th element: "))
print (list1)

for i in range(len(list2)):
    list2[i] = int(input(f"Enter the value of {i}'th element: "))
print (list2)

print(sorted(set(list1).intersection(list2)))
# or
print(sorted(set(list1) & set(list2)))