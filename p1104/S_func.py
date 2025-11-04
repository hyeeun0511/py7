# 학생"1명"의 성적을 저장하는 클래스
class Student:     # class 다음은 무조건 대문자로 시작
    def __init__(self,stuno,name,kor,eng,math):  # 생성자 - 객체선언시 함수호출
        self.stuno = stuno  # self 자동으로 변수생성
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.total = kor+eng+math
        self.avg = self.total/3   
        self.rank = 0     
  

    def sum(self):
        # self.total = self.kor+sel.eng+self.math
        return self.kor+self.eng+self.math
    def avg(self):
        return self.total/3

# 학생성적"들"을 저장하는 클래스
class Stuscore:
    stu_list = []
    titles = ['번호','이름','국어','영어','수학','합계','평균','등수']
    # def __init__(self,s):   # s -> student
    #     self.stu_list.append(
    #         {'stuno':s.stuno,'name':s.name,'kor':s.kor,'eng':s.eng,'math':s.math,\
    #  'total':s.total,'avg':s.avg,'rank':s.rank}
    #     )
    
    # 학생성적 1명 추가함수     # 위에서는 선언안해도 됨.  # add에만 객체선언하면 됨
    def add(self,s):
        self.stu_list.append(
            {'stuno':s.stuno,'name':s.name,'kor':s.kor,'eng':s.eng,'math':s.math,\
     'total':s.total,'avg':s.avg,'rank':s.rank}
        )
        print("학생이 추가 되었습니다.")

    # 학생성적 출력함수
    def print(self):
        # print(self.stu_list)   # 이 값을 실행시킬시 -> 학생성적리스트가 한줄로 나옴
        print(" "*10,"[ 학생성적리스트 ]")
        print("-"*50)
        print(*self.titles,sep="\t")
        print("-"*50)
        for stus in self.stu_list:
            print(f"{stus['stuno']}\t{stus['name']}\t{stus['kor']}\
\t{stus['eng']}\t{stus['math']}\t{stus['total']}\
\t{stus['avg']:.2f}\t{stus['rank']}")
            
        print()