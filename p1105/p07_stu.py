                    # class Student:
                    #     stuno = 0
                    #     name = ""
                    #     kor,eng,math,total,avg,rank = 0     => 생성자로 받으면 필요없음

# 학생성적 1명 클래스
class Student:
    # 전역변수 만들어짐
    # stuno = 1 -> 자동으로 들어감
    def __init__(self,stuno,name,kor,eng,math):
        self.stuno = stuno     # 키(self.stuno),값(stuno)
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.total = kor+eng+math
        self.avg = self.total/3
        self.rank = 0
    
    # 객체, 또는 참조변수를 출력하면 함수실행을 시킴 
    def __str__(self):
        return (f"{self.stuno}\t{self.name}\t{self.kor}\t\
{self.eng}\t{self.math}\t{self.total}\t\
{self.avg:.2f}\t{self.rank}\t")   

    # def s_total(self,kor,eng,math):
    #     self.total = kor+eng+math 
    def s_total(self):               # 위 대신 이렇게 작성해도 됨
        self.total = self.kor+self.eng+self.math
    def s_avg(self):
        self.avg = self.total/3
            

# 학생성적리스트 클래스
class Students:
    stu_list = []
    titles = ['번호','이름','국어','영어','수학','합계','평균','등수']
    def print(self):
        print(" "*10,"[ 학생성적리스트 ]")
        print("-"*50)
        print(*self.titles,sep="\t")
        print("-"*50)
        for stus in self.stu_list:
            print(stus)
        print()
    
    def add(self,student):
        self.stu_list.append(student)


                    # stu_list = []
                    # s1 = Student(10101,'홍길동',100,100,99)   # 합계,평균,순위까지 다 들어감
                    # print(s1.total)   # 합계
                    # print(s1.avg)     # 평균
                    # stu_list.append(s1)

stus = Students()         # 객체선언

# Students 클래스에서 리스트에 추가
stus.add(Student(10101,'홍길동',100,100,99))
stus.add(Student(10102,'유관순',90,90,99))
stus.add(Student(10103,'이순신',80,80,99))

stus.print()
# print(stus.print())

# print(Student(10101,'홍길동',100,100,99))   # (Student(10101,'홍길동',100,100,99)) => 주소값 -> 추출하면 주소값이 나옴 
