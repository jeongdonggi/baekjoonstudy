t = int(input())

mirror_dic = {'b': 'd', 'd': 'b', 'p' : 'q', 'q' : 'p'}

for test in range(1, t+1):
	s = input()
	answer = ""
	for i in s[::-1]:
		answer += str(mirror_dic.get(i))

	print("#{} {}".format(test,answer))