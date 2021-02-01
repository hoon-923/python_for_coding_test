import sys
r=sys.stdin.readline
N,*l=r().rstrip(),
for i in N:
	l.append(int(i))

ans=l[0] # 0
for i in range(1,len(l)):
	if l[i-1] <= 1:
		ans += l[i]
	else:
		ans *= l[i]

print(ans)
