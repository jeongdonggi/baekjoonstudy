n = list(input().split('-'))

result = 0

for index, value in enumerate(n):
    plus = 0
    for j in list(map(int, (value.split('+')))):
        plus += j

    if index == 0:
        result = plus
    else:
        result -= plus

print(result)