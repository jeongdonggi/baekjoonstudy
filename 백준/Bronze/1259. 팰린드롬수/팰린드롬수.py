arr = []
result = []

while True:
    n = input()
    if n == "0":
        break
    else:
        arr.append(n)

for a in arr:
    left = 0
    right = len(a) - 1
    r = "yes"

    while left <= right:
        if a[left] != a[right]:
            r = "no"
            break

        left += 1
        right -= 1

    result.append(r)

print("\n".join(result))