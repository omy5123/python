"""
문제
명우기업은 2008년부터 택배 사업을 새로이 시작하기로 하였다. 우선 택배 화물을 모아서 처리하는 집하장을 몇 개 마련했지만, 택배 화물이 각 집하장들 사이를 오갈 때 어떤 경로를 거쳐야 하는지 결정하지 못했다. 어떤 경로를 거칠지 정해서, 이를 경로표로 정리하는 것이 여러분이 할 일이다.



예시된 그래프에서 굵게 표시된 1, 2, 3, 4, 5, 6은 집하장을 나타낸다. 정점간의 간선은 두 집하장간에 화물 이동이 가능함을 나타내며, 가중치는 이동에 걸리는 시간이다. 이로부터 얻어내야 하는 경로표는 다음과 같다.



경로표는 한 집하장에서 다른 집하장으로 최단경로로 화물을 이동시키기 위해 가장 먼저 거쳐야 하는 집하장을 나타낸 것이다. 예를 들어 4행 5열의 6은 4번 집하장에서 5번 집하장으로 최단 경로를 통해 가기 위해서는 제일 먼저 6번 집하장으로 이동해야 한다는 의미이다.

이와 같은 경로표를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 두 수 n과 m이 빈 칸을 사이에 두고 순서대로 주어진다. n은 집하장의 개수로 200이하의 자연수, m은 집하장간 경로의 개수로 10000이하의 자연수이다. 이어서 한 줄에 하나씩 집하장간 경로가 주어지는데, 두 집하장의 번호와 그 사이를 오가는데 필요한 시간이 순서대로 주어진다. 집하장의 번호들과 경로의 소요시간은 모두 1000이하의 자연수이다.

출력
예시된 것과 같은 형식의 경로표를 출력한다.

예제 입력 1
6 10
1 2 2
1 3 1
2 4 5
2 5 3
2 6 7
3 4 4
3 5 6
3 6 7
4 6 4
5 6 2
예제 출력 1
- 2 3 3 2 2
1 - 1 4 5 5
1 1 - 4 5 6
3 2 3 - 6 6
2 2 3 6 - 6
5 5 3 4 5 -
"""
import sys
sys.stdin = open('input.txt')
from heapq import heappush,heappop
def dijkstra(start,result):
    heap = []
    dp = [inf for i in range(n+1)]
    dp[start] = 0
    heappush(heap, [0, start])
    while heap:
        a, b = heappop(heap)
        for n_n, wei in arr[b]:
            n_w = a + wei
            if dp[n_n] > n_w:
                dp[n_n] = n_w
                result[n_n-1][start-1] = b
                heappush(heap, [n_w, n_n])
    return dp

n,m = map(int,input().split())
inf = sys.maxsize
arr = [[] for _ in range(n+1)]
result = [[0]*n for i in range(n)]
for _ in range(m):
    a,b,c = map(int,input().split())
    arr[a].append([b,c])
    arr[b].append([a,c])

for i in range(1,n+1):
    dp = dijkstra(i,result)
for i in range(n):
    for j in range(n):
        if i == j:
            print('-',end=' ')
        else:
            print(result[i][j],end=' ')
    print()