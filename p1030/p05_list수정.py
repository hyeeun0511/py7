stu_list = [
    ['홍길동',80,80,80,240,80.0],       # 이름,국어성적,영어성적,수학성적,합계,평균  [0,1,2,3,4,5]
    ['유관순',90,90,90,280,90.0],
    ['이순신',100,100,100,300,100.0]
]
titles = ['이름','국어','영어','수학','합계','평균']      # [0,1,2,3,4,5]


while True:       # 반복 -> 점수 바꾸면 다음 점수를 바꿔도 유지  ex) 1. 홍길동 80->90  2. 홍길동 90 (유지), 유관순 90->100
    print("[ 학생성적수정 ]")
    print("0. 홍길동")
    print("1. 유관순")
    print("2. 이순신")
    print("-"*30)
    num = int(input("수정하려는 학생 번호를 입력하세요.>> "))
    print("[ {} 학생을 선택 ]".format(stu_list[num][0]))
    print("1. 국어성적수정")
    print("2. 영어성적수정")
    print("3. 수학성적수정")
    print("-"*30)
    subject = int(input("수정할 과목을 선택하세요.>> "))

    # 국어 성적 수정
    print("[ {} 학생 {}점수를 수정 ]".format(stu_list[num][0],titles[subject]))  # stu_list[num][0] -> 이름
    print("현재 {}점수 : {}".format(titles[subject] , stu_list[num][subject]))  # stu_list[num][1] -> 현재점수(성적)
    # 국어점수입력
    score = int(input("수정할 {}점수를 입력하세요.>> ".format(titles[subject])))
    stu_list[num][subject] = score  # => 점수변경
    stu_list[num][4] = stu_list[num][1]+stu_list[num][2]+stu_list[num][3]     # 변경된 합계
    stu_list[num][5] = stu_list[num][4]/3                                     # 변경된 평균 
    print(stu_list)           # 변경된 국어점수 -> stu_list                                    





# # 0. 홍길동
# # 1. 유관순
# # 2. 이순신
# # --------
# # 수정하고 싶은 학생번호를 입력하세요.
# # 국어점수를 변경하는 프로그램을 구현하시오.
# print('''\
#     [ 수정할 학생번호]
#     0.홍길동
#     1.유관순
#     2.이순신
#     '''
# )
# num = int(input("수정할 학생번호를 입력하세요.>> "))
# # 1번 선택
# # 국어점수를 70점으로 변경하고, 합계, 평균도 같이 변경해서 출력하시오.
# stu_list[1][1] = 70  # 유관순 90->70
# print(stu_list)  
# # 합계
# stu_list[1][4] = stu_list[1][1]+stu_list[1][2]+stu_list[1][3]
# # stu_list[1][4] = 250                  # 합계  # print(stu_list)를 해야 값이 변경됨
# stu_list[1][5] = stu_list[1][4]/4       # 평균  # print(stu_list)를 해야 값이 변경됨
# print(stu_list)                         # 출력




# stu_list[2][2] = 70
# stu_list[2][4] = stu_list[2][2]+stu_list[2][3]+stu_list[2][4]
# # stu_list[2][4] = 280    # 100점의 점수가 바뀌어서 다시 더해서 합계구해야함
# stu_list[2][5] = stu_list[2][4]/3

# print(stu_list)

## 89점을 출력하세요.
# print(stu_list[1][3])    # (0,1,2)  /  1번째줄(유관순)의 3번째(89)를 출력

# # 이순신을 출력하세요.
# print(stu_list[2][0])    # 2번쨰줄(이순신)의 0번쨰(이순신)을 출력

# # 이순신의 두번째 100을 80으로 변경하세요.
# stu_list[2][2] = 80      # 2번째줄(이순신)의 2번째(100)을 80(= 80)으로 변경
# print(stu_list)          # 100의 값을 80으로 변경한 전체 리스트(stu_list) 출력

# a_list = [1,2,3]
# a_list[1] = 100
# print(a_list[1])
# print(a_list)



# a_list = [1,2,3,4,5,6,7,8,9]   # len(a_list) 9                # a_list안에 9묶음이 들어있음
# b_list = [                     # len(b_list) 3                # b_list안에 세묶음이 들어있음
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]

# a_list[3] = 100     # a_list 사이에 있는 값을 100으로 바꾸기 4->100
# print(a_list)
# # b_list[1] = 100     # [4,5,6]->100
# # print(b_list)  
# b_list[1][0] = 100    # [4,5,6]->[100,5,6]
# print(b_list)
# b_list[2][1] = 50
# print(b_list)


# # 1차원 리스트 출력
# for a in a_list:           
#     print(a,end="\t")
# print()

# print("-"*50)    
# for b in b_list:
#     print 
#     print(b,end="\t")