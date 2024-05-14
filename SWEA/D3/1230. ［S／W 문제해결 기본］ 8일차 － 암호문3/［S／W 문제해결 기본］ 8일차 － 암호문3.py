for test in range(10):
	first = int(input())
	second = list(map(int, input().split()))
	third = int(input())
	fourth = list(input().split())

	for key, value in enumerate(fourth):
		if value == 'I':
			for i in range(int(fourth[key+2])):
				second.insert(int(fourth[key+1])+i, int(fourth[(key+3)+i]))
			# second.insert(int(fourth[key+1]),fourth[key+3:(key+3)+int(fourth[key+2])])
		elif value == 'D':
			second = second[:int(fourth[key+1])] + second[int(fourth[key+1])+int(fourth[key+2]):]
		elif value == 'A':
			second += fourth[key+2: (key+2)+int(fourth[key+1])]

	answer = " ".join(str(x) for x in second[:10])
	print("#{} {}".format(test+1,answer))