s = 'cbbd'
dp = [[0 for _ in range(len(s))] for _ in range(len(s))]

result = ''
max_len = 1
for j in range(len(s)):
	for i in range(0,j + 1):
		if i == j:
			dp[j][j] = 1
		elif i == j - 1:
			if s[i] == s[j]:
				dp[i][j] = 1
				if j - i + 1 > max_len:
					result = s[i:j+1]
			else:
				dp[i][j] = 0
		else:
			if dp[i+1][j-1] == 1 and s[i] == s[j]:
				dp[i][j] = 1
				if j - i + 1 > max_len:
					result = s[i:j+1] 
			else:
				dp[i][j] = 0
print(dp)
print(result)