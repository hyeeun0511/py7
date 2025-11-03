# 함수 : 특정명령어를 집합 - 반복을 제거, 유지보수 쉽게하기위해 사용. 코드량 줄임
# print() 함수  # 프린트 함수

# # 함수형태
# def 함수명():
# 매개변수
#     pass    # 명령어 입력

# # 함수호출
# 함수명()
# 함수호출 변수 2개 -> 함수정의 변수 2개
def calculate(a,b): # 함수정의  # 함수정의는 한번만 가능 / def 있음 / : 있음     # a:10 b:2 <-- 매개변수
    print("더하기",a+b)
    print("빼기",a-b)
    print("곱하기",a*b)
    print("나누기",a/b)
    
# 함수는 호출하는것의 위에 있어야 실행 가능
a,b = 10,2
calculate(10,2) # 함수호출  # 함수호출은 여러번 할수있음 / def 없음 / : 없음
a,b = 5,3
calculate(a,b)
a,b = 2,1
calculate(a,b)


# a,b = 10,2   # a = 10  b = 2
# # print(a,b)   # 10 2
# print("더하기 :",a+b)
# print("빼기 :",a-b)
# print("곱하기 :",a*b)
# print("나누기 :",a/b)

# a,b = 5,3   # a = 10  b = 2
# # print(a,b)   # 10 2
# print("더하기 :",a+b)
# print("빼기 :",a-b)
# print("곱하기 :",a*b)
# print("나누기 :",a/b)