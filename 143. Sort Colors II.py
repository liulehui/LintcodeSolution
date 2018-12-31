# coding:utf-8
# counting sort O(k) extra space
def sortColors2(colors, k):
        # write your code here
        
        colorset = {}
        for i in colors:
            if i not in colorset:
                colorset[i] = 1 
            else:
                colorset[i] += 1 
        k = 0
        for key in sorted(colorset):
            for i in range(colorset[key]):
                colors[k] = key
                k += 1
        return

