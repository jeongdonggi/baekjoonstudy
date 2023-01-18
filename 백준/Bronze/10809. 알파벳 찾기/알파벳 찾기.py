s = input()

r = ""
for i in range(26):
    # chr(i+97) # 아스키 반환
    for j in range(len(s)):
        if (chr(i+97) == s[j]):
            r = r + str(j)
            break
        elif (j == len(s)-1):
            r = r +"-1"
    if (i != 25):
        r = r + " "
print(r)