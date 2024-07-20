
from itertools import permutations, combinations
data = ["a","b","c"]
result = list(permutations(data,2))
print("answer : ",result)


data = ["a","b","c"]
target_level = 1 
target_list = [0 for i in range(target_level+1)]
visited = [False for i in range(len(data))]

def dfs(node,visited,level):
    

    val = data[node]
    target_list[level] = val
    visited[node] = True

    if level == target_level:
        print(target_list)
        return
    

    for i in range(len(data)):
        if visited[i] != True: 
            dfs(i,visited,level+1)
            target_list[level+1] = 0
            visited[i] = False

#---- exec
for q in range(len(data)):
    dfs(q,visited,0)
    #-- init 
    visited = [False for i in range(len(data))]


#---- update 
#https://ckd2806.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC-python-%EC%88%9C%EC%97%B4-%EC%A1%B0%ED%95%A9-%EC%BD%94%EB%93%9C%EB%A1%9C-%EA%B5%AC%ED%98%84%ED%95%98%EA%B8%B0
#for 문을 들어가면서 value 카운트를 해서, 밖에서 for문으로 첫번째 루프를 시작할 필요가 없어졌음. 
#나머지 부분은 좋음
    
#-----
l = ['a', 'b', 'c']
visited = [0 for _ in range(len(l))]
answer = []

def dfs(cnt, list):
    if cnt == len(l):
        answer.append(list[:])
        return

    for i, val in enumerate(l):
        # 만약 방문했다면 건너 뛰기(순열을 위함)
        if visited[i] == 1:
            continue
        # 현재까지의 list에 값을 추가하고, 방문 표시하기
        list.append(val)
        visited[i] = 1

        dfs(cnt+1, list)
        # 방금 전 list에 추가한 값과 방문 한 것을 되돌려주기
        list.pop()
        visited[i] = 0


dfs(0, [])
print(answer)
    
