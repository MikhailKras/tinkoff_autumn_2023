def solution(n, m, a_list):
    a_list = [x for x in a_list for _ in range(2)]
    dp_dict = {0: 0}
    a_index = 0
    while n not in dp_dict and a_index < m * 2:
        keys = list(dp_dict.keys()).copy()
        for key in keys:
            if key + a_list[a_index] <= n:
                dp_dict[key + a_list[a_index]] = a_list[a_index]

        a_index += 1
    combination_bill = []
    if n in dp_dict:
        while n > 0:
            last_bill = dp_dict[n]
            n -= last_bill
            combination_bill.append(last_bill)
        return len(combination_bill), combination_bill
    else:
        return -1


if __name__ == '__main__':
    n, m = map(int, input().split())
    a_list = list(map(int, input().split()))
    answer = solution(n, m, a_list)
    if isinstance(answer, int):
        print(answer)
    else:
        print(answer[0])
        print(*answer[1])
