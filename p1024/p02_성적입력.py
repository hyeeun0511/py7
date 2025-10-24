# 국어,영어,수학점수를 받아 합계와 평균을 출력하시오.

# 스스로
# num1 = kor
# num2 = eng
# num3 = mat

# num1 = int(input("국어점수를 입력하세요."))
# num2 = int(input("영어점수를 입력하세요."))
# num3 = int(input("수학점수를 입력하세요."))


# print("합계 :",num1+num2+num3)
# print("평균 :",(num1+num2+num3)/3)
# //


kor = int(input("국어점수를 입력하세요."))
eng = int(input("영어점수를 입력하세요."))
math = int(input("수학점수를 입력하세요."))
print("합계 :",kor+eng+math)
print("평균 :",(kor+eng+math)/3)
print("평균 : %.2f" % ((kor+eng+math)/3))  # 소수점의 둘째자리까지 실수로 받겠다 