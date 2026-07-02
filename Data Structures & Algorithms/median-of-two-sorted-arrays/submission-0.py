class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # naive
        # find median
        # after combine 2 arrays:
        # if odd, (n/2) + ((n/2) - 1) / 2
        # if median, (n + 1) / 2

        # arrayA is always smaller
        if len(nums1) < len(nums2):
            A = nums1
            B = nums2
        else:
            A = nums2
            B = nums1
        
        total = len(nums1) + len(nums2)

        half = total // 2

        l, r = 0, len(A) - 1
        while True:
            i = l + (r - l) // 2 # A mid
            j = half - i - 1 - 1 # B mid

            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            
            # left partition is correct
            if Aleft <= Bright and Bleft <= Aright:
                # odd
                if total % 2:
                    return min(Aright, Bright)

                # even
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            
            # else A is too big reduce it
            elif Aleft > Bright:
                r = i - 1

            else:
                l = i + 1