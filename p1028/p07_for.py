# 1~5 for문을 사용해서 출력하시오.
# for 변수 in 범위:
# for i in range(5):     # for :
#     print(i+1)         # 반복해야 할 내용 들여쓰기를 해야 함.

# # 숫자를 입력받아, 입력받은 값을 출력하는 것을 5번 반복하시오.
# #

# for i in range(5):
#     num = int(input("숫자를 입력하세요."))
#     print(num)
    
# 1~10까지 숫자의 합을 출력하시오. 반복 10번
# for i in range(10): # 0~9
sum = 0
for i in range(1,11,2):  # 1~10 1,3,5,7,9
    sum = sum + i
print("합계 : ",sum)   # for문 안에 있으면 10번 실행 / 바깥쪽에 있으면 총 합계 1번 실행

# 1~10까지 홀수 합계를 구하시오.
print("합계 :",sum)
# range 스탭을 사용래서 할것
sum = 0
for i in range(1,11):
    if i%2 == 1:
        sum = sum + i
print("합계 :",sum)



# # for문-
# # 구조 - for 변수 in 범위(range,list,문자열) :

# for i in range(10):
#     print(i)
    

# # 반갑습니다. 10번출력하시오.
# for i in range(10):
#     print("반갑습니다.")


#,,,?
# a_list = []
# sum = 0
# for i in range(10):
#     num = int(input("숫자를 입력하세요."))
#     if num%2 == 0:
#         break   # break : 반복문을 중지시키는 명령어
#     # append
#     a_list.append(sum)
#     sum = sum + i
#     print("합계 :",sum)
    
# print("리스트 : ",a_list)

# 합계