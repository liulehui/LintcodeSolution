class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # using stack
        stack = []
        if s is None or len(s) == 0:
            return True
        if len(s) == 1:
            return False
        
        for i in s:
            if len(stack) == 0:
                stack.append(i)
                continue
            top = stack[-1]
            if top == '(' and i == ')':
                stack.pop()
            elif top == '[' and i == ']':
                stack.pop()
            elif top == '{' and i == '}':
                stack.pop()
            else:
                stack.append(i)
        if len(stack) == 0:
            return True
        return False