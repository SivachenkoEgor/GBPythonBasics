# first task
def num_translate(input_string_digit):
    translate_dict = {
        "zero": "ноль",
        "one": "один",
        "two": "два",
        "three": "три",
        "four": "четыре",
        "five": "пять",
        "six": "шесть",
        "seven": "семь",
        "eight": "восемь",
        "nine": "девять",
        "ten": "десять",
    }
    return translate_dict.get(input_string_digit)


# second task
def num_translate_adv(input_string_digit: str):
    translate_dict = {
        "zero": "ноль",
        "one": "один",
        "two": "два",
        "three": "три",
        "four": "четыре",
        "five": "пять",
        "six": "шесть",
        "seven": "семь",
        "eight": "восемь",
        "nine": "девять",
        "ten": "десять",
    }
    if input_string_digit == input_string_digit.capitalize():
        return translate_dict.get(input_string_digit.lower()).capitalize()
    return translate_dict.get(input_string_digit)
# можно было тернарным оператором воспользоваться, но было длинно и некрасиво
# данные поместил внутри функций, хотя это не совсем корректно по следующей причине - по идее у нас должен быть класс,
# в котором будет атрибут со словарём, но поскольку такого класса нет я поместил словарь в тело функции
