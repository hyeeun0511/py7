# return : 함수를 호출한 곳으로 값을 전달할때 사용
# def cal(a,b):
#     a+b
#     # print(a+b)   # 함수끝을 만나면 함수종료됨.
#     # return       # return을 만나면 함수종료됨.
     
# print(cal(2,1))    # None     -> 아무일도 일어나지않음 - 값을 전달하지 않아서



# def cal(a,b):  
#     return a+b     # return으로 인해, 함수를 호출한 곳으로 값이 절달됨.
#     # print(a+b)   # 함수끝을 만나면 함수종료됨.
#     # return       # return을 만나면 함수종료됨.
    
# print(cal(2,1))    # 3



def cal(a,b):      # 매개변수는 꼭 타입을 일치시켜야 함   # cal('a',2) -> 에러 - a와 2는 계산 불가능
    return a+b     # return으로 인해, 함수를 호출한 곳으로 값이 절달됨.

# sum = cal(12323234234,5452452452)
# print(sum)
    
    

# def cal(a,b):  
#     print(a+b)     # return으로 인해, 함수를 호출한 곳으로 값이 절달됨.

# cal(10,5)   # 15
# cal(2,7)    # 9
# cal(3,5)    # 8

num1 = cal(10,5)   # 15
num2 = cal(2,7)    # 9
num3 = cal(3,5)    # 8
# num4 = cal('a',2)  # 에러 

# 3개의 계산 더하기, 뺴기를 구하시오.
print(num1+num2+num3)
print(num1-num2-num3)

    
    