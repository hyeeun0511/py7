###중요### 
# lambda() 함수 - 함수를 한줄로 간단히 만든 것

# 함수선언, 함수정의
# def add(a,b):
#     result = a + b    # 함수는 def로 시작함    # 한줄만 가능   # if문까지는 가능   result = lambda a,b  : a+b  if a>b
#     return result

# 함수호출
# print(add(10,20))     # 30

# 함수축약 lambda()
# def 선언하는 것과 같음.
# lambda 매개변수 : 함수수식
# result : 함수명(값,값)
# lambda는 간단한 함수만 가능
# result = lambda a,b  : a+b   # a와 b를 받겠다는 의미
# print(result(10,20))    # 30   # lambda는 def다.   # lambda는 함수를 축약해놓은것
# add(값,값)
# 복잡한 함수는 기본함수를 사용해야 함.
# add = lambda a,b  : a+b   
# print(add(10,20))   # 30

# cal = lambda a:a**2
# print(cal(10))   # 100   # 10이 매개변수가 됨

# result = lambda a:a%2            # lambda는 간단한 (수식)함수만 가능
# print(result(3))   # 1

# # map함수    # map : 어떤것을 반복적으로 사용할때
# # 결과값리스트 = map(함수,리스트)
# # 결과값리스트 - map타입 객체 -> list타입으로 변경
# my_list = ['0']*10
# print(my_list)          # ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
# def cal(a):
#     return a*10         # a+10 -> 10씩 더해짐   # a%2 -> 나머지값이 return 됨.

# map(함수,리스트)
# m_list = list(map(cal,my_list))   # map을 list타입으로 변경해야함
# print(m_list)

# 람다식함수 - 함수축약 / 변수 = lambda 매개변수: 수식
# map함수 - 여러개를 함수적용시킬때 사용 / 리스트 = map(함수,리스트)
my_list = [1,2,3,4,5]
m_list = list(map(lambda a:"{}원".format(a*1425),my_list))          # a:a+100 -> 무조건 100을 더해서 처리  
print(m_list)             # ['1425원', '2850원', '4275원', '5700원', '7125원']
m_list = list(map(lambda a:a*10,my_list))            
print(m_list)             # [10, 20, 30, 40, 50]
m_list = list(map(lambda a:a+100,my_list))          
print(m_list)             # [101, 102, 103, 104, 105]
my_list = ['1','2','3','4','5']  # 문자형태
m_list = list(map(lambda a:int(a),my_list))
print(m_list)             # [1, 2, 3, 4, 5]



# # 내부함수 - 함수내에 함수        # 외부에 함수를 호출해서 사용하는것
# def outFunc(a,b) :                
#     def inFunc(n1,n2):
#         return n1+n2
#     return inFunc(a,b)

# print(outFunc(10,20))   # 30

##
# def outFunc(a,b):
#     # a,b = inFunc(a,b)    # a,b를 result로 작성
#     # return a,b
#     result = inFunc(a,b)
#     return result

# def inFunc(n1,n2):
#     return n1+n2