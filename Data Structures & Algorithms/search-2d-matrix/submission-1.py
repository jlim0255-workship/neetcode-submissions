class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # init 2 pointers l and r
        l, r = 0, len(matrix[0]) - 1

        num_of_rows = len(matrix[0])
        row_to_search = 0
        

        # the last element of the previous row is smaller than the first item of next row
        
        # first to check which row should we search
        for i in range(len(matrix)):
            if matrix[i][0] <= target <= matrix[i][-1]:
                row_to_search = i
            

        while l <= r:
            mid = l + ((r - l) // 2)

            if matrix[row_to_search][mid] == target:
                return True
            
            elif matrix[row_to_search][mid] > target:
                r = mid - 1

            else:
                l = mid + 1
    
        return False