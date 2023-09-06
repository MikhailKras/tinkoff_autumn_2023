def solution(n, start_seq, end_seq):
    if n == 1:
        return "YES"

    start_seq_count_dict, end_seq_count_dict = {}, {}
    for start_seq_elem, end_seq_elem in zip(start_seq, end_seq):
        start_seq_count_dict[start_seq_elem] = start_seq_count_dict.get(start_seq_elem, 0) + 1
        end_seq_count_dict[end_seq_elem] = end_seq_count_dict.get(end_seq_elem, 0) + 1
    if start_seq_count_dict != end_seq_count_dict:
        return "NO"

    left, right = 0, 1
    non_decrease_seqs_indexes = []
    while right < n:
        if end_seq[right - 1] <= end_seq[right]:
            right += 1
        else:
            if right - 1 != left:
                non_decrease_seqs_indexes.append((left, right - 1))
            left = right
            right += 1

    if left < n - 1:
        non_decrease_seqs_indexes.append((left, right - 1))
    left, right = 0, n-1
    while left <= right and (start_seq[left] == end_seq[left] or start_seq[right] == end_seq[right]):
        if start_seq[left] == end_seq[left]:
            left += 1
        if start_seq[right] == end_seq[right]:
            right -= 1
    for left_subseq, right_subseq in non_decrease_seqs_indexes:
        if left >= left_subseq and right <= right_subseq:
            return "YES"
    return "NO"


if __name__ == '__main__':
    n = int(input())
    start_seq = list(map(int, input().split()))
    end_seq = list(map(int, input().split()))
    print(solution(n, start_seq, end_seq))
