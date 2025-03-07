"""
Щоб виграти головний приз лотереї, необхідний збіг кількох номерів на лотерейному квитку з числами, що випали випадковим чином і в певному діапазоні під час чергового тиражу. Наприклад, необхідно вгадати шість чисел від 1 до 49 чи п'ять чисел від 1 до 36 тощо.

Вам необхідно написати функцію get_numbers_ticket(min, max, quantity), яка допоможе генерувати набір унікальних випадкових чисел для таких лотерей. Вона буде повертати випадковий набір чисел у межах заданих параметрів, причому всі випадкові числа в наборі повинні бути унікальні.


Вимоги до завдання:

Параметри функції:
min - мінімальне можливе число у наборі (не менше 1).
max - максимальне можливе число у наборі (не більше 1000).
quantity - кількість чисел, які потрібно вибрати (значення між min і max).
Функція генерує вказану кількість унікальних чисел у заданому діапазоні.
Функція повертає список випадково вибраних, відсортованих чисел. Числа в наборі не повинні повторюватися. Якщо параметри не відповідають заданим обмеженням, функція повертає пустий список.


Рекомендації для виконання:

Переконайтеся, що вхідні параметри відповідають заданим обмеженням.
Використовуйте модуль random для генерації випадкових чисел.
Використовуйте множину або інший механізм для забезпечення унікальності чисел.
Пам'ятайте, що функція get_numbers_ticket повертає відсортований список унікальних чисел.


Критерії оцінювання:

Валідність вхідних даних: функція повинна перевіряти коректність параметрів.
Унікальність результату: усі числа у видачі повинні бути унікальними.
Відповідність вимогам: результат має бути у вигляді відсортованого списку.
Читабельність коду: код має бути чистим і добре документованим.


Приклад: Припустимо, вам потрібно вибрати 6 унікальних чисел для лотерейного квитка, де числа повинні бути у діапазоні від 1 до 49. Ви можете використати вашу функцію так:

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)

Цей код викликає функцію get_numbers_ticket з параметрами min=1, max=49 та quantity=6. В результаті ви отримаєте список з 6 випадковими, унікальними та відсортованими числами, наприклад, [4, 15, 23, 28, 37, 45]. Кожен раз при виклику функції ви отримуватимете різний набір чисел.

"""

import random

def get_numbers_ticket(min:int, max:int, quantity:int)->list:

	if min < 1 or max > 1000 or quantity < min or quantity > max:
		return []
	else: 
		some_nums = range(min, max)
		list_of_random_numbers = random.sample(some_nums, quantity)
		sorted_list = sorted(list_of_random_numbers)
		return sorted_list 
		
		
print(get_numbers_ticket(1, 49, 6))



#NOTES:

# random.sample - повертає випадково вибрані елементи з послідовності (random.sample(obj, quantity)
# range(min, max) - генерує послідовність чисел від min до max (не включаючи max), 

"""
SORTED() VS SORT()

Пам'ятайте, що метод sort() змінює сам список, на якому він був викликаний. 
Якщо потрібно зберегти початковий порядок елементів, розгляньте можливість створення копії списку перед сортуванням або використай функцію sorted(), 
яка повертає новий відсортований список. Також sort() працює тільки зі списками, де всі елементи можуть бути порівняні між собою. Наприклад, спроба відсортувати список, 
який містить і цифри, і рядки, призведе до помилки.


Вбудований метод sorted() у Python використовується для сортування колекцій. Він відрізняється від методу sort(), 
який застосовується безпосередньо до списку, та змінює його: sorted() повертає новий відсортований об'єкт, 
залишаючи вихідний об'єкт без змін. Метод також використовує аргумент reverse=True, щоб відсортувати об'єкти у зворотному порядку, 
та за допомогою аргументу key можна вказати функцію, яка буде застосовуватися для визначення порядку сортування.

"""

