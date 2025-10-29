n_list = []
i = 0
while True:    # 무한대로 받을수있음
    if i<4:
        name = input("{} 번째 이름을 입력하세요.".format(len(n_list)+1))
        kor = int(input("{} 번째 국어점수를 입력하세요.".format(len(n_list)+1)))
        n_list.append([name,kor])
        print(n_list)
        i = i + 1
    else:
        break      # 2보다 작지않으면 멈춤  # 즉, 2번 돌면 멈춤
    
# 전체 출력  [['홍길동', 100], ['유관순', 90], ['이순신', 80], ['김구', 95]]
print("  [ 학생성적프로그램 ]")
print("이름\t국어\t영어\t수학\t합계\t평균")
print("-"*50)
for i in range(len(n_list)):     # 0,1,2,3
    print("{}\t{}".format(n_list[i]))




# n_list = []

# n_list.append(1)
# n_list.append(2)
# n_list.append(3)
# n_list.insert(0,5)
# n_list.insert(2,100)
# n_list.extend([10,20,30])  # list타입을 추가
# n_list.append([10,20,30])
# n_list.append([100,200,300])
# n_list.append(['홍길동',100])
# print(n_list)


# while True:      # while 반복
#     # 반복시작 -----------
#     name = input("이름을 입력하세요.")
#     n_list = [name]
#     print("이름")
#     print("-"*50)
#     print("{}".format(name))
#     #--------------------


# 틀림..
# while True:      # while 반복
#     # 반복시작 -----------
#     name = input("이름을 입력하세요.")
#     n_list.append(name)
#     print(n_list)
#     #--------------------


# a_list = []

# a_list = ['홍길동',100,90]