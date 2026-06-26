class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort the nums
        sorted_nums = sorted(nums)
        res = []

        # loop through the sorted list
        for i in range(len(sorted_nums)):

            
            if i >= 1 and sorted_nums[i] == sorted_nums[i-1] :
                continue

            # init 2 pointers
            j, k = i+1, len(nums)-1

            # MEAT
            # num[i] + num[j] + num[k] = 0
            # -num[i] = num[j] + num[k]

            # keep shrinking towards the middle            
            while j < k:
                if sorted_nums[j] + sorted_nums[k] == -sorted_nums[i]:
                    res.append([sorted_nums[i], sorted_nums[j], sorted_nums[k]])

                    j+=1
                    k-=1

                    # skip duplicates for j
                    while j < k and sorted_nums[j] == sorted_nums[j-1]:
                        j += 1

                    # skip duplicates for k
                    while j < k and sorted_nums[k] == sorted_nums[k+1]:
                        k -= 1

                # too big, decrease k
                elif sorted_nums[j] + sorted_nums[k] > -sorted_nums[i]:
                    k -= 1

                # too small, increase j
                elif sorted_nums[j] + sorted_nums[k] < -sorted_nums[i]:
                    j += 1
                
        return res    

        # target = -num[i]
        # j k pointers to find j and k

        # only append into list when num[j] + num[k] == -num[i]
        # then find next pair