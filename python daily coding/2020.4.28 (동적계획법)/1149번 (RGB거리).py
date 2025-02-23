"""

시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
0.5 초 (추가 시간 없음)	128 MB	42429	19878	14951	47.726%
문제
RGB거리에는 집이 N개 있다. 거리는 선분으로 나타낼 수 있고, 1번 집부터 N번 집이 순서대로 있다.

집은 빨강, 초록, 파랑 중 하나의 색으로 칠해야 한다. 각각의 집을 빨강, 초록, 파랑으로 칠하는 비용이 주어졌을 때, 아래 규칙을 만족하면서 모든 집을 칠하는 비용의 최솟값을 구해보자.

1번 집의 색은 2번 집의 색과 같지 않아야 한다.
N번 집의 색은 N-1번 집의 색과 같지 않아야 한다.
i(2 ≤ i ≤ N-1)번 집의 색은 i-1번, i+1번 집의 색과 같지 않아야 한다.
입력
첫째 줄에 집의 수 N(2 ≤ N ≤ 1,000)이 주어진다. 둘째 줄부터 N개의 줄에는 각 집을 빨강, 초록, 파랑으로 칠하는 비용이 1번 집부터 한 줄에 하나씩 주어진다. 집을 칠하는 비용은 1,000보다 작거나 같은 자연수이다.

출력
첫째 줄에 모든 집을 칠하는 비용의 최솟값을 출력한다.

예제 입력 1
3
26 40 83
49 60 57
13 89 99
예제 출력 1
96
"""
import sys
sys.stdin = open('input.txt')
N = int(input())
cost_per_home = []

# 각 집마다 색깔 별 가격을 저장한다.
for _ in range(N):
    cost_per_home.append(list(map(int, input().split())))

    dp = [cost_per_home[0]]

for i in range(1, N):
    cost_per_color = []

    temp_red = min(dp[i - 1][1], dp[i - 1][2])

    cost_per_color.append(temp_red + cost_per_home[i][0])

    temp_green = min(dp[i - 1][0], dp[i - 1][2])
    cost_per_color.append(temp_green + cost_per_home[i][1])

    temp_blue = min(dp[i - 1][0], dp[i - 1][1])
    cost_per_color.append(temp_blue + cost_per_home[i][2])

    dp.append(cost_per_color)

print(min(dp[N - 1]))