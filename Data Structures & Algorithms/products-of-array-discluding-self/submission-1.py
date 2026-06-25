class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # naive: zero division error
        # without dictionary way
        # multiply all element M
        # for each index, the result = M / that element

        # get multiplication of all elements
        # res = nums[0]
        # for i in range(1, len(nums), 1):
        #     new_product = res * nums[i]
        #     res = new_product

        # # construct the final array
        # final_res = []
        # for i in range(len(nums)):
        #     final_res.append(res // nums[i])

        # return final_res

        # prefix postfx product

        # n = len(nums)
        # res = [1]*n

        # # prefix
        # prefix = 1
        # for i in range(n):
        #     res[i] = prefix
        #     prefix *= nums[i]

        # # suffix
        # suffix = 1
        # for i in range(n-1, -1, -1):
        #     res[i] *= suffix
        #     suffix *= nums[i]

        # return res
        
        # better way
        n = len(nums)
        res = [0] * n
        pref = [0] * n
        suff = [0] * n

        pref[0] = suff[n - 1] = 1
        for i in range(1, n):
            pref[i] = nums[i - 1] * pref[i - 1]
        for i in range(n - 2, -1, -1):
            suff[i] = nums[i + 1] * suff[i + 1]
        for i in range(n):
            res[i] = pref[i] * suff[i]
        return res
