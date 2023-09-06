import random
import time

from solution import solution

elapsed_time = 0
while elapsed_time < 3:
    n, m = random.choice(range(1000, 10 ** 5, 1000)), random.randint(1, 10)
    a_list = [random.choice(range(1000, 10000, 1000)) for _ in range(m)]
    start = time.perf_counter()
    answer = solution(n, m, a_list)
    end = time.perf_counter()
    if isinstance(answer, int):
        print(answer)
    else:
        print(answer[0])
        print(*answer[1])
    elapsed_time = end - start
    print(elapsed_time)
