def convert(number):
    result = ""
    if _divisible_by_3(number):
        result += "Pling"
    if _divisible_by_5(number):
        result += "Plang"
    if _divisible_by_7(number):
        result += "Plong"

    if result == "":
        return str(number)
    else:
        return result

def _divisible_by_3(number):
    return number % 3 == 0

def _divisible_by_5(number):
    return number % 5 == 0

def _divisible_by_7(number):
    return number % 7 == 0
