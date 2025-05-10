n = 1000 - int(input())

moneys = [500, 100, 50, 10, 5, 1]

result = 0

for money in moneys:
    result += n // money
    n = n % money

print(result)