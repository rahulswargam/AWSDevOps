import math

def calculate_values(input_seq):
    C = 50
    H = 30
    results = []
    numbers = input_seq.split(',')

    for D in numbers:
        Q = math.sqrt((2 * C * int(D)) / H)
        results.append(str(round(Q)))

    print(",".join(results))

# Example usage:
input_seq = "100,150,180"
calculate_values(input_seq)
