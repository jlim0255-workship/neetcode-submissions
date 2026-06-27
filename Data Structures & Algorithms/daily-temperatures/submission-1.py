class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # temperatures =[30,38,30,36,35,40,28]
        
        # stack = []
        # res = []
        # counter = 0

        # put the values into stack as we loop the list
        # for i in range(0, len(temperatures)):
        #     stack.append(temperatures[i])
    
        #     if len(stack) > 0:
        #         if temperatures[i+1] <= stack[0]:
        #             stack.append(temperatures[i])

        #         elif temperatures[i] > stack[0]:
        #             counter = len(stack)
        #             res.append(counter)
        #             stack = []
        #     elif len(stack) == 0:
        #         stack.append(temperatures[i])

        # init result list with 0
        res = [0] * len(temperatures)
        stack = []

        # loop through the list
        for idx, temp in enumerate(temperatures):

            # if the temp i is greater than the one at top stack
            # meaning the decreasing trend ended, pop out and count the interval
            # LIFO: we will fill up the res list with the one near temp, then go left
            while stack and temp > stack[-1][0]:
                top_temp, top_idx = stack.pop()
                res[top_idx] = idx - top_idx

            stack.append((temp, idx))

        return res