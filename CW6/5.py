#Dany jest ciąg zer i jedynek zapisany w tablicy T[N]. Proszę napisać funkcję, która odpowiada
#na pytanie czy jest możliwe pocięcie ciągu na kawałki z których każdy reprezentuje liczbę pierwszą. Długość
#każdego z kawałków nie może przekraczać 30. Na przykład dla ciągu 111011 jest to możliwe, a dla ciągu
#110100 nie jest możliwe.

def min_size_matching_subset_sum(seq):
    min_values_count = len(seq)+1
    min_count_sum = 0

    def recur(idx=0, sum_values=0, sum_indices=0, values_count=0):
        nonlocal min_values_count, min_count_sum

        if values_count < min_values_count and min_values_count > 1:

            if values_count and sum_indices == sum_values:
                min_values_count = values_count
                min_count_sum = sum_values

            elif idx < len(seq):
                recur(idx+1, sum_values + seq[idx], sum_indices + idx, values_count+1)
                recur(idx+1, sum_values, sum_indices, values_count)

    recur()

    return min_count_sum if min_values_count <= len(seq) else None
