import sys
r=sys.stdin.readline
T=int(r())
for _ in range(T): # O(T), 1<=T<=1000
	n,m=map(int,r().split()) # n=3, m=4
	gold_list=list(map(int,r().split()))
	
	gold=[]
	idx=0
	for i in range(n):
		gold.append(gold_list[idx:idx+m])
		idx+=m
	
	
	for x in range(1,m):
		for y in range(n):
			if y==0:
				left_up=0
			else:
				left_up=gold[y-1][x-1]
			
			if y==n-1:
				left_down=0
			else:
				left_down=gold[y+1][x-1]
			
			left=gold[y][x-1]
			gold[y][x]+=max(left_up, left_down, left)
	
	res=[]
	for i in range(n):
		res.append(gold[i][-1])
	
	print(max(res))
