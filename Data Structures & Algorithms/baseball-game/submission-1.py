class Solution:
    def calPoints(self, operations: List[str]) -> int:
        sizeofop=len(operations)
        record=[]
        for i in range(sizeofop):
            if(operations[i]=="+"):
                record.append(int(record[-1])+int(record[-2]))
            elif(operations[i]=="C"):
                record.pop()
            elif(operations[i]=="D"):
                record.append(record[-1]*2)
            else:
                record.append(int(operations[i]))
        return sum(record)



                  