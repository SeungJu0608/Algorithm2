### with Greedy Algorithm ###

# 데이터 입력
n = int(input())
count = 0  # 최소 봉지 개수

# 케이스 나누기
# 1) 5로 나누어 떨어지면 5로 나눈 몫 출력
while n >= 0:
    if n % 5 == 0:
        count += (n//5)
        print(count)
        break
    # 2) 5로 나누어 떨어지지 않을 떄
    else:
        n -= 3
        count +=1
else :
    print(-1)



## 다이나믹 프로그래밍 이용하기
# 데이터 입력
n = int(input())
v = [5, 3]

# 최소 봉지개수를 저장하기 위한 dp_table 초기화
dp = [5001] * 5001
for i in v:
    dp[i] = 1

# 다이나믹 프로그래밍
for i in range(6, n + 1):
    if dp[i - 5] == 0 and dp[i - 3] != 0:
        dp[i] = dp[i - 3] + 1
    if dp[i - 5] != 0 and dp[i - 3] == 0:
        dp[i] = dp[i - 5] + 1
    if dp[i - 5] != 0 and dp[i - 3] != 0:
        dp[i] = min(dp[i - 5], dp[i - 3]) + 1
    else:
        continue
# 결과 프린트
if dp[n] == 5001:
    print(-1)
else:
    print(dp[n])
