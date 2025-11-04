# 클래스       # 데이터 양이 많아서 요즘 class로 함
# 클래스 내 변수,함수를 사용하려면, 무조건 객체선언을 해야 사용할수 있음.
# 객체선언 : 참조변수 = 클래스명  (이렇게 작성하면 객체선언 쓸수있음)
class Car:
    # color = ""                         # color : 전역변수
    # speed = 0                          # color,speed 없어도 생성 가능
    

    
    ## 생성자 : 객체선언시 값을 바로 할당할수 있도록 해줌.
    def __init__(self,color,speed):    # color : 지역변수
        self.color = color             # self.변수명 시 없으면 클래스에 변수 추가해 줌.
        self.speed = speed
        self.tire = 4                  # 변수가 없으면 자동생성
    
    
    # 변수(2개)- color,speed / 함수(2개)
    # 생성자 생략 (생성자 없음)
    # 클래스내 함수(self) : self는 함수밖에 변수를 찾아서 변경하기위해 사용
    def upSpeed(self,num):
        # 함수내 변수를 선택
        self.speed += num
        
    def downSpeed(self,num):
        self.speed -= num


# 1. 객체선언후 값지정        
# c1 = Car() # 객체선언
# c1.color = '파랑'  # 변수값지정
# c1.speed = 100    # 변수값지정
# print(c1.color)
# print(c1.speed)

# 2. 생성자를 통해 값지정 - 생성자를 사용해서 프로그램을 함.
# c2 = Car('파랑',100)        # 생성자의 매개변수 개수를 맞춰야 함.
# print(c2.color)    # 파랑
# print(c2.speed)    # 100
# c2.door = 5  # 클래스에 변수가 없으면 클래스에 자동으로 추가 됨.
# print(c2.door)  # 5    # c2라는 class안에 새로운 값이 만들어짐.


        
### c1 = Car()  # 객체선언 - 변수, 함수사용
# 사용방법 - 참조변수.변수명
# 함수 - 참조변수.함수명
## print(c1.speed)
## c1.upSpeed(10)  # 클래스 내 함수 호출 - 참조변수.함수명()
## print("스피드 : ",c1.speed)


##### 퀴즈 #####

# 속도 50으로 증가, 속도 30 감소, 속도 100으로 증가
# 속도를 출력하시오.
# 색상 => 파랑으로 변경하시오.

# c1 = Car()
# c1.upSpeed(50)
# c1.downSpeed(30)
# c1.upSpeed(100)
# c1.speed = -100    # -100이라는 속도는 없음
# print(c1.speed)
# c1.color = '파랑'
# print(c1.color)
             
##----------- 직접해봄 -------틀림##
# num1 = 50
# def upSpeed(self,num1):
#     self.speed += num1
# num2 = 30
# def downSpeed(self,num2):
#     self.speed -= num2
# num3 = 100
# def upSpeed(self,num3):
#     self.speed += num3 
# c1 = Car()
# print(c1.speed)

    
