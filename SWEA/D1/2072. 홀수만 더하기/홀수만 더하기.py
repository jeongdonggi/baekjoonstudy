t = int(input())

for test in range(1, t+1):
	lst = list(map(int,input().split()))
	
	answer = 0
	
	for num in lst:
		if num % 2 == 1:
			answer += num
			
	print("#{} {}".format(test, answer))