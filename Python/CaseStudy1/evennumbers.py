def is_all_even(num):
    for digit in str(num):
        if int(digit) % 2 != 0:
            return False
    return True

even_numbers = []
for number in range(1000, 3001):
    if is_all_even(number):
        even_numbers.append(str(number))

print(",".join(even_numbers))
