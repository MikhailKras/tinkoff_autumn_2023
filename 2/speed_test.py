import random
import time


def solution(s):
    res = 0
    dct = {
        "s": 0,
        "h": 0,
        "e": 0,
        "r": 0,
        "i": 0,
        "f": 0
    }
    for char in s:
        if char in dct:
            dct[char] += 1
    min_chars = min(dct.values())
    if dct["f"] // 2 >= min_chars:
        res = min_chars
    print(res)


if __name__ == '__main__':
    for _ in range(1000):
        s = ''.join([random.choice('sheriff') for _ in range(2 * 10 ** 5)])
        start = time.perf_counter()
        solution(s)
        end = time.perf_counter()
        print(end - start)
