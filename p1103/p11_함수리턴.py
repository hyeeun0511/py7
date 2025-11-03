# return : 함수호출로 값을 전달할때 사용

def cal(a,b):
    return a+b  # 함수호출로 값을 전달

sum = cal(1,2)  # 함수호출

def func(a,b):
    a+b
    return      # return값이 없으면 함수종료  # a+b에대한 것을 return해주지않음 -> return자리에 있는것만 return해줌

def big(a,b):
    if a>b:
        return a
    else:
        return    # -> 아무것도 돌리지않겠다는 의미  # 뭔가는 돌려줘야하기에 return입력
    
def big(a,b):
    c = 0
    if a>b:
        return a
    else:
        return -1