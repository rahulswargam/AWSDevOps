def capitalize_lines(input_lines):
    capitalized_lines = [line.strip().upper() for line in input_lines]
    for line in capitalized_lines:
        print(line)

# Example usage:
input_lines = [
    "Hello world",
    "Practice makes perfect"
]
capitalize_lines(input_lines)
