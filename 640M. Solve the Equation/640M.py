class Solution:
    def solveEquation(self, equation: str) -> str:
        eq = equation.split('=')

        def cnt(s):
            sign, n = 1, len(s)
            # i, coef, const stand for current index, and accumulative 'x' coefficient and constant
            i = coef = const = 0
            while i < n:
                if s[i] == '+':
                    sign = 1
                elif s[i] == '-':
                    sign = -1
                elif s[i].isdigit():
                    j = i
                    while j < n and s[j].isdigit():
                        j += 1
                    tmp = int(s[i:j])
                    if j < n and s[j] == 'x':
                        coef += tmp * sign
                        j += 1
                    else:
                        const += tmp * sign
                    i = j - 1
                else:
                    coef += 1 * sign
                i += 1
            return const, coef

        n1, x1 = cnt(eq[0])
        n2, x2 = cnt(eq[1])
        x3 = x1 - x2
        n3 = n2 - n1
        if x3 == 0 and n3 == 0:
            return "Infinite solutions"
        try:
            return "x=" + str(n3 // x3)
        except:
            return "No solution"
