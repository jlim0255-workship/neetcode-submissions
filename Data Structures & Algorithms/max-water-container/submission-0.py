class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # init 2 pointers
        l, r = 0, len(heights) - 1

        max_area = 0

        # keep shrinking 2 pointers toward middle
        while l < r:
            length = min(heights[l], heights[r]) 
            width = r - l
            area = length * width
            max_area = max(max_area, area)

            if heights[l] >= heights[r]:
                # keep the larger height
                r -= 1

            if heights[l] < heights[r]:
                # keep the larger height
                l += 1

        return max_area
        # calculate area using pointers
        # area = length x width
        # length = min(pointer l, pointer r)
        # width = idx(r) - idx(l)
        # update the pointers


        # keep track current max
        # keep comparing and get the max