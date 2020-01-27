def arabic_to_roman(number):
    arabic = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

    roman = ["M", "CM", "D", "CD", "C", "XC",
             "L", "XL", "X", "IX", "V", "IV", "I"]

    i = 0
    result = ""

    while number:
        div = number // arabic[i]
        number %= arabic[i]

        while div:
            result += roman[i]
            div -= 1
        i += 1

    return result
