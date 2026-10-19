def is_armstrong_number(number):
    word = str(number)
    number_of_digits = len(word)
    digit_sum = 0
    for char in word:
        digit_sum = digit_sum + (int(char) ** number_of_digits)
    return number == digit_sum
