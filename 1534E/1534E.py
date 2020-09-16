from itertools import combinations
# combinations('ABCD', 2) --> AB AC AD BC BD CD
# combinations(range(4), 3) --> 012 013 023 123
class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        combs = combinations(arr, 3)
        ans = 0
        for i in combs:
            if abs(i[0] - i[1]) <= a and abs(i[1] - i[2]) <= b and abs(i[0] - i[2]) <= c:
                ans += 1

        return ans