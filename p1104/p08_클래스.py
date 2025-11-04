# 클래스가 2개 있음
# 
from S_func import *






# s1 = Student(10101,'홍길동',80,80,80)
# s2 = Student(10102,'유관순',90,90,90)
# s3 = Student(10103,'이순신',100,100,100)

# # 학생성적 "들" 저장
# students = Stuscore()    # 객체선언 - 객체선언을 해야 공간이 나옴
# students.add(s1)   # 홍길동 학생이 추가됨    # 학생이 추가 되었습니다.
# students.add(s2)   # 유관순 학생이 추가됨    # 학생이 추가 되었습니다.
# students.add(s3)   # 이순신 학생이 추가됨    # 학생이 추가 되었습니다.

students = Stuscore()   # 객체선언
students.add(Student(10101,'홍길동',80,80,80))   # 홍길동
students.add(Student(10102,'유관순',80,80,80))   # 유관순
students.add(Student(10103,'이순신',80,80,80))   # 이순신

students.print()