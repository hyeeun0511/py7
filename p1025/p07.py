# 숫자 2개를 입력받아 사칙연산 결과를 출력하시오.
# 10 + 5 = 15
# 10 - 5 = 5
# 10 * 5 = 50
# 10 / 5 = 2
## 문제 -  % print()를 사용해서 출력하세요.
## 풀이과정
# num = input("첫번째 숫자를 입력하세요.")  #문자열   문자열 + 문자열 = 연결   100+200=100200  =>int로 타입변경 필수
# num2 = input("두번째 숫자를 입력하세요.") #문자열
# #                  문자열,문자열,숫자-정수
# print("%s+%s=%d" % (num,num2,int(num)+int(num2)))
# print("%s-%s=%d" % (num,num2,int(num)-int(num2)))
# print("%s*%s=%d" % (num,num2,int(num)*int(num2)))
# print("%s/%s=%d" % (num,num2,int(num)/int(num2)))

# 해보기 - 하는중
num = int(input("첫번째 숫자를 입력하세요."))
num2 = int(input("두번째 숫자를 입력해주세요."))


num = int(input("첫번째 숫자를 입력하세요."))  # 문자열 -> 정수타입 
num2 = input("두번째 숫자를 입력하세요.")
print(num+int(num2))
