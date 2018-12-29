# coding:utf-8
def fastPower(a, b, n):
        # write your code here
        ans = 1
        base = a
        while n!=0:
            if n % 2 == 1:
                ans = (ans * base) % b
            base = (base * base) % b # may overflow
            n = n // 2
        
        return ans%b