class Solution:
    def trap(self, height: List[int]) -> int:
        # init 2 pointers
        l, r = 0, len(height)-1
        leftmax, rightmax = height[l], height[r]

        i = 0
        res = 0

        # shrinking the 2 pointers toward middle
        while l < r:
            # the water that can be trapped at ith position
            # formula = min(leftmax, rightmax) - h[i]

            if height[l] >= height[r]:
                rightmax = max(rightmax, height[r])
                trapped_water_at_i = rightmax - height[r]
                # keep larger left
                
                r -= 1


            # if height[l] < height[r]:
            else:
                # keep larger right
                leftmax = max(leftmax, height[l])
                trapped_water_at_i = leftmax - height[l]
                l += 1
                
            if (trapped_water_at_i) > 0:
                res += trapped_water_at_i
                
            

            # loop through the height, and accumulate those ith position with non negative value
        
        return res