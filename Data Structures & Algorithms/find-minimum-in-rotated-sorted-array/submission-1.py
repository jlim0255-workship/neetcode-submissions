class Solution:
    def findMin(self, nums: List[int]) -> int:
        # init 2 pointers, l, r
        l, r = 0, len(nums) - 1

        res = nums[0]

        # shrink the left and right poinnters toward middle
        while l <= r:
            # get the result for this interval (this l and r, possibly one of l/r is mid)
            if nums[l] < nums[r]:
                res = min(nums[l], res)
                break


            mid = l + (r - l) // 2
            res = min(res, nums[mid])

            # if the middle element is larger than the first left element, 
            # we at the left sorted portion, search right
            if nums[mid] >= nums[l]:
                l = mid + 1

            # else we at the right sorted portion, search left
            else:
                r = mid - 1

        return res

