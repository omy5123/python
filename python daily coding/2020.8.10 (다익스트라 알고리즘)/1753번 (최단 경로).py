"""import sys
sys.stdin = open('input.txt')
from heapq import heappush, heappop
inf = 100000000
v, e = map(int, sys.stdin.readline().split())
k = int(sys.stdin.readline())
s = [[] for _ in range(v + 1)]
dp = [inf] * (v + 1)
heap = []
def dijkstra(start,dp,s,heap):
    dp[start] = 0
    heappush(heap, [0, start])
    while heap:
        w, n = heappop(heap)
        for n_n, wei in s[n]:
            n_w = wei + w
            if n_w < dp[n_n]:
                dp[n_n] = n_w
                heappush(heap, [n_w, n_n])
for i in range(e):
    u, v, w = map(int, sys.stdin.readline().split())
    s[u].append([v, w])
dijkstra(k,dp,s,heap)
for i in dp[1:]:
    print(i if i != inf else "INF")"""




import sys

from heapq import heappush, heappop
input = sys.stdin.readline

V, E = map(int, input().split())
k = int(input())

inf = sys.maxsize
dp = [inf]*(V+1)
arr = [[] for _ in range(V+1)]
heap = []
def dijkstra(start,dp,arr,heap):
    dp[start] = 0
    heappush(heap,[0,start])
    while heap:
        w, n = heappop(heap)
        for n_n, wei in arr[n]:
            n_w = wei + w
            if n_w < dp[n_n]:
                dp[n_n] = n_w
                heappush(heap, [n_w, n_n])

for i in range(E):
    u, v, w = map(int,input().split())
    arr[u].append([v,w])
dijkstra(k,dp,arr,heap)

for i in dp[1:]:
    if i != inf:
        print(i)
    else:
        print('INF')












