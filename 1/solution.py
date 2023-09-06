def solution(s, lst):
    max_revolver = 0
    for cost in lst:
        if s >= cost > max_revolver:
            max_revolver = cost
    print(max_revolver)


if __name__ == '__main__':
    n, s = map(int, list(input().split()))
    lst = map(int, list(input().split()))
    solution(n, s, lst)
