words = input("Enter a sequence of words separated by spaces: ")
word_list = words.split()
word_list.sort()

print("Sorted words:")
for word in word_list:
    print(word)
