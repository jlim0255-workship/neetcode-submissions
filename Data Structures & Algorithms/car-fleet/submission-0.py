class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # target = 10, position = [1,4], speed = [3,2]
        # output = 1

        pair = [[p, s] for p, s in zip(position, speed)]

        stack = []

        # reverse sorted order
        for p, s in sorted(pair)[::-1]:
            stack.append((target - p) / s)

            # does if overlap with others?
            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)


        # just find the time for the top car in stack
        # formula = (target - position) / time

        