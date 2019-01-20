# coding:utf-8
import sys
class Solution:
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        minutes = []
        for timePoint in timePoints:
            minute = int(timePoint.split(':')[0]) * 60 + int(timePoint.split(':')[1])
            minutes.append(minute)
        
        minutes.sort()
        print(minutes)
        res = sys.maxsize
        for i in range(len(minutes)):
            if i == len(minutes) - 1:
                diff = minutes[0] + 24 * 60 - minutes[i]
                res = min(res,diff)

                break
            diff = minutes[i+1] - minutes[i]
            res = min(res,diff)
            print(res)
        print(minutes)
        print(res)
        
        return res

if __name__ == '__main__':
	solution = Solution()
	timePoints = ["23:59","00:00"]
	res = solution.findMinDifference(timePoints)
	print(res)