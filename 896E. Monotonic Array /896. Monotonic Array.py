class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        return A == sorted(A) or A == list(reversed(sorted(A)))

        # len({x < y for x, y in zip(A, A[1:]) if x != y}) <= 1