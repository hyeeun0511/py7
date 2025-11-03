# 함수의 매개변수는 개수를 맞춤

# 매개변수 개수는 호출하는 변수의 개수와 동일   # 동일하지 않으면 에러
# 매개변수 타입도 호출하는 변수타입과 일치      # 일치하지 않으면 에러
# def add(a,b):
#     return a+b

# a = add(1,2)
# print(a)    # 3

# 가변 매개변수
# def add(a,b,*c): # 변수 앞에 *를 붙이면 가변매개변수가 됨.
#     sum = a+b
#     for i in c:  # c:여러개 가능
#         sum += i
#     return sum

# print(add(1,2,3,4,5,6,7,8,9,10))         # a=1 b=2 *C=3,4,5,6,7,8,9,10  # *c -> list 타입으로 바뀜

# print(add(1,2,3))  # 6
# print(add(1,2,3,4))  # 10       # 매개변수가 똑같지않아도 가능

#

# def print_str(*c):
#     for i in c:
#         print(i)
        
# print_str("안녕","사과","홍길동","점수",100)


# ## 여러개를 입력받아, 함수를 사용해서 출력하세요.
# a_input = []

# def print_str(*c):
#     for i in c:
#         print(i)
        

# ## 5번 입력받아, 모두 출력하시오.
# str1 = [0,0,0,0,0]  # 5번 입력받음 # 이렇게 먼저 만들어줘야 에러가 나지않음 
# for i in range(5):
#     str1[i] = input("문자를 입력하세요.>>> ")
    
# print_str(*str1)    # *str1 = str1[0],str1[1],str1[2]
# print_str(str1[0],str1[1],str1[2])



stus = [1,'홍길동',100,90,80]

# 국어, 영어, 수학 점수를 입력받아, return을 적용
def sum(kor,eng,math):
    return kor+eng+math

def avg(kor,eng,math):
    return (kor+eng+math)/3

# stus = [1,'홍길동',100,90,80]
# 함수를 제대로 구성해서 stus 리스트를 아래와 같이 변경하세요.
# stus = [1,'홍길동',100,90,80,270,90.00] 으로 변경하세요.
# 함수를 꼭 사용할 것.

stus.append(sum(stus[2],stus[3],stus[4]))    # 합계가 추가적으로 들어감
print(stus)
stus.append(avg(stus[2],stus[3],stus[4]))    # 평균이 추가적으로 들어감
print(stus)                                             
