class Solution:
    def minOperations(self, n: int) -> int:
        return n**2//4
    """if odd length:
need 2, 4 .. , 2 * ( n / 2) ops, that is n / 2 * (2 + 2 * (n / 2)) / 2 = n / 2 * (n / 2 + 1) ;

if even length:
need 1, 3 .. , 2 * ( n / 2) - 1 ops, that is n / 2 * (1 + 2 * (n / 2) - 1) / 2 = n / 2 * (n / 2) ;"""