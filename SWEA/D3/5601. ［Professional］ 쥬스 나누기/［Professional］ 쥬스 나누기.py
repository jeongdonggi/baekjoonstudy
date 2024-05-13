n = int(input())
for i in range(1, n+1):
	num = int(input())
	answer = ""
	for j in range(num):
		answer += ' 1/'+str(num)

	print("#{}{}".format(i,answer))