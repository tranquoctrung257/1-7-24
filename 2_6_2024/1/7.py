import random
a = [1,2,3]

new_list = []

# for x in a:
#     new_list.append(x*2)
# print(new_list)

# hoặc
print([i*2 for i in a])
# để random 1 số lượng phần tử nhất định | k là số lượng phần tử cần radom ra
a = random.sample(range(1,100),k= 50)
print(a)

# để tính số giây chương trình chạy
import time

start = time.perf_counter()
print([i*2 for i in a])
stop = time.perf_counter()

print(f"{stop-start}s")