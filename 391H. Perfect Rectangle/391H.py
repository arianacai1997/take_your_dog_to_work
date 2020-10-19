class Solution:
    def isRectangleCover(self, rectangles) -> bool:
        area = 0
        corners = set()
        a, c = lambda: (X - x) * (Y - y), lambda: {(x, y), (x, Y), (X, y), (X, Y)}
        for x, y, X, Y in rectangles:
            area += a()
            corners ^= c()
        x, y, X, Y = (f(k) for f, k in zip((min, min, max, max), zip(*rectangles)))
        # *rectangles => unpack the rectangles into n lists
        # zip(*rectangles) => pair the items with the same index in each iterator
        # so here, x/y coordinates of the same coners are paired together
        # zip((), zip()) => pair the min/max function with the paired items
        return area == a() and corners == c()

    """Here can be another idea of sweeping:
    If the area does not match, return false.
    The outside corners should only appear once. And the inside corners could appear either twice or four times.
    So it is an even number. If # of corners except for outside corners is odd, return false.
"""
