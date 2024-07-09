def count_case_letters(input_str):
    upper_count = sum(1 for char in input_str if char.isupper())
    lower_count = sum(1 for char in input_str if char.islower())
    print(f"UPPER CASE {upper_count}")
    print(f"LOWER CASE {lower_count}")

# Example usage:
input_str = "Hello world!"
count_case_letters(input_str)
