class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # init l and r
        l, r = 0, len(nums) - 1

        # identify which half mid is at
        while l <= r:

            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid

            # we at the left half
            if nums[mid] >= nums[l]:
                # check if the target within?
                if nums[l] <= target <= nums[mid]:
                    # adjust the right 
                    r = mid - 1

                else:
                    # adust left
                    l = mid + 1

            else:
                if nums[mid] <= target <= nums[r]:
                    # adjust the left
                    l = mid + 1

                else:
                    # adjust right
                    r = mid - 1
        
        # if target not inside nums
        return -1
