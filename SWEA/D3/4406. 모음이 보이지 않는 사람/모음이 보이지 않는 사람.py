n = int(input())

for i in range(1, n+1):
	s = input()
	s = s.replace('a','').replace('e','').replace('i','').replace('o','').replace('u','')
	print("#{} {}".format(i,s))