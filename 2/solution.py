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
    s = input()
    solution(s)
