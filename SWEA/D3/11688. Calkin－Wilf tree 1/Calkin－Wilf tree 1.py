n = int(input())

for i in range(1, n+1):
	num = input()
	lr_list = [1,1]
	for j in num:
		if j == 'L':
			lr_list[1]  = sum(lr_list)
		else:
			lr_list[0] = sum(lr_list)


	print("#{} {} {}".format(i,lr_list[0],lr_list[1]))
