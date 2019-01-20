class Solution:
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        dict = {}
        for i in T:
            if i not in dict:
                dict[i] = 1 
            else:
                dict[i] += 1
        res = []
        
        for j in S:
            if j in dict:
                while dict[j] != 0:
                    res.append(j)
                    dict[j] -= 1
                    #print(j,dict[j])
        
        for key, value in dict.items():
            if value == 0:
                continue
            while dict[key] != 0:
                res.append(key)
                dict[key] -= 1
        
        return ''.join(res)
        