# 클래스 선언
# __init__함수사용
class Student:
    def __init__(self,stuno,name,kor,eng,math):     # __init__ : 생성자 - 객체선언시 바로 실행되는 함수
        self.stuno = stuno    # self.stuno : 전역변수(class내에서만 사용하는)   / stuno : 지역변수(함수내에서만 사용하는)
      # global.stuno
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.total = kor+eng+math  # self.kor+self.eng+self.math  와 같음
        self.avg = self.total/3
        self.rank = 0
        
    # 합계
    def total_f(self):   # self 무조건 넣기
        self.total = self.kor+self.eng+self.math   # 호출만 받아도 이미 total안에 들어가있음
    # 평균
    def avg_f(self):
        self.avg = self.total/3

# 매개변수 __init__함수 매개변수 개수와 맞아야 함. 5개를 넘겨줘야 함.
s = Student(10101,'홍길동',80,80,80)    # <-- init을 실행시키라는 의미   # s안에 홍길동의 국,영,수,합계,평균,등수까지 다 들어가있음
print("국어 : ",s.kor)   # 80
print("합계 : ",s.total) # 240
s.kor = 100
print("국어 : ",s.kor)   # 100
s.total_f() # 바뀐 국어점수 포함한 합계
s.avg_f()   # 평균
print("합계 : ",s.total) # 260
print("평균 : ",s.avg) # 260


# #--------------------------------------------------
# 클래스 선언 
# class Student:
#     pass    # 아무것도 안넣음
# s = Student()     # 객체선언   # 객체선언하지않으면 공간이 안만들어짐
# s.stuno = 10101     # 변수추가
# print(s.stuno)    # 변수출력   # 10101

# #--------------------------------예전방법------------간단한 프로그램 할 시 이렇게-----
# stuno = 10101
# print(stuno)
