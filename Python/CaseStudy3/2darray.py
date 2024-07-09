def generate_2d_array(X, Y):
    array = [[0 for j in range(Y)] for i in range(X)]
    for i in range(X):
        for j in range(Y):
            array[i][j] = i * j
    return array

# Example usage:
X, Y = 3, 5
print("2-Dimensional Array:")
print(generate_2d_array(X, Y))
