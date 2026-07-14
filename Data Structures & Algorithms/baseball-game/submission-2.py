class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []

        def add(x):
            record.append(x)
        def sum1(a, b):
            record.append(a + b)
        def dbl(a):
            record.append(2*a)
        def rmv(a):
            record.remove(a)
        
        j = 0
        for i in range(len(operations)):
            if operations[i] == '+':  
                if j > 1:                        
                    sum1(record[j - 1], record[j - 2]) 
                    j += 1                 
            elif operations[i] == 'D':
                if j > 0:  
                    dbl(record[j-1])
                    j += 1
            elif operations[i] == 'C':
                if j > 0:
                    rmv(record[j-1])
                    j -= 1
            else:
                add(int(operations[i]))
                j += 1

        return sum(record)
