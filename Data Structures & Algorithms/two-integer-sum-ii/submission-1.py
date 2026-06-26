class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # sort the numbers array
        sorted_numbers = sorted(numbers)

        # init 2 pointers
        l, r = 0, len(numbers)-1

        # keep shrinking the l and r pointers toward middle
        while l < r:

            # if num[l] + num[r] == target, return
            if sorted_numbers[l] + sorted_numbers[r] == target:
                return [l+1, r+1]

            # if num[l] + num[r] > target, too big, decrease r
            if sorted_numbers[l] + sorted_numbers[r] > target:
                r -= 1

            # if num[l] + num[r] < target, too small, increase l
            if sorted_numbers[l] + sorted_numbers[r] < target:
                l += 1

        return [l+1, r+1]