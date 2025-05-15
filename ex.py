import random

num=random.sample(range(1, 101), 10)
sorted_num=sorted(num, reverse=True)
second_high=sorted_num[1]

print(num)
print(second_high)
