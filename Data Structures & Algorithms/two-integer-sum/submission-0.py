class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dct = dict()

        for i in range(len(nums)):
            # key = this value
            # value = index of this value

            key = nums[i]
            value = i
            
            difference = target - key

            # if dct.get(difference):
            if difference in dct:
                # dct.get(difference) always smaller
                return [dct.get(difference), value]
            else:
                dct[key] = value