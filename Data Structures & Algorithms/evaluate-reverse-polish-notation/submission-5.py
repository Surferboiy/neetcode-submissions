class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        var=[]
        for i in tokens:
            if i not in ["+",'-','*','/']:
                var.append(int(i))
            elif i=='+':
                a=var.pop()
                b=var.pop()
                var.append(a+b)
            elif i=='-':
                a=var.pop()
                b=var.pop()
                var.append(b-a)
            elif i=='*':
                a=var.pop()
                b=var.pop()
                var.append(a*b)
            else:
                a=var.pop()
                b=var.pop()
                var.append(int(b/a))
        return var[0]