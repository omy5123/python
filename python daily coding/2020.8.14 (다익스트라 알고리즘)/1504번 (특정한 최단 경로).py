"""
문제
방향성이 없는 그래프가 주어진다. 세준이는 1번 정점에서 N번 정점으로 최단 거리로 이동하려고 한다. 또한 세준이는 두 가지 조건을 만족하면서 이동하는 특정한 최단 경로를 구하고 싶은데, 그것은 바로 임의로 주어진 두 정점은 반드시 통과해야 한다는 것이다.

세준이는 한번 이동했던 정점은 물론, 한번 이동했던 간선도 다시 이동할 수 있다. 하지만 반드시 최단 경로로 이동해야 한다는 사실에 주의하라. 1번 정점에서 N번 정점으로 이동할 때, 주어진 두 정점을 반드시 거치면서 최단 경로로 이동하는 프로그램을 작성하시오.

입력
첫째 줄에 정점의 개수 N과 간선의 개수 E가 주어진다. (2 ≤ N ≤ 800, 0 ≤ E ≤ 200,000) 둘째 줄부터 E개의 줄에 걸쳐서 세 개의 정수 a, b, c가 주어지는데, a번 정점에서 b번 정점까지 양방향 길이 존재하며, 그 거리가 c라는 뜻이다. (1 ≤ c ≤ 1,000) 다음 줄에는 반드시 거쳐야 하는 두 개의 서로 다른 정점 번호 v1과 v2가 주어진다. (v1 ≠ v2, v1 ≠ N, v2 ≠ 1)

출력
첫째 줄에 두 개의 정점을 지나는 최단 경로의 길이를 출력한다. 그러한 경로가 없을 때에는 -1을 출력한다.

예제 입력 1
4 6
1 2 3
2 3 3
3 4 1
1 3 5
2 4 5
1 4 4
2 3
예제 출력 1
7
"""
import sys
input = sys.stdin.readline
from heapq import heappush, heappop

def dijkstra(start,arr,heap):
    dp = [inf]*(m+1)
    dp[start] = 0
    heappush(heap,[0,start])
    while heap:
        w, n = heappop(heap)
        for n_n, wei in arr[n]:
            n_w = wei + w
            if n_w < dp[n_n]:
                dp[n_n] = n_w
                heappush(heap, [n_w, n_n])
    return dp

m,e = map(int,input().split())
inf = sys.maxsize
arr = [[] for _ in range(m+1)]
heap = []
for _ in range(e):
    u, v, w = map(int,input().split())
    arr[u].append([v, w])
    arr[v].append([u, w])
v_1,v_2 = map(int,input().split())
one = dijkstra(1,arr,heap)
v1 = dijkstra(v_1,arr,heap)
v2 = dijkstra(v_2,arr,heap)
result = min(one[v_1]+v1[v_2]+v2[m],one[v_2]+v2[v_1]+v1[m])
if result < inf:
    print(result)
else:
    print(-1)
