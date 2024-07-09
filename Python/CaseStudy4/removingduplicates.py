def remove_duplicates(input_str):
    words = input_str.split()
    unique_words = sorted(set(words))
    print(" ".join(unique_words))

# Example usage:
input_str = "hello world and practice makes perfect and hello world again"
remove_duplicates(input_str)
