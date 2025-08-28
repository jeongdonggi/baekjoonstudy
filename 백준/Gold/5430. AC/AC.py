from collections import deque

t = int(input())

for _ in range(t):
    ps = list(input())

    n = int(input())
    arr_str = input().strip()[1:-1]

    if arr_str == "":  # 값이 없는 경우
        queue = deque()
    else:
        queue = deque(map(int, arr_str.split(',')))

    reverse = False # reverse를 계속하면 시간 초과 나기 때문
    error = False # error인 경우

    for p in ps:
        if p == 'R':
            reverse = not reverse # reverse flag만 변경
        elif p == 'D':
            if not queue:
                print("error")
                error = True
                break
            if reverse: # 맨뒤부터
                queue.pop()
            else: #맨 앞부터
                queue.popleft()

    if not error: # 에러 아닌 경우
        if reverse:
            queue.reverse()
        print("[" + ",".join(map(str, queue)) + "]")