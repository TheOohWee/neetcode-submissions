class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        stack = [] 
        result = [0] * len(temps)

        for i in range(len(temps)):
            while stack and temps[stack[-1]] < temps[i]:
                popped = stack.pop()
                result[popped] = i - popped

            stack.append(i)

        return result
            