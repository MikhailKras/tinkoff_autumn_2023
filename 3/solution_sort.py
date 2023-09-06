def solution(n, start_seq, end_seq):
    if n == 1:
        return "YES"

    start_seq_count_dict, end_seq_count_dict = {}, {}
    for start_seq_elem, end_seq_elem in zip(start_seq, end_seq):
        start_seq_count_dict[start_seq_elem] = start_seq_count_dict.get(start_seq_elem, 0) + 1
        end_seq_count_dict[end_seq_elem] = end_seq_count_dict.get(end_seq_elem, 0) + 1
    if start_seq_count_dict != end_seq_count_dict:
        return "NO"

    left, right = 0, n-1
    while left <= right and (start_seq[left] == end_seq[left] or start_seq[right] == end_seq[right]):
        if start_seq[left] == end_seq[left]:
            left += 1
        if start_seq[right] == end_seq[right]:
            right -= 1

    if sorted(start_seq[left:right + 1]) == end_seq[left:right + 1]:
        return "YES"

    return "NO"


if __name__ == '__main__':
    n = int(input())
    start_seq = list(map(int, input().split()))
    end_seq = list(map(int, input().split()))
    print(solution(n, start_seq, end_seq))
