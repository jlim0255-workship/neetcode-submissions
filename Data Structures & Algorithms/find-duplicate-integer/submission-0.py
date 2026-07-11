class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # naive dict approach
        valueToCount = {}
        for i in range(len(nums)):
            valueToCount[nums[i]] = 1 + valueToCount.get(nums[i], 0)
            if valueToCount[nums[i]] > 1:
                return nums[i]

        

            