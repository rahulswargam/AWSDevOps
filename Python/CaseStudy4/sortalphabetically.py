def sort_words(input_str):
    words = input_str.split(',')
    sorted_words = sorted(words)
    print(",".join(sorted_words))

# Example usage:
input_str = "without,hello,bag,world"
sort_words(input_str)
