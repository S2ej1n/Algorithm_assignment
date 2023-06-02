#입력 (N과 가격 나타내는 N개의 양의 정수 주어짐.)
N = int(input("양의 정수 N을 입력하세요 : "))
cst_str = input("N개의 양의 정수 입력하세요 : ")

#가격을 리스트로 변경
cst = cst_str.split()
cost = [int(n) for n in cst]

#N을 분해하는 함수
def Division(n):
    Stack = [n]
    divisin_list = [] #분할된 값들 저장
    while True:
        divisin_list.append(Stack.copy()) #우선 그냥 Stack 추가
        temp = Stack.pop() #우선 스택에서 수를 하나 꺼내서 temp라고 한다.

        if temp != 1: #꺼낸 temp가 1이 아니라면
            Stack.append(temp - 1) #여기서 1을 빼서 스택에 넣고
            Stack.append(1) #1도 스택에 넣는다.
        else: #하지만 temp가 1이라면 (마지막 분할 요소가 1이 아니라면)
            '''
            스택에서 1이 아닌 수가 나올 때 까지 계속 꺼내고, 
            꺼내는 수들의 합 +1을 sum에 저장하는 알고리즘입니다~

            그러다가 1이 아닌 수가 나올때(=b) b-1과 지금까지의 sum을 다시 스택에 넣는다
            '''
            sum = 2 #이미 1인거 꺼낸거에 +1
            for _ in range(len(Stack)): #stack의 길이만큼 반복.
                if Stack and Stack[-1] == 1: #stack 비어있지 않고, 마지막 요소 1이라면
                    sum += 1
                    Stack.pop() #stack에서 해당 요소 제거
            if not Stack:
                break

            not_One_num = Stack.pop() - 1 #1을 뺀다. (이미 1을 꺼낸것에 1을 더했기 때문)
            Stack.append(not_One_num) #스택에 추가해준다.

            while sum > not_One_num: #sum이 마지막 남은 수보다 큰 경우
                Stack.append(not_One_num)
                sum -= not_One_num
            Stack.append(sum)

    return  divisin_list

division = Division(N)

def MaxCost(N, cost, Division):
    #우선 N의 가격을 max로 지정
    max_cost = cost[N-1]
    sum_cost = 0 #가격의 최대합

    for i in Division:
        for j in i:
            sum_cost += cost[j-1]
        if sum_cost > max_cost:
            max_cost = sum_cost
        sum_cost = 0
    print(max_cost)

MaxCost(N,cost,division)