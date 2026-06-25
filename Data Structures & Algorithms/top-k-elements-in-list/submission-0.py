class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        # create a heap
        heap = []
        for num in count.keys():
            # every node is a tuple of (frequency, key)
            heapq.heappush(heap, (count[num], num))

            # check if the len over k
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
