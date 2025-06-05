arr = list(map(int, input().split()))

if arr[0] == 1:
    r = True
    for i in range(len(arr)):
        if arr[i] != i + 1:
            print("mixed")
            r = False
            break

    if r:
        print("ascending")

elif arr[0] == 8:
    r = True
    for i in range(len(arr) - 1, -1, -1):
        if arr[7 - i] != i + 1:
            print("mixed")
            r = False
            break
    if r:
        print("descending")

else:
    print("mixed")