# 기본변수 - 1개 값을 저장                       # 종류 : int,float,str,bool
# 복합변수 - 여러개의 갑을 저장                   # 종류 : list,,dict,tuple,set
# 클래스 - 여러개의 변수, 여러개의 함수까지 저장    # 종류 : class

# 클래스 사용시 장점 - 변수,함수 함께 저장 / 변수에 접근하는 제한을 둘수있음
#                    한번에 여러개의 변수, 여러개의 함수를 바로 사용 가능
# 동일한 변수를 묶음

# # 함수 작성 방법
# def 함수명():
#     프로그램

# # class 작성 방법
# class 이름:  # 첫글자를 대문자로 작성  # ex. class Car
#     프로그램

class Car:
    # color = ""
    # speed = 0 # speed : 전역변수    
    
    # Car() (함수)객체선언일떄 __init__ 함수 호출 : 생성자      # 매개변수 : 2개 -> 무조건 매개변수가 2개인것만 받을 수 있음
    def __init__(self,color,speed):  # __init__ : 생성자(매개변수:color,speed)
        self.color = color  # 변수가 없으면 변수 생성(변수를 새롭게 만듦)
        self.speed = speed
    
    def upSpeed(self,speed):  # speed : 지역변수
        self.speed += speed   # self:global의 개념-> 밖에 있는 speed의 값을 갖고오는것 (self.speed -> speed = "0")
    
# 클래스를 사용하려면(즉, 변수,함수를 호출,변수에 값을 입력하려면), 무조건 객체선언해야 함.
# 객체선언
# 참조변수명 = 클래스명()

c = Car() # c라는 참조변수 
# c.color = "white"
# c.speed = 10


# 값읽기 - 참조변수명.변수명
print(c.color)

# 값수정 - 참조변수명.변수명 = "값"
c.color = "red"
print(c.color)  # red

c2 = Car("red",100)  # c2 -> 복합변수처럼 주소값이 있음 / 변수뿐만아니라 함수도 있음
c2.upSpeed(100)
print(c2.speed)  # 100






####-------
# a = [12,30,20]
# a[0] = 50
# print(a)  # [50, 30, 20]
# # aa = int(input("시간을 입력하세요.>> "))
# # if aa>24:
# #     print("에러입니다.")
#     # 프로그램 종료
# # a[0] = aa

# class cal:       # 선언해야 class를 사용할 수 있음         
#     __hour = 12  # 접근제한 -> 12시를 변경할수 없음
#     minute = 30
#     second = 20
    
#     def setHour(self,hour):
#         if hour>23:   # 23:59:59 -> 00:00:00
#             print("23보다 큰수는 입력을 할수 없습니다.")
#             return    
#         self.__hour = hour
#     def getHour(self):
#         return self.__hour
    
# time = cal()
# time.minute = 100
# print(time.minute)      
# # print(time.__hour)    # 클래스의 변수에 직접접근제한  , __만 넣으면 접근제한 됨
# print(time.setHour(50))   
# print(time.getHour())