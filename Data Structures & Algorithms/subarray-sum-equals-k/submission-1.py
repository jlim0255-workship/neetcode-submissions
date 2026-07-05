class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # prefix = [0] * len(nums) + 1

        # prefix[0] = 0
        
        # # init prefix array
        # for i in range(1, len(nums) + 1):
        #     prefix[i] = prefix[i-1] + nums[i-1]

        # + 2 pointers

        
        # default way handling positive and negative integers
        prefix_sums = {0: 1}

        result = 0
        curr_sum = 0

        # for i in range(len(nums)):
        for num in nums:
            curr_sum += num
            complement = curr_sum - k
            # if complement in prefix_sums:
            #     result += prefix_sums[complement]
            result += prefix_sums.get(complement, 0)

            prefix_sums[curr_sum] = 1 + prefix_sums.get(curr_sum, 0)
        return result

