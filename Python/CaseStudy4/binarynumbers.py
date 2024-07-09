def check_divisibility(binary_numbers):
    numbers = binary_numbers.split(',')
    divisible_by_5 = [num for num in numbers if int(num, 2) % 5 == 0]
    print(",".join(divisible_by_5))

# Example usage:
binary_numbers = "0100,0011,1010,1001"
check_divisibility(binary_numbers)
