weekend = ['MON','TUE','WED','THU','FRI','SAT','SUN']
n = int(input())
for i in range(1, n+1):
	s = input()
	answer = 7 if weekend.index(s)+1 == 7 else 7-(weekend.index(s)+1)
	print("#{} {}".format(i,answer))