"""
문제
수열 S가 어떤 수 Sk를 기준으로 S1 < S2 < ... Sk-1 < Sk > Sk+1 > ... SN-1 > SN을 만족한다면, 그 수열을 바이토닉 수열이라고 한다.

예를 들어, {10, 20, 30, 25, 20}과 {10, 20, 30, 40}, {50, 40, 25, 10} 은 바이토닉 수열이지만,  {1, 2, 3, 2, 1, 2, 3, 2, 1}과 {10, 20, 30, 40, 20, 30} 은 바이토닉 수열이 아니다.

수열 A가 주어졌을 때, 그 수열의 부분 수열 중 바이토닉 수열이면서 가장 긴 수열의 길이를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 수열 A의 크기 N이 주어지고, 둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ N ≤ 1,000, 1 ≤ Ai ≤ 1,000)

출력
첫째 줄에 수열 A의 부분 수열 중에서 가장 긴 바이토닉 수열의 길이를 출력한다.

예제 입력 1
10
1 5 2 1 4 3 4 5 2 1
예제 출력 1
7
"""
import sys
sys.stdin = open('input.txt')

a = int(input())
arr = list(map(int,input().split()))

dp = [0]*a
dp_1 = [0]*a
for i in range(a):
    dp[i] = 1
    for j in range(i):
        if arr[j] < arr[i] and dp[j]+1 > dp[i]:
            dp[i] = dp[i]+1

arr.reverse()

for i in range(a):
    dp_1[i] = 1
    for j in range(i):
        if arr[j] < arr[i] and dp_1[j] + 1 > dp_1[i]:
            dp_1[i] = dp_1[i] + 1
dp_1.reverse()
dp_2 = [0]*a
for i in range(a):
    dp_2[i] = dp[i] + dp_1[i]
print(max(dp_2)-1)




"""arr_2 = arr[i:]
    dp_2 = [0] * len(arr_2)
    for k in range(len(arr_2)):
        dp_2[k] = 1
        for n in range(k):
            if arr_2[n] > arr_2[k] and dp_2[n] + 1 > dp_2[k]:
                dp_2[k] = dp_2[k] + 1
"""