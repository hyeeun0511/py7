# while
stu_list = []
while True:                      # 무제한
    print("[ 학생성적프로그램 ]")
    print("1. 학생성적입력")
    print("3. 학생성적출력")
    print("3. 학생성적수정")
    print("0. 프로그램종료")
    print("-"*20)
    choice = int(input("원하는 번호를 입력하세요."))    # no -> choice / num ... 변수는 아무거나 작성가능
    # no == 0 비교
    if choice==0:                    # 0이 입력되었을때 프로그램을 빠져나옴 
        break
    elif choice==1:
        # 학생성적입력
        print("[ 학생성적입력 ]")
        name = input("이름을 입력하세요.")
    kor = int(input("국어 성적을 입력하세요."))
    eng = int(input("영어 성적을 입력하세요."))
    math = int(input("수학 성적을 입력하세요."))
    total = kor+eng+math
    avg = total/3
    stu_list.append(name)
    stu_list.append(n1)
    stu_list.append(n2)
    stu_list.append(n3)
    stu_list.append(total)
    stu_list.append(avg)
    stu_list.append[name,n1,n2,n3,total,avg]

    print("이름\t국어\t수학\t영어\t합계\t평균\t")
    print("-"*50)
    # [
    #  ['홍길동',kor,eng,math,total,avg],
    #  ['유관순',kor,eng,math,total,avg]
    # ]
    print("{}\t{}\t{}\t{}\t{}\t{:.2f}\t".format(name,kor,eng,math,total,avg))
    

print()

# while 종료후
print(stu_list)




## 문제 ## 5번 동안 숫자를 입력받아 합계를 출력하시오.
# for문, while문
# i = i + 1     =     i += 1
# i++ (X)
# ## for
# sum = 0                     # sum 필수
# # for _ in range(5):        # 가능
# for i in range(5):          # _ 안받을 때 사용   -> i라고 해놔도 상관없음
#     num = int(input("숫자를 입력하시오."))
#     sum = sum + num
#     # sum += num    # 가능 
# print("총합 : ",sum)

# ## while
# sum = 0
# i = 0
# while i<5:
#     num = int(input("숫자를 입력하세요."))
#     sum = sum + num
#     i = i + 1
    
# print("합계 : ",sum)


# # 1 ~ 10까지 합을 구하시오.
# # for
# sum = 0
# for i in range(1,11):     # 자동증감이 됨.
#     sum = sum + i
# print("총합 : ",sum)

# # while
# sum = 0
# i = 1
# while i<11:
#     sum = sum + i
#     i = i + 1  # 증감식 - 추가
# print(sum)

