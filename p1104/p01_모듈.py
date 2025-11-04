# # 모듈 : 함수의 집합  (어떤 함수든 상관없음)
# # 다른 파일의 모듈을 사용하려면, import을 해야 사용가능 
# # import를 하면 모듈이름(파일이름).함수명으로 호출해야 함.

# import Func  # Func.py의 모든 함수를 가져옴.

# # 
# Func.func1()  # Func이라는 파일 안의 func1을 가져오라는 뜻
#               # Func.py 모든 함수를 가져옴.
# import random

# # import 이름. 함수명으로 사용
# print(Func.func1())  
# random.sample()


# ###
# def func1():
#     return "안녕"   # 밑에 있으면 에러. 
# # Func.func1() 을 사용해야 import Func안에있는 Func을 사용할수있음

# def func2():
#     return "hello"

# print(func1())   # 안녕     # 함수호출은 항상 함수정의보다 아래에 있어야 함.
# # print(Func.func1())  


# from 파일명 import 함수를 정의하면(사용하는 함수를 지정하면) 파일명(Func)을 생략가능
# 모듈명 생략가능
# from + 모듈명 / import + 변수,함수,클래스 
# 유사한 함수 그룹에 묶어두면 사용하기 편함.
# from Func import func1
# print(func1())   # 안녕

# from Func import * # Func안에있는것을 가져옴
# print(func1())     # 안녕
# func2        # 함수사용
# s1 = stu()   # 클래스사용


# 예제
# 수학공식
# from math import sin,cos,tan,floor,ceil         # round 포함시키지말아야함 -> 포함시킬시 에러!!
# # floor 소수점 버림, ceil 소수점 올림, round 반올림
# print(floor(1.95))  # 1   # from을 했기때문에 floor를 바로 사용할수있음   
# print(ceil(1.2))    # 2
# print(round(1.59))  # 2   # round : 내장함수 -> import를 하지않아도 사용할수있게 해줌  

# import random
# print(random.randint(1,6))   # 1부터 5 사이에있는 숫자중 하나만 뽑아오는것
# 모듈이름이 너무 길때 줄여 사용가능 : as 별칭  # 약식으로 사용
# 어디 출처인지, 어디에서 가져온건지 적어놓는게 좋음
# import random as r         # import -> 최상단에 둠       # 같은 함수가 있으면 충돌함
# import math                # import -> 최상단에 둠    
# print(r.randint(1,6))
# # dir : 모듈안에 모든 함수를 보여주는 명령어 
# print(dir(math))  # math안에 있는 모든 함수를 보여줌.
# print(dir(r))     # random안에 모든 함수를 랜덤으로 보여줌.

# 날짜와 시간을 가져오는 모듈
# 파이썬 - 날짜, html - 날짜, 자바스크립트 - 날짜, db - 날짜
import datetime 
now = datetime.datetime.now()
print(now)       # 2025-11-04 10:24:12.831620
print(now.year)  # 2025   # 올해 연도 출력   # year,month,day,hour,minute,second

import time
print("a")     # a
time.sleep(5)  # 5초동안 대기   # 5초 후에 다음(밑에) 내용 출력됨
print("b")     # b


# 패키지 : 모듈파일을 모아둔 폴더
# from Func import func1
# from 폴더명.모듈명 import 변수,함수,클래스.*(*:모든걸 갖고오고싶을때)
# from 폴더명 import 모듈명

# from cal.Func import*
# from cal.Func import*
# print(func1())
# from cal import Func
# print(Func.func1())
