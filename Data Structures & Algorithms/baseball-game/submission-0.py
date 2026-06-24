class Solution:
    def calPoints(self, operations: List[str]) -> int:
        records = []    

        def fst(a):
            records.append(a)

        def snd(a, b):
            c = a + b
            records.append(c)

        def trd(a):
            c = 2*a
            records.append(c)
        
        def frth():
            records.pop()
            
        for i in range(len(operations)):
            if operations[i] == "+":
                snd(records[-1], records[-2])
            elif operations[i] == "D":
                trd(records[-1])
            elif operations[i] == "C":
                frth()
            else:
                fst(int(operations[i]))

        return sum(records)