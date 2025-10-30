stu_list = [
    ['홍길동',80,80,80,240,80.0],      
    ['유관순',90,90,90,280,90.0],
    ['이순신',100,100,100,300,100.0]
]
titles = ['이름','국어','영어','수학','합계','평균']      

# 홍길동
# 유관순
# 이순신
# stu_list파일을 가지고 이름을 출력

for stus in stu_list:
    print(stus[0])
    
# 홍길동 80
# 유관순 90
# 이순신 100
# stu_list파일을 가지고 이름을 출력

# for stus in stu_list:
#     print(stus[0],stus[1])
    
for stus in stu_list:
    # print("{}\t{}\t".format(*stus))
    print("{}\t{}".format(*stus))
    
# 1.홍길동 0 
# 2.유관순 1 
# 3.이순신 2
# stu_list파일을 가지고 이름을 출력
while True:
    print("[ 학생성적삭제 리스트 ]")
    for idx,stus in enumerate(stu_list):
        print("{}. {}".format(idx+1,stus[0]))
    print("-"*50)
    num = int(input("삭제하려는 번호를 입력하세요.>> "))  # 1->0
    del stu_list[num-1]
    print(stu_list)



# a_list = [1,2,3]
# del a_list[0]

# pop()      # 가장 뒤 삭제
# remove()   # 값 삭제
# clear()    # 전부 삭제