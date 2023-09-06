import random
import time


def solution(n, s, lst):
    max_revolver = 0
    for cost in lst:
        if s >= cost > max_revolver:
            max_revolver = cost
    return max_revolver


if __name__ == '__main__':
    n = 2 * 10 ** 5
    for _ in range(1000):
        s = random.randint(1, 10**9)
        lst = [random.randint(1, 10**9) for _ in range(n)]
        start = time.perf_counter()
        solution(n, s, lst)
        end = time.perf_counter()
        print(end - start)
