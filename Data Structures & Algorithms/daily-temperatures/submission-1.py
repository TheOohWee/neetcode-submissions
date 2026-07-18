class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        stack = [] 
        result = [0] * len(temps)

        for i in range(len(temps)):
            while stack and stack[-1][1] < temps[i]:
                popped = stack.pop()
                result[popped[0]] = i - popped[0]

            stack.append((i, temps[i]))

        return result
            