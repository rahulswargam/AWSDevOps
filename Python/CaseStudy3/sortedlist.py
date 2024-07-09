def search_data(data_list, key):
    # Assuming data_list is already sorted
    if key in data_list:
        return f"{key} found in the list."
    else:
        return f"{key} not found in the list."

# Example usage:
data_list = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
key = 18
print(search_data(data_list, key))
