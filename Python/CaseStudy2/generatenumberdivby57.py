import random

random_list = random.sample([x for x in range(1, 1001) if x % 5 == 0 and x % 7 == 0], 5)
print(random_list)
