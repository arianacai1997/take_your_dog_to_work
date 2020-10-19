class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        if len(s1) != len(s2):
            return -1

        xs, ys = lambda st: st.count('x'), lambda st: st.count('y')
        x1, x2, y1, y2 = xs(s1), xs(s2), ys(s1), ys(s2)
        if (x1 + x2) % 2 or (y1 + y2) % 2:
            return -1

        a1, a2 = '', ''
        for x, y in zip(s1, s2):
            if x != y:
                a1 += x
                a2 += y
        x1, x2, y1, y2 = xs(a1), xs(a2), ys(a1), ys(a2)
        if (x1 + x2) % 2 or (y1 + y2) % 2:  # xxx, yyy
            return -1
        cnt = 0
        # case 1 xx, yy eg. xxxy, yyxx => xyxy, xyyx first, 1 swap
        # eg. xxxyyy, yyyxxx => pair the first 2 x/y in case 1 => xyxxyy, xyyxyx
        c1 = x1 // 2
        d1 = y1 // 2
        cnt += c1 + d1
        x1, x2, y1, y2 = x1 - 2 * c1, x2 - 2 * d1, y1 - 2 * d1, y2 - 2 * c1
        # case 2 xy, yx
        cnt += x1 + y1
        return cnt

    def minimumSwap2(self, s1: str, s2: str) -> int:
        if len(s1) != len(s2):
            return -1

        x, y = 0, 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if s1[i] == 'x':
                    x += 1
                else:
                    y += 1
        # y is the num of 'x' in s2
        if (x + y) % 2:
            return -1
        return x // 2 + y // 2 + 2 * (x % 2)





