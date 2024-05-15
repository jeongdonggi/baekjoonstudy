t= int(input())

for i in range(1, t+1):
	a ,b = map(int, input().split())
	lst = list(map(int, input().split()))

	lst = sorted(lst,reverse=True)
	print("#{} {}".format(i,sum(x for x in lst[:b])))