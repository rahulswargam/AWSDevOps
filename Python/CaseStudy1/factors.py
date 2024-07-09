def find_factors(num):
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    return factors

def even_or_odd(num):
    if num % 2 == 0:
        return "even"
    else:
        return "odd"

number = int(input("Enter a number: "))
factors = find_factors(number)

print(f"Factors of {number} are:")
for factor in factors:
    print(f"{factor} is {even_or_odd(factor)}")
