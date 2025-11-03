import random
stu_list = [
    [10101,'홍길동',80,80,80,240,80.0],      
    [10102,'유관순',90,90,90,280,90.0],
    [10103,'이순신',100,100,100,300,100.0]
]
stu_count = 10104   # 학생번호  # 만약 4라고 작성하면 --- 1.홍길동 2.유관순 3.이순신 -> 다음은 4번부터 시작기때문  # 3번까지 나왔다는 의미
titles = ['번호','이름','국어','영어','수학','합계','평균']

# 학생입력부분
while True:
    print("-"*50)
    print(" "*10,"[ 학생성적프로그램 ]")
    print("-"*50)
    print("1. 학생성적입력")
    print("2. 학생성적출력")
    print("3. 학생성적수정")
    print("4. 학생성적삭제")
    print("0. 프로그램종료")
    print("-"*50)
    choice = int(input("원하는 번호를 입력하세요."))
    if choice == 1:   # 1. 학생입력
        print("[ 학생성적 입력 ]")
        name = input("{}번 학생 이름을 입력하세요.".format(stu_count))
        kor = int(input("국어성적을 입력하세요.>> "))
        eng = int(input("영어성적을 입력하세요.>> "))
        math = int(input("수학성적을 입력하세요.>> "))
        total = kor + eng + math
        avg = total/3
    if choice == 2:    # 2. 학생성적출력
        print("[ 학생성적 출력 ]")
        name = input("{}번 학생 이름을 입력하세요.".format(stu_count))
        print("-"*10,"[ 학생성적 리스트 ]")
        print(("{}\t{}\t{}\t{}\t{}\t{}\t{}\t".format(*titles)))
        for stus in stu_list:
            print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t".format(*stus))
            print()