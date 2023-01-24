#

def rec(A, idx=0, idxsum=0, tabsum=0, emptyans=True):
        if not emptyans and idxsum == tabsum:
            return tabsum
        if len(A) == idx:
            return float('inf')
        anssum1 = rec(A, idx + 1, idxsum + idx, tabsum + A[idx], False)
        anssum2 = rec(A, idx + 1, idxsum, tabsum, emptyans)
        return min(anssum1, anssum2)

print(rec([0,1,2,3,4]))