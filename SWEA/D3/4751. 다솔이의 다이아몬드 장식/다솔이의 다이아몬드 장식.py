T = int(input())

for t in range(1,T+1):
	s = input()
	lst = [[] for _ in range(5)]
	answer = ""

	lst[0] = "..#.."
	lst[1] = ".#.#."
	lst[2] = "#."+ s[0] +".#"
	lst[3] = ".#.#."
	lst[4]=  "..#.."

	line = len(s)

	for i in range(1,line):
			lst[0] += ".#.."
			lst[1] += "#.#."
			lst[2] += "."+ s[i] + ".#"
			lst[3] += "#.#."
			lst[4] += ".#.."

	for j in range(5):
		print(lst[j])
