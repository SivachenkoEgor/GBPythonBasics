# 2. Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):
# Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
# Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.
# Внимание: использовать только арифметические операции!
# К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка,
# сумма цифр которых делится нацело на 7.
# * Решить задачу под пунктом b, не создавая новый список.


# with list
def is_div_by_seven_with_str(number):
    result = 0
    number_str = str(number)
    digits_sum = 0
    for inner_number in number_str:
        digits_sum += int(inner_number)
    if digits_sum % 7 == 0:
        result += number
    return result

def is_div_by_seven(number):
    result = 0
    temp = number
    while temp > 0:
        result += temp % 10
        temp //= 10
    if result % 7 == 0:
        result = number
    return result



task_list = [i ** 3 for i in range(1, 1000 + 1) if i % 2 == 1]
result_1 = 0
result_2 = 0
for number in task_list:
    result_1 += is_div_by_seven(number)
    result_2 += is_div_by_seven(number + 17)

print(result_1)
print(result_2)

# with no list

result_1 = 0
result_2 = 0
i = 1
while i <= 1000:
    number = i ** 3
    if number % 2 == 1:
        result_1 += is_div_by_seven(number)
        result_2 += is_div_by_seven(number + 17)
    i += 1

print(result_1)
print(result_2)