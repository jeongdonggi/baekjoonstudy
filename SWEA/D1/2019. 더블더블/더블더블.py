T = int(input())
lst = []
answer = ""
for test in range(T+1):
	lst.append(2**test)

answer = " ".join(str(x) for x in lst)
print(answer)