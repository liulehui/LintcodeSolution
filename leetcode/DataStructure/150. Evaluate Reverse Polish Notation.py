# coding:utf-8
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        operators = set(['+','-','*','/'])
        stack = []
        for i in range(len(tokens)):
            if tokens[i] not in operators:
                stack.append(int(tokens[i]))
            else:
                ele1 = int(stack.pop())
                ele2 = int(stack.pop())
                if tokens[i] == '+':
                    stack.append(ele1+ele2)
                elif tokens[i] == '-':
                    stack.append(ele2-ele1)
                elif tokens[i] == '*':
                    stack.append(ele1*ele2)
                elif tokens[i] == '/':
                    if ele2 * ele1 < 0 and ele2 % ele1 != 0: 
                        stack.append(ele2//ele1+1)
                    else:
                        stack.append(ele2//ele1)

        return stack.pop()
        
