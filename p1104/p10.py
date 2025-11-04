# 클래스 선언   # init함수 사용
class Student:
    def __init__(self,stuno,name,kor,eng,math):  # stuno:student number
        self.stuno = stuno
      # global.stuno
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.total = kor+eng+math   # = self.kor+self.eng+self.math
        self.avg = self.total/3
        self.rank = 0
      
    # 합계
    def total_f(self):      # def + 함수명()     # class 내에 있는 변수를 사용해야하기 때문에 self 작성 필수
        self.total = self.kor+self.eng+self.math
    # 평균
    def avg_f(self):
        self.avg = self.total/3
        
# 매개변수 __init__함수 매개변수 개수와 맞아야 함. 5개를 (맞춰서)넘겨줘야 함.
s = Student(10101,'홍길동',80,80,80)    # init을 실행시키라는 의미   # s안에 홍길동의 국,영,수,합계,평균,등수 다 들어가있음
                                       # Student를 선언하고 init에 값을 넘겨서 실행됨
print("국어 : ",s.kor)   
print("합계 : ",s.total) 
s.kor = 100             
print("국어 : ",s.kor)    # 국어점수를 100점으로 수정
s.total_f()               # 바뀐 국어점수 포함한 합계(total)

