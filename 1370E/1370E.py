import collections


class Solution:
    def sortString(self, s: str) -> str:
        res = ''
        s = list(s)
        s.sort()
        while s:
            i = 0
            curr = []
            while i < len(s):
                if s[i] not in curr:
                    curr.append(s.pop(i))
                else:
                    i += 1
            res += ''.join(curr)

            j = len(s) - 1
            curr = []
            while j >= 0:
                if s[j] not in curr:
                    curr.append(s.pop(j))
                j -= 1
            res += ''.join(curr)
        return res

    def sol2(self, s):
        cnt, ans, asc = collections.Counter(s), [], True
        while cnt:                                                                  # if Counter not empty.
            for c in sorted(cnt.keys()) if asc else reversed(sorted(cnt.keys())):   # traverse keys in ascending/descending order.
                ans.append(c)                                                       # append the key.
                cnt[c] -= 1                                                         # decrease the count.
                if cnt[c] == 0:                                                     # if the count reaches to 0.
                    del cnt[c]                                                      # remove the key from the Counter.
            asc = not asc                                                           # change the direction, same as asc ^= True.
        return ''.join(ans)