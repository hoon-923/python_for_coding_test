import sys
r=sys.stdin.readline
N=int(r())
l=list(map(int,r().split()))
l.sort()
money=1
for i in l:
	if i > money:
		print(money)
		break
	else:
		money += i
