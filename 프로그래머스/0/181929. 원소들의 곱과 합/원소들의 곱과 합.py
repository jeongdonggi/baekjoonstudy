def solution(num_list):
    answer = 0
    mul = 1
    s = sum(num_list) ** 2
    for num in num_list:
        mul *= num
    print(mul, s)
    if mul < s:
        return 1
    
    return answer