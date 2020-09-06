# # def cl(n):
# #     card = []
# #     for i in range(1,n+1):
# #         card.append([i,i])
# #     if not n%2:
# #         for t in range(1, n // 2 + 1):
# #             card[n-t][0] = 2 * t - 1
# #             card[t-1][0] = 2 * t
# #     else:
# #         card[0][0] = 1
# #         for i in range(1, n // 2 + 1):
# #             card[n-i][0] = 2 * i
# #             card[i][0] = 2 * i +1
# #     ls = sorted(card, key=lambda  x: x[0], reverse=True)
# #     to_return = [car[1] for car in ls]
# #     return to_return
# #
# # print(cl(13))
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
import sys
if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    total = []
    for i in range(n):
        line = sys.stdin.readline().strip()
        values = list(map(int, line.split()))
        total.append(values)

    def helper(ls=[]):
        if len(ls) <= 1:
            pass
        else:
            ls.insert(0, ls.pop())
        return ls


    for cards in total:
        res = []
        for i in range(len(cards), 0, -1):
            helper(res)
            res.insert(0, cards[i-1])
        res = list(map(str, res))
        print(' '.join(res))

import sys
import bisect
#
# if __name__ == "__main__":
#     n = int(sys.stdin.readline().strip())
#     total = []
#     for i in range(n):
#         line = sys.stdin.readline().strip()
#         values = list(map(int, line.split()))
#         total.append(values)
#
#     def helper(ls, K):
#         l, r, n = 0, 1, len(ls)
#         while True:
#             m = (l+r)/2
#             border = [bisect.bisect(ls, ls[i]/m) for i in range(n)]
#             curr = sum(n-i for i in border)
#             if curr > K:
#                 r = m
#             elif curr < K:
#                 l = m
#             else:
#                 return max([(ls[i], ls[j]) for i, j in enumerate(border) if j < n], key=lambda x: x[0] /x[1])
#
#
#     for lis in total:
#         K = lis[0]
#         ls = lis[1:]
#         print(K, ls)
#         m, n = helper(ls, K)
#         res = list(map(str, [m, n]))
#         print(' '.join(res))
#

# import sys
#
# if __name__ == "__main__":
#     n = int(sys.stdin.readline().strip())
#     total = []
#     for i in range(n):
#         line = sys.stdin.readline().strip()
#         values = list(map(int, line.split()))
#         total.append(values)
#
#
#     def helper(ls, K):
#         l, r, n = 0, 1, len(ls)
#         while True:
#             m = (l + r) / 2
#             border = [bisect.bisect(ls, ls[i] / m) for i in range(n)]
#             curr = sum(n - i for i in border)
#             if curr > K:
#                 r = m
#             elif curr < K:
#                 l = m
#             else:
#                 return max([(ls[i], ls[j]) for i, j in enumerate(border) if j < n], key=lambda x: x[0] / x[1])
#
#
#     for lis in total:
#         K = lis[0]
#         ls = lis[1:]
#         m, n = helper(ls, K)
#
#         print(m, n)





