# Write a function named sumDigits which takes a number as input and returns the sum of the absolute value of each of
# the number's decimal digits
def sum_digits(number):
    result = 0
    for letter in str(number):
        if letter in "+-":
            pass
        else:
            result += int(letter)

    return result

