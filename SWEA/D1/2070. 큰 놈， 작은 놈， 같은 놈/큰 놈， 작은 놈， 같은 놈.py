n = int(input())

for i in range(1, n+1):
	a, b = map(int,input().split())
	if a -b > 0:
		print("#{} {}".format(i,'>'))
	elif a - b < 0:
		print("#{} {}".format(i, '<'))
	else:
		print("#{} {}".format(i, '='))