import sys
a = int(sys.stdin.readline())

for i in range(a):
    b, c = map(int, sys.stdin.readline().split())
    print("Case","#%d:"%(i+1),b,"+",c,"=",b+c)