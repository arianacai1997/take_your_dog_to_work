class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        even = 0
        while not n % 2:
            even += 2
            n /= 2

        # eg. 63=7*9, 7 steps to get 7, copy + paste * 8=> 9 steps to get 63
        # odd x = a * b, we need a+b steps
        element = []
        if n == 1:
            return even

        def factor(n):
            for i in range(2, n):
                while n // i == n / i:
                    element.append(i)
                    n //= i

        factor(int(n))
        odd = sum(element) if element else n
        return int(even + odd)

    def minSteps(self, n):
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return self.minSteps(n / i) + i
        return 0 if n == 1 else n