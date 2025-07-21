n = input()  # 예: 9788975992*8

for x in range(10): # 1~ 10까지의 값
    s = 0
    for i in range(13): # 13자리
        c = n[i] # 값
        if c == '*': # *인 경우
            c = str(x) #
        c = int(c)
        if i % 2 == 0: # 1
            s += c
        else: # 
            s += c * 3
    if s % 10 == 0:
        print(x)
        break