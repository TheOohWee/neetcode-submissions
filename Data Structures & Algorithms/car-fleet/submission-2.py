class Solution:
    def carFleet(self, target: int, pos: List[int], s: List[int]) -> int:
        stack = []
        eta = []

        cars = [] 
        for i in range(len(pos)):
            cars.append([pos[i], s[i]])
        cars = sorted(cars, reverse = True)

        for j in cars:
            a = (target - j[0]) / j[1]
            eta.append(a)

        for i in range(len(eta)):
            if stack and stack[-1] >= eta[i]:
                pass
            else:            
                stack.append(eta[i])

        return len(stack)
