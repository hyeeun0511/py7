# 이름, 국어, 영어, 수학, 합계, 평균

# 3명의 학생성적을 입력받아 stus에 모두 저장하여 출력하시오.

# stus = []
# stu.append(['홍길동',100,100,100,300,100.0])

stus = []
name = input("이름을 입력하세요.")
stus.append(name)
kor = int(input("국어점수를 입력하세요."))
stus.append(kor)
eng = int(input("영어점수를 입력하세요."))
stus.append(eng)
math = int(input("수학점수를 입력하세요."))
stus.append(math)
total = kor+eng+math
stus.append(total)
avg = total/3
stus.append(avg)  
stus.append(total)  # 전체리스트

# list = input("국어성적을 입력하세요.")
# stus.append(list)
# print("성적리스트 : ",stus)

# list2 = input("영어성적을 입력하세요.")
# stus.append(list2)
# print("성적리스트 : ",stus)

# list3 = input("수학성적을 입력하세요.")
# stus.append(list3)
# print("성적리스트 : ",stus)

# stus.append(list)
# print("성적리스트 : ",stus,"")