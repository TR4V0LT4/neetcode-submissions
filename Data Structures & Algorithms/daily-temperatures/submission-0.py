class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = []
        start = 0
        for day in temperatures:
            counter = 1
            stack.append(day)

            for i in range(start+1 ,len(temperatures)):
                if stack[-1] < temperatures[i]:
                    stack.pop()
                    result.append(counter)
                    break
                else :
                    counter += 1
            else:
                result.append(0)       
            start += 1
        return result