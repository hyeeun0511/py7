# 학생성적입력,출력,수정,삭제를 구현하시오.

import random
stu_list = [
    [10101,'홍길동',80,80,80,240,80.0],      
    [10102,'유관순',90,90,90,280,90.0],
    [10103,'이순신',100,100,100,300,100.0]
]
stu_count = 10104   # 학생번호  # 만약 4라고 작성하면 --- 1.홍길동 2.유관순 3.이순신 -> 다음은 4번부터 시작기때문  # 3번까지 나왔다는 의미
titles = ['번호','이름','국어','영어','수학','합계','평균']     


# 학생 성적 프로그램
while True:
    print("-"*50)
    print(" "*10,"[ 학생성적프로그램 ]")                                    # [학생성적프로그램]
    print("-"*50)
    print("1. 학생성적입력")
    print("2. 학생성적출력")
    print("3. 학생성적수정")
    print("4. 학생성적삭제")
    print("0. 프로그램종료")
    print("-"*50)
    choice =int(input("원하는 번호를 입력하세요.>> "))                       # 1.학생성적입력~4.학생성적삭제 번호중 
    
    # 1. [학생성적입력]
    if choice == 1:                                                       
        print("[ 학생성적입력 ]")
        print("-"*50)
        name = input("{}번 학생의 이름을 입력하세요.".format(stu_count))      # stu_count : 학생번호
        kor = int(input("국어성적을 입력하세요.>> "))                        # 국어성적-숫자  =>  int
        eng = int(input("영어성적을 입력하세요.>> "))
        math = int(input("수학성적을 입력하세요.>> "))
        total = kor+eng+math                                              # 합계
        avg = total/3
        # 영어,수학,합계,평균 추가
        # 나열 append
        stu_list.append([stu_count,name,kor,eng,math,total,avg])
        stu_count = stu_count + 1                                          # 학생 번호 1 증가
        print("학생성적입력이 완료되었습니다.")
        
    # 2. [학생성적출력]    
    elif choice == 2:                               
        print("[ 학생성적출력 ]")
        print("-"*50)
        name = input("{}번 학생의 이름을 입력하세요.".format(stu_count))
        print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t".format(*titles))              # '번호','이름','국어','영어','수학','합계','평균'
        print("-"*50)
        for stus in stu_list:                                              # for   in
            print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t".format(*stus))
    
    # 3. [학생성적수정]
    elif choice == 3:                                                      
        print("[ 학생성적수정 ]")
        print("-"*50)
        name = input("{}번 학생의 이름을 입력하세요.".format(stu_count))      # stu_count : 학생번호
        kor = int(input("국어성적을 입력하세요.>> "))                        # 국어성적-숫자  =>  int
        eng = int(input("영어성적을 입력하세요.>> "))
        math = int(input("수학성적을 입력하세요.>> "))
        total = kor+eng+math                                              # 합계
        avg = total/3
        
    # 4. [학생성적삭제]
    elif choice == 4:
        print("[ 학생성적삭제 ]")                                             
        for idx,stus in enumerate(stu_list):                                # enumerate , 학생리스트
            print("{} {} {}".format(idx+1,stus[0],stus[1]))
        choice = int(input("삭제할 번호를 입력하세요.>> "))
        choice = int(input("삭제하시겠습니까?>> 1.Yes  2.No "))
        if choice == 1:
            print("삭제되었습니다.")
            
            
        if choice == 2:
            print("취소되었습니다.")
    
    # 0. [프로그램종료]
    elif choice == 0:
        print("[ 프로그램이 종료되었습니다. ]")