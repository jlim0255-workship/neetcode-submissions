class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # key = num, value = length
        # dct = {}
        
        # for i in range(len(nums)):
        #     if nums[i] in dct.keys():
        #         dct[nums[i]] += 1

        #     else:
        #         dct[nums[i]] = 1

        # # get the values list, and filter the max
        # res = list(dct.values())

        # return max(res)

        numSet = set(nums)
        longest = 0
        dct = {}

        for num in numSet:
            if (num - 1) not in dct:

                # this can be a start
                length = 1

                # if next num (num + length) in set, keep extending until the loop breaks
                while (num + length) in numSet:
                    length += 1

                # comnpare get the max
                longest = max(length, longest)
                
        return longest



