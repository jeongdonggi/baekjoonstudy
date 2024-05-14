t = int(input())
mon_dic = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
for test in range(1, t+1):
	a,b = map(int, input().split())
	n = [[] for _ in range(a)]

	answer = 0

	for i in range(a):
		n[i] = list(map(int, input().split()))

	# 흰색이 1 검은색이 0

	for i in range(a):
		s = ""
		lst = []
		for j in n[i]:
			s += str(j)
		lst = list(s.split('0'))
		for k in lst:
			if len(k) == b and len(lst) != 1:
				answer += 1

	for i in range(a):
		s = ""
		lst = []
		for j in range(a):
			s += str(n[j][i])
		lst = list(s.split('0'))
		for k in lst:
			if len(k) == b and len(lst) != 1:
				answer += 1



	print("#{} {}".format(test,answer))