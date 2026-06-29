class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # init left right pointers
        l, r = 0, len(nums)-1
        

        # shrinking l and r toward middle
        while l <= r:
            mid = l + ((r - l) // 2)

            # mid = target, return
            if nums[mid] == target:
                return mid

            # if mid > target
            elif nums[mid] > target:
               # shrink r
               r = mid - 1

            # if mid < target
            # elif nums[mid] < target:
            else:
                l = mid + 1

        return -1
