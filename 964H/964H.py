from functools import lru_cache


class Solution:
    def leastOpsExpressTarget(self, x: int, target: int) -> int:
        cache = dict()

        def helper(target, idx):
            if idx == 0 or target == 1:
                return target * 2 - 1  # combination of / and +, minus the leading 1
            if (idx, target) in cache:
                return cache[(idx, target)]
            power = x ** idx
            count = target // power
            if target % power == 0:
                return idx * count - 1
            low = idx * count + \
                  helper(target - power * count, idx - 1)
            high = idx * (count + 1) + \
                   helper(power * (count + 1) - target, idx - 1)
            cache[(idx, target)] = min(low, high)
            return cache[(idx, target)]

        ret = helper(target, math.ceil(math.log(target, x)))
        return ret