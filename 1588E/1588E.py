class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        """Enumerate all possible odd length of subarray.
Time O(n^3)
Space O(1)
"""
        l = len(arr)
        res = 0
        for leng in range(1, l+1, 2):
            for i in range(l-leng+1):
                res += sum(arr[i:i+leng])
        return res

    def sumOddLengthSubarrays2(self, arr):
        """Consider the subarray that contains A[i],
we can take 0,1,2..,i elements on the left, we have i + 1 choices.
we can take 0,1,2..,n-i-1 elements on the right, we have n - i choices.

In total, there are (i + 1) * (n - i) subarrays, that contains A[i].
And there are ((i + 1) * (n - i) + 1) / 2 subarrays with odd length, that contains A[i].
A[i] will be counted ((i + 1) * (n - i) + 1) / 2 times.
"""
        res, n = 0, len(arr)
        for i, a in enumerate(arr):
            res += ((i + 1) * (n - i) + 1) // 2 * a
        return res

    def sumOddLengthSubarrays3(self, A):  # same as 2
        return sum(((i + 1) * (len(A) - i) + 1) // 2 * a for i, a in enumerate(A))
