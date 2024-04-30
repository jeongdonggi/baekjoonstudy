def solution(myString, pat):
    answer = 0
    rev_pat = ""
    for p in pat:
        if p == "A":
            rev_pat += chr(ord(p)+1)
        else:
            rev_pat += chr(ord(p)-1)
    answer = 1 if rev_pat in myString else 0
    return answer