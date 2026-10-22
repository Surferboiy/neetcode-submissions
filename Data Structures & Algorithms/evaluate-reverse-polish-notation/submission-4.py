class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        var_list=[]
        for i in tokens:
            if i not in ["+",'-','*','/']:
                var_list.append(i)
            elif i=='+':
                a=int(var_list.pop())
                b=int(var_list.pop())
                var_list.append(a+b)
            elif i=='*':
                a=int(var_list.pop())
                b=int(var_list.pop())
                var_list.append(a*b)
            elif i=='-':
                a=int(var_list.pop())
                b=int(var_list.pop())
                var_list.append(b-a)
            else:
                a=int(var_list.pop())
                b=int(var_list.pop())
                var_list.append(b/a)
        return int(var_list[0])

        