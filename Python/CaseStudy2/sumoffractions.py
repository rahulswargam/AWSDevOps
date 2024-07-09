n = int(input("Enter a number: "))
result = sum([i/(i+1) for i in range(1, n+1)])
print(round(result, 2))
