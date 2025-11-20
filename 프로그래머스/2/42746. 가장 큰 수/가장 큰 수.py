from functools import cmp_to_key  # key 2개 이상일 경우 함수형식으로 check

def solution(numbers):
    answer = ''
    
    strs = [str(num) for num in numbers]
    
    def check(x ,y): # 함수 check - 큰 값을 맨 앞으로
        if x+y > y+x:
            return -1 # x가 앞
        elif x+y < y+x:
            return 1 # y가 앞
        else:
            return 0
        
    strs.sort(key=cmp_to_key(check)) # 함수를 이용해서 앞뒤 확인
    
    answer = "".join(strs)
    
    if answer[0] == '0': # 맨 앞이 가장 큰 수
        return '0'
    
                    
    return answer