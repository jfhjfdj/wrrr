numbers = [3, 7, 12, 5, 9]
sum_numbers = sum(numbers)
print("Сумма всех чисел:", sum_numbers)

print("Четные числа")
for num in numbers:
    if num % 2 == 0:
        print(num)


max_number = max(numbers)
print("Самое большое число:", max_number)

print("Список в обратном порядке")
for i in range(len(numbers) - 1, -1, -1):
    print(numbers[i])

print("Таблица умножения на 5")
for i in range(1, 11):
    print("5 x {i} = {5 * i}")