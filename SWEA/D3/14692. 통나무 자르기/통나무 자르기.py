t = int(input())
mon_dic = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
for test in range(1, t+1):
	n = int(input())
	
	answer = ""
	
	if n % 2 == 0:
		answer = "Alice"
	else:
		answer = "Bob"


	print("#{} {}".format(test,answer))