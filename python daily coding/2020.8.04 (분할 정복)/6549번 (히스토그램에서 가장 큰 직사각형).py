import sys
sys.stdin = open('input.txt')

while True:
    N, *l=list(map(int, input().split()))
    l.append(0)
    if N == 0:
        break
    s=[]
    a=0
    for i,h in enumerate(l):
        while s and l[s[-1]]>h:
            ih=l[s.pop()]
            # s의 높이!
            w=i-s[-1]-1 if s else i
            # i에서부터 s의 top까지의 거리를 가로길이로 한다.
            # w = i일때는 마지막일 때
            if a<w*ih:
                a=w*ih
        s.append(i)
    print(a)