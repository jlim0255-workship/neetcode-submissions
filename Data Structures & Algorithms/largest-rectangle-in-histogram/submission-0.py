class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # heights = [7,1,7,2,2,4]
        # output = 8

        # init stack
        # only go left to right if increasing order or even height
        # if start decreasing, then pop, calculate area, compare with max, then see if can go right again
        maxArea = 0
        stack = [] # pair: (index, height)

        for i, h in enumerate(heights):
            start = i
            
            # extend
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))

                # extend start index backwards
                start = index

            stack.append((start, h))

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))

        return maxArea