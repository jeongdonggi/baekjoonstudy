m = int(input())
result = 0
num = [5, 2]

# 5로 계속 나누어 주었을 때 1, 3만 나오지 않으면 다 나누어 떨어짐

for i in num:
    result += m // i
    m = m % i  # 여기서 5로 나눈 값이 1이거나 3이면
    if m == 1 or m == 3:
        if result > 0:
            result -= 1
            m = m + i
        else:
            result = -1
            break


print(result)
