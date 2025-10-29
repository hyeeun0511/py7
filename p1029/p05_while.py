stu_list = []
# ['홍길동',100,90,80,270,90.00]


while True:    # 지우고입력되고 지워고입력돼서 맨 마지막것만 입력됨
    # 반복시작 -------------------------
    name = input("이름을 입력하세요.")
    n1 = int(input("국어 성적을 입력하세요."))
    n2 = int(input("수학 성적을 입력하세요."))
    n3 = int(input("영어 성적을 입력하세요."))
    total = n1 + n2 + n3
    avg = total/3
    # stu_list.append(name)
    # stu_list.append(n1)
    # stu_list.append(n2)
    # stu_list.append(n3)
    # stu_list.append(total)
    # stu_list.append(avg)
    # stu_list = [name,n1,n2,n3,total,avg]
    print("이름 : {}".format(stu_list[0]))
    print("국어 : {}".format(stu_list[1]))
    print("수학 : {}".format(stu_list[2]))
    print("영어 : {}".format(stu_list[3]))
    print("합계 : {}".format(stu_list[4]))
    print("평균 : {}".format(stu_list[5]))

    print("이름\t국어\t수학\t영어\t합계\t평균\t")
    print("-"*50)
    print("{}\t{}\t{}\t{}\t{}\t{:.2f}\t".format(\
        stu_list[0],stu_list[1],stu_list[2],stu_list[3],stu_list[4],stu_list[5]))