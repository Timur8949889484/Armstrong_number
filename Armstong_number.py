def armstrong_number(number):
    # Если входное значение - целое число, преобразуем его в строку
    if isinstance(number, int):
        number_str = str(number)
    elif isinstance(number, str):
        # Проверка на наличие букв в строке
        if any(char.isalpha() for char in number):
            return "Ошибка: ввод содержит недопустимые символы (буквы)."
        number_str = number
    else:
        return "Ошибка: недопустимый тип данных. Ожидалась строка или целое число."

    # Преобразование строки в целое число
    try:
        number = int(number_str)
    except ValueError:
        return "Ошибка: ввод не является числом."

    # Проверка числа Армстронга
    digits = list(map(int, number_str))
    power = len(digits)

    armstrong_sum = sum(digit ** power for digit in digits)

    return armstrong_sum == number


# Примеры использования
print(armstrong_number(371))  # True
print(armstrong_number(9474))  # True
print(armstrong_number(123))  # False
print(armstrong_number("371"))  # True
print(armstrong_number("9474"))  # True
print(armstrong_number("123"))  # False
print(armstrong_number("371g"))  # Ошибка: ввод содержит недопустимые символы (буквы).
print(armstrong_number("12a3"))  # Ошибка: ввод содержит недопустимые символы (буквы).
print(armstrong_number([371]))  # Ошибка: недопустимый тип данных. Ожидалась строка или целое число.