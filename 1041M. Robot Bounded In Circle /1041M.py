class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # treat L, R as rotation for 90 degrees and the direction is a base vection
        x, y, dx, dy =0, 0, 0, 1
        for i in instructions:
            if i == 'L':
                dx, dy = -dy, dx
            if i == 'R':
                dx, dy = dy, -dx
            if i == 'G':
                x += dx
                y += dy
        return (x, y) == (0, 0) or (dx, dy) != (0, 1)