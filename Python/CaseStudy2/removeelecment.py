original_list = [12,24,35,70,88,120,155]
indexes_to_remove = [0, 4, 5]
result = [original_list[i] for i in range(len(original_list)) if i not in indexes_to_remove]
print(result)
