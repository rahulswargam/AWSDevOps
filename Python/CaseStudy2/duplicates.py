original_list = [12,24,35,24,88,120,155,88,120,155]
unique_list = []
for num in original_list:
    if num not in unique_list:
        unique_list.append(num)
print(unique_list)
