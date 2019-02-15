class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        if len(s) <= numRows:
            return s
        
        rows = []
        for i in range(numRows):
            rows.append([])
            
        curRow = 0
        goingDown = False
        
        for i in s:
            rows[curRow].append(i)
            if curRow == 0 or curRow == numRows - 1:
                goingDown = not goingDown
            if goingDown == True:
                curRow += 1
            else:
                curRow -= 1
        result = []
        for row in rows:
            for i in row:
                result.append(i)
        
        return "".join(result)
        
        
        
        