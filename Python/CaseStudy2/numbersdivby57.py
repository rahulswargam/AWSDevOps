original_list = [12,24,35,70,88,120,155]
result = [x for x in original_list if x % 5 != 0 or x % 7 != 0]
print(result)
