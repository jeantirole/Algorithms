트리의 부모 찾기 
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	256 MB	87533	39205	27549	42.510%
문제
루트 없는 트리가 주어진다. 이때, 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 노드의 개수 N (2 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N-1개의 줄에 트리 상에서 연결된 두 정점이 주어진다.

출력
첫째 줄부터 N-1개의 줄에 각 노드의 부모 노드 번호를 2번 노드부터 순서대로 출력한다.

예제 입력 1 
7
1 6
6 3
3 5
4 1
2 4
4 7
예제 출력 1 
4
6
1
3
1
4




#----------------------------
# sol
import sys
sys.setrecursionlimit(10**6)

num_nodes = int(sys.stdin.readline())

adjacency_list = [[] for _ in range(num_nodes + 1)]
for _ in range(num_nodes - 1):
    node1, node2 = map(int, sys.stdin.readline().split())
    adjacency_list[node1].append(node2)
    adjacency_list[node2].append(node1)

parent_nodes = [0] * (num_nodes + 1)


def depth_first_search(current_node):
    for adjacent_node in adjacency_list[current_node]:
        if parent_nodes[adjacent_node] == 0: # 방문한 적이 없다면
            parent_nodes[adjacent_node] = current_node # 현재 노드를 부모 노드로 저장
            depth_first_search(adjacent_node)


depth_first_search(1)

for node in range(2, num_nodes + 1):
    print(parent_nodes[node])
