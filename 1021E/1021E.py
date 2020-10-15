class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        if not S:
            return ''
        stack = []
        flag = 0
        start = 0
        res = ''
        for i in range(len(S)):
            if S[i] == '(':
                if flag == 0:  # this is in an outer parenthess
                    start = i
                stack.append('(')
                flag += 1
            else:
                flag -= 1
                if flag == 0:  # this closes an outer parenthess
                    res += S[start + 1: i]
        return res

    def removeOuterParentheses2(self, S):
        res, opened = [], 0
        for c in S:
            if c == '(' and opened > 0: res.append(c)
            if c == ')' and opened > 1: res.append(c)
            opened += 1 if c == '(' else -1
        return "".join(res)


