"""
주어진 두 문자열의 최대 공통 부분 수열(Longest Common Sequence)의 길이를 계산하는 프로그램을 작성하시오.

예를 들어 "acaykp"와 "capcak"의 경우, 두 문자열의 최대 공통 부분 수열은 "acak"로 길이가 4이다.

최장 공통 부분문자열(Longest Common Substring)을 계산하는 것이 아님에 주의한다.

[입력]

첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

각 테스트 케이스의 첫째 줄에 두 문자열이 공백을 사이에 두고 주어진다.

각 문자열은 알파벳 소문자로만 구성되어 있음이 보장된다.

각 문자열의 길이는 1,000 이하의 자연수이다.

[출력]

각 테스트 케이스마다 ‘#T’(T는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고, 최대 공통 부분 수열의 길이를 출력한다.

입력
1
acaykp capcak

출력
#1 4
"""

import sys
sys.stdin = open('input.txt')

t = int(input())

for tr in range(t):
    arr = list(map(str, input().split()))
    result =[[0]*(len(arr[0])+1) for _ in range(len(arr[1])+1)]


    for i in range(1,len(arr[0])+1):
        for j in range(1,len(arr[1])+1):
            if arr[0][i-1] == arr[1][j-1]:
                result[i][j] = result[i-1][j-1] + 1
            else:
                result[i][j] = max(result[i-1][j], result[i][j-1])

    print('#%d'%(tr+1), result[-1][-1])