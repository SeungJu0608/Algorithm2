### ATM  ###

## using Greedy Algorithm
# 1대뿐인 ATM 앞에 N명의 사람이 줄을 서 있고 각각 번호가 부여되있다.
# i번 사람이 돈을 인출하는데 걸리는 시간은 P_i분 이다.
# 사람들이 줄을 서는 순서에 따라 돈을 인출하는데 필요한 시간의 합은 달라진다.
# N과 [P_1 : P_N]의 정보가 주어졌을 때 각 사람이 돈을 인출하는데 필요한 시간의 합의 최솟값을 구하여라

# 시간이 가장 짧게 걸리는 사람부터 차례로 업무를 본다면 필요한 시간의 합을 최소로 만들 수 있다.
# 따라서 각 개인의 돈을 인출하는데 걸리는 시간에 따라 정렬한다.
# 데이터 입력
n = int(input())
p = list(map(int,input().split()))

# 정렬 후 그리디 알고리즘을 이용하여 최솟값 찾기
p.sort()
count = 0
time = []

for i in range(n):
    count += p[i]
    time.append(count)

print(sum(time))

