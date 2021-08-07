  
# Дано целое число m, задающее номер месяца года.
# Выведите строку — название времени года, соответствующего данному месяцу.
# Формат входных данных: дано целое число m (1 ≤ m ≤ 12).
# Формат выходных данных: требуется вывести название времени года

# TODO: your code here
month = int(input("month:"))
if 9 <= month <= 11:
	print ("Autumn")
elif 6 <= month <= 8:
	print ("Summer")
elif 3 <= month <= 5:
	print ("Spring")
else:
	print ("Winter")
