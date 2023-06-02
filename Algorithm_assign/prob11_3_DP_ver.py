def MaxCostDP(N, cost):
    #memoization
    dp = [0] * (N+1)
    dp[1] = cost[0]  # 첫 번째 가격을 초기값으로 설정

    #bottom-up
    for i in range(2, N+1):
        max_cost = cost[i-1]  #현재 숫자에 해당하는 가격
        for j in range(1, i):
            max_cost = max(max_cost, dp[i-j] + dp[j])  #max 가격 변경
        dp[i] = max_cost

    return dp[N]

N = int(input("양의 정수 N을 입력하세요: "))
cst_str = input("N개의 양의 정수를 입력하세요: ")

# 가격을 리스트로 변경
cst = cst_str.split()
cost = [int(n) for n in cst]

max_cost = MaxCostDP(N, cost)
print(max_cost)
