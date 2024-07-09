sentence = input("Enter a sentence: ")

letters = sum(c.isalpha() for c in sentence)
digits = sum(c.isdigit() for c in sentence)

print(f"LETTERS: {letters}")
print(f"DIGITS: {digits}")
