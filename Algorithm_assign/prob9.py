#파일 경로 입력
file_input = "Algorithm_assign\dict_simplified.txt"

#단어 저장할 리스트
word = []
#설명을 저장할 리스트
expl = []
#샘플파일 불러오기 open("입력한 파일 경로","r")
with open(file_input,"r") as file:
    for line in file:
        data = line.split('\t')
        word.append(data[0])
        expl.append(data[1])

def make_graph (word,expl):

  make_list = [[]for _ in range(len(word))]
  graph = dict(zip(word,make_list))
  #각 리스트의 같은 인덱스들끼리 묶어줌.
  #name = ['merona', 'gugucon'] , price = [500, 1000]이면
  #dict(zip(name,price)) = {'merona': 500, 'gugucon': 1000}

  for i in range(len(word)):
    for j in range(len(expl)):
      expl_sp = expl[j].split() #설명들 단어 나눔
      if word[i] in expl_sp: #단어가 설명들 단어 안에 있다면
        make_list[i].append(word[j])
        make_list[j].append(word[i]) #각각 추가
  
  return graph

graph = make_graph(word,expl)

#그래프 정점의 개수와 에지 개수 출력
#정점의 개수
print(len(graph))
#에지의 개수
def edge_count(graph):
    count = 0
    
    for i in graph:
        count += len(graph[i])
    
    return count//2

print(edge_count(graph))

#차수가 최대인 정점을 찾아, 그 정점에 해당하는 단어와 차수 출력
def max_degree(graph):
  max_word = None
  max = 0

  for i in graph:
    if len(graph[i]) > max :
      max = len(graph[i])
      max_word = i

  return max_word, max

print(max_degree(graph))

#가장 큰 연결요소를 찾아 그 연결요소의 크기 (정점의 개수)출력
def large_comp(graph):
    visited = set()  # 방문한 정점 저장. 중복 방지위해 set
    max_size = 0 

    for v in graph:
        if v not in visited:
            comp_size = dfs(graph, v, visited)
            max_size = max(max_size, comp_size)

    return max_size

def dfs(graph, start, visited):
    stack = [start]  # DFS에 사용할 스택
    comp_size = 0  # 연결 요소의 크기

    while stack:
        v = stack.pop()
        if v not in visited:
            visited.add(v) #집합에 추가할 경우에는 add
            comp_size += 1

            #스택 인접 정점 추가
            for nebor in graph[v]:
                stack.append(nebor) #추가했고 이를 계속 반복

    return comp_size

print(large_comp(graph))

#하나의 단어 x와 탐색 깊이 나타내는 정수 k 입력 받고,
#단어 x로부터 떨어진 거리가 k이하인 모든 단어 출력

x = input('단어를 입력하세요 : ')
k = int(input('탐색 깊이를 입력하세요 : '))

def prt_word(graph, x, y):
    visited = set()  # 방문한 정점을 저장하는 집합
    queue = [(x, 0)]  # BFS에 사용할 큐
    count = 0  # 출력된 단어의 개수

    while queue:
        word, distance = queue.pop(0)
        if word not in visited and distance <= k:
            visited.add(word)
            if distance == 0:
                print(word)
                count += 1
            else:
                print('' * (2 * distance) + word)
                count += 1

            # 인접한 단어를 큐에 추가
            for neighbor in graph[word]:
                queue.append((neighbor, distance + 1))

    print(count)

prt_word(graph, x, k)
