# 조건문 - if문
# 반복문 - 여러번 실행
# for, while

# 문자열,리스트 슬라이싱[시작:끝-1:스탭]
# range - 범위 , range(10) 10번반복
# range(시작,끝-1,스탭), range(끝):0 ~ 끝-1 (0번부터 끝 바로 앞에까지라는 뜻)
# for 변수 in 범위 - 문법

for i in range(10):       # 0 ~ 10-1   # 0번부터 9번까지 입력
    print(i)
    
for i in range(5):        # 0~4 5번 실행
    print("안녕하세요.")
    
for _ in range(5):        # 0~4 5번 실행
    print("hello")
    
for i in range(5):        # 0~4 5번 실행
    print(i,"번째 안녕")    # 0번부터 시작
    
for i in range(5):
    print(i+1,"번째 안녕")  # 1번부터 시작하기위해 i+1 
     
for i in range(1,6):       # 1~5 5번 실행
    print(i,"번째")
    
for i in range(1,11):      # 0~10 10번 실행
    print(i)
    
sum = 0
for i in range(1,11):
    sum = sum + i
    print(i,"번째: ",sum)
    
sum = 0
for i in range(1,11):
    sum = sum + i
    print("{}번째: {}".format(i,sum))
    
print("총합계 : ",sum)


a_list = ["홍길동",100,90,80]
for a in a_list:  # a_list[0],a_list[1],a_list[2],a_list[3]
    print(a)
    
# 2차원리스트 - for문 2번, 3차원리스트 - for문 3번

name ="홍길동유관순이순신"   # "홍길동유관순이순신" <= 하나의 리스트임
for i in name:
    print(i)

# range() 숫자를 입력하세요 10번출력
print("숫자를 입력하세요")
for i in range(10):
    print(i+1,"번째 숫자를 입력하세요")
    input()
    
for i in range(10):
    print("{}번째 숫자를 입력하세요".format(i+1))
    # print(i+1, "번째 숫자를 입력하세요.")
    
for i in range(10):
    num = int(input("{}번째 숫자를 입력하세요.".format(i+1)))
    snm = sum + num
    print("합계 :",sum)
    

# 입력받기
    
# sum = 0
# for i in range(1,11):
#     sum = sum + i
# print("합계 : ",sum)