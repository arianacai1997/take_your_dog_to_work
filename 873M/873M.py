from _collections import Counter
class Solution:
    def lenLongestFibSubseq(self, A) -> int:
        sA = set(A)
        B = Counter()
        ans = 0
        for i in reversed(range(len(A))):
            a = A[i]
            for b in A[i + 1:]:
                c = a + b
                if c in sA:
                    B[a, b] = B[b, c] + 1
                    # if recording B[b,c] = B[a,b]+1, everything is counted 1. We are tracking back like 3+5, 2+3, 1+2.
                    # So we want the 1+2 to be counted the most, which means the smaller pair should increase its value.
                    ans = max(ans, B[a, b] + 2)
                    # [a, b, c] = [1 ,2, 3], B[b, c] = 1
                if c > A[-1]:
                    break  # the inner loop needn't continue
        return ans if ans >= 3 else 0

    def inorderloop(self, A) -> int:
        sA = set(A)
        B = Counter()
        ans = 0
        for i in range(len(A)):
            a = A[i]
            for b in A[:i]:  # b is the smalles and does not to be recorded
                c = a + b
                if c in sA:
                    B[a, c] = B[b, a] + 1
                    ans = max(ans, B[a, c] + 2)
                if c > A[-1]:
                    break
        return ans if ans >= 3 else 0