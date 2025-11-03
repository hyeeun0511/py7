def cal(a,b):
    print("[ 사칙연산 ]")
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)
    

# 두수를 입력해서 사칙연산을 하시오. 함수를 사용할것
while True:      # if a == 0 이 없다면 - 무한 반복
    a = int(input("숫자를 입력하세요.(0.프로그램 종료)>> "))
    if a == 0:   # 무한 반복을 멈추기 위해
        print("프로그램을 종료합니다.!! ")
        break
    b = int(input("숫자를 입력하세요.>> "))
    cal(a,b)

    
# # 문제 ##  두수를 입력해서 사칙연산을 하시오. 함수를 사용할것
# i = 0
# a_list = [0,0]
# while True:  # 무한대로 돌리기 위해서
#     a = input("숫자를 입력하세요.") # str(input)
#     if a.isdigit():  # 숫자인지 확인
#         a_list[i] = int(a)   # 타입변환
#         i += 1       # 1증가
#     else : print("숫자만 입력가능합니다.!!")
#     if i == 2 : break
#     # b = input("숫자를 입력하세요.")
#     # if b.isdigit():  # 숫자인지 확인
#     #     b = int(b)   # 타입변환
#     #     i += 1       # 1증가
#     # else: print("숫자만 입력가능합니다.!!")
# cal(a_list[0],a_list[1])  # 호출

# # 무한반복되도록 하시오.
# # 0을 입력하면 프로그램을 종료하시오.





# def kor_hello(a):
#     print("[ 반복 회수 ]")
#     for i in range(a):
#         print("안녕하세요.")
    
    
# kor_hello(10)   # 안녕하세요 10번 반복
# kor_hello(7)    # 안녕하세요 7번 반복
# kor_hello(5)    # 안녕하세요 5번 반복