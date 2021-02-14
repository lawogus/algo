import sys

n,m = map( int, sys.stdin.readline().split())

dp = [10001] * (m+1) 
arr = []

for _ in range(n):
    arr.append(int(sys.stdin.readline()) )


dp[0] = 0
for i in range(n):
    for j in range(arr[i],m+1):
        if dp[j- arr[i]] != 10001:
            dp[j] = min( dp[j], dp[j-arr[i]] + 1)

if dp[m] == 10001:
    print(-1)
else:
    print(dp[m])