# = 뒤의 값을 앞에 대입
# == 같다
# != 같지않다
# > 크다
# < 작다
# >= 크거나 같다
# <= 작거나 같다

num,num2 = 100,200
num3 = 300
num4 = 400
num5 = 100

# 관계연산자
print(num==num2)       # False
print(num == num5)     # True
print("5 < 7",5<7)     # False
print("5==5",5==5)     # True
print("10>=5",10>=5)   # True
print("10!=10",10!=10) # False
print("5!=10",5!=10)   # True

# and,or 논리연산자
# or - 둘다 False일때 False
# and - 앞 뒤 둘다 True일때 True // T,F/F,T/F,F - False
print("(100>50) and (100<200)",(100>50) and (100<200))  # True
print("(100>50) and (300<200)",(100>50) and (300<200))  # False

# 국어점수가 50점이거나 영어점수가 50점이상인 사람을 출력하시오. or
# 국어점수가 50점이면서 영어점수도 50점이상인 사람을 출력하시오. and