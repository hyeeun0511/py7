# 문자열 함수
# upper() - 대문자로 변경
# lower() - 소문자로 변경
# swapcase() - 대문자는 소문자로, 소문자는 대문자로 변경
# title() - 첫글자를 대문자로 변경

# 문자열 찾기
# count() - 해당되는 문자 개수
# find() - 해당 문자 위치 검색 - 없을때 -1 리턴
# index() - 해당 문자 위치 검색 - 없을때 에러
# startswith() - 해당문자로 시작되는지 확인  # True, False
# endswith() - 해당문자로 끝나는지 확인  # True, False

# 공백제거
# strip() - 좌우 공백제거, 문자 사이 공백은 제거되지 않음.
# rstrip() - 오른쪽 공백제거
# lstrip() - 왼쪽 공백제거

# replace(변경전문자,변경후문자) - 문자열 변경

# split()   # 문자열 분리 : 타입은 리스트로 분리 해줌.

a = '1,홍길동,100,100,100,300,100.0'
titles = ['번호','이름','국어','영어','수학','합계','평균']

# print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t".format(*titles))
# a_list = a.split(",")



# # join() - 문자연결
# ss = "-"
# print(ss.join('파이썬'))


# map() : 리스트를 입력받아 처리하는 함수
# map(function함수부분,리스트데이터)

## 중요
# isdigit() : 숫자인지 확인
# isalpha() : 문자(영문자,한글) 확인
# isalnum : 문자(영문자,한글),숫자인지 확인
# islower() : 소문자인지 확인
# isupper() : 대문자인지 확인


# 국어점수를 입력하세요.
while True:
    kor = input('국어점수를 입력하세요.')
    if kor.isdigit():  # 숫자인지 확인
        break
    else:
        print("숫자가 아닙니다. 다시 입력하세요.")
        
print("숫자로 변경 : ",int(kor))



# --------------------------여기까지는 꼭 외워놓기

# def multi(x):
#     return x**2

# a = [1,2,3]
# b = list( map(multi,a) )
# print(a)
# print(b)



# a = ['100','90','80']
# print(map(int,a))
# b = list(map(int,a))             # map타입에 리스트형태로 저장됨    # 즉, map타입객체로 저장
# print(a)
# print(b)




# a = ['100','90','80']   # 숫자같은 문자를 입력받음  # str
# b = []
# for i in a:
#     print(b.append(int(i)))   # 문자형태를 숫자로 바꿔야하기때문 # int
    
# print(a)
# print(b)
# ---------------------------



# print(sep: 변수 사이사이 모두 적용 , end: 마지막에 한번 적용)
# print(*titles,sep='**') # sep 사이 간격출력          # 번호**이름**국어**영어**수학**합계**평균
# print(*titles,end='**')                            # 번호 이름 국어 영어 수학 합계 평균**    
# print("-"*50)
# print(*a_list,sep='\t')


# a_list = a.split(',')
# print(int(a_list[2]))
# b= '홍길동 유관순 이순신 김구'
# b_list = b.split('')
# print(b_list[1])




# a = "홍길동은 키가 180, 홍길동은 몸무게 70, 홍길동은 사는 곳은 서울입니다."
# print(a.replace('홍길동','홍길자'))   # : 홍길동을 홍길자로 변결시켜줘



# a = "  a   b   c  "
# print(a.replace(' ',''))  # 공백있는 부분의 공백을 다 제거
# print(a.strip())

# input1 = input("이름을 입력하세요.>> ").strip()   # strip - 좌우 공백있게 작성해도 입력됨.
# if '홍길동' == input1:
#     print("맞습니다.",input1)
# else:
#     print("틀립니다.",input1)


# input1 = input("이름을 입력하세요.>> ").replace(' ','')    # 공백을 없애줌
# if '홍길동' == input1:
#     print("맞습니다.",input1)
# else:
#     print("틀립니다.",input1)



# a = '11223333345'
# print(a.count('1'))    # a에 1이 몇개 있는지
# print(a.count('3'))    # 3 - 5개 존재

# b = '프로그램 중 파이썬 사용자가 제일 많습니다.(파이썬 프로그래밍)'
# print(b.find('파이썬'))    # 왼쪽에서 검색. 파이썬 위치 검색  # 없을때 : -1 리턴
# print(b.find('파이선'))    # 왼쪽에서 검색. 파이썬 위치 검색  # 없을때 : -1 리턴
# print(b.rfind('파이썬'))   # 오른쪽에서 검색. 순번은 그대로. 위치만 오른쪽에 있는걸로.
# print(b.index('파이썬'))   # 파이썬 위치 검색  # 없을때 : 에러
# print(b.startswith('프로그램'))   # 프로그램으로 시작하는지  # True
# c = "abc.xls"
# print(c.endswith("xls"))  # 엑셀 파일같은 파일 찾을때

# a = 'abc'
# # 대문자로 변경
# a.upper()
# print(a.upper())

# b = 'aBBccDF'
# print(b.upper())



# # 문자열
# # 문자열 슬라이싱
# a = "안녕하세요"
# # '하세'를 출력하시오.
# print(a[2:4])
# print("안녕"*3)  # 3번 반복
# print("안녕" + "hello")  # 연결연산자