class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dct = dict()
    
        for i in range(len(nums)):
            
            key = nums[i]

            # if key in dct:
            if dct.get(key):
                return True
                
            else:
                dct[key] = 1
    
        return False