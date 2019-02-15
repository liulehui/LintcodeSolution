class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        MAX_INT = 2**31 - 1
        MIN_INT = -MAX_INT - 1
        pre = ''
        result = ''
        preSymbol = True
        space = True
        
        for i in str:
            if i == " " and space == True:
                continue
            elif (i == '+' or i =='-') and preSymbol==True:
                pre = i
                preSymbol = False
                space = False
            elif i.isdigit():
                result += i
                preSymbol = False
                space = False
            else:
                break
                
        if result.isdigit():
            if int(pre+result) > MAX_INT:
                return MAX_INT
            elif int(pre+result) < MIN_INT:
                return MIN_INT
            else:
                return int(pre+result)
                
        else:
            return 0