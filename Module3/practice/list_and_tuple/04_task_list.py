# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -10 до 10.
# Вывести на экран сумму всех положительных элементов.

# TODO: your code here
random_list = [-10, 3, 4, 2, 5, -8]
i = 0
sum = 0
for num in random_list:
    if num > 0:
        i += 1
        sum += num
print (sum)
