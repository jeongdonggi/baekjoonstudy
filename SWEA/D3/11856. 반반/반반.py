t = int(input())

for test in range(1, t+1):
    s = input()
    answer = "No"
    if s.count(s[0]) == 2:
        s = s.replace(s[0], "")
        if s.count(s[0]) == 2:
            answer = "Yes"

    print("#{} {}".format(test, answer))