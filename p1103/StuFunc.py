stu_list = [                                                                                                  # 주소값이 저장되어있음
    [10101,'홍길동',80,80,80,240,80.0],      
    [10102,'유관순',90,90,90,280,90.0],
    [10103,'이순신',100,100,100,300,100.0]
]
stu_count = 10104   # 학생번호  # 만약 4라고 작성하면 --- 1.홍길동 2.유관순 3.이순신 -> 다음은 4번부터 시작기때문        # 값이 저장되어있음
titles = ['번호','이름','국어','영어','수학','합계','평균']     

def stu_print():
    print("-"*50)
    print(" "*10,"[ 학생성적프로그램 ]")
    print("-"*50)
    print("1. 학생성적입력")
    print("2. 학생성적출력")
    print("3. 학생성적수정")
    print("4. 학생성적삭제")
    print("5. 등수처리")
    print("9. 파일저장")
    print("0. 프로그램종료")
    print("-"*50)
    
def stu_input():
    # 단순변수가 선언되면 함수에서는 변수를 새롭게 생성
    global stu_count  # 전역변수  # global을 무조건 붙여주기
    print("[ 학생성적입력 ]")
    name = input("{}번 학생이름을 입력하세요.>> ".format(stu_count))
    kor = int(input("국어점수를 입력하세요.>> "))
    eng = int(input("영어점수를 입력하세요.>> "))
    math = int(input("수학점수를 입력하세요.>> "))
    total = kor+eng+math
    avg = total/3
    # 영어,수학,합계,평균 추가하기
    stu_list.append([stu_count,name,kor,eng,math,total,avg])
    stu_count = stu_count + 1   # 학생번호 1증가
    print("성적입력이 완료되었습니다.")
    print()


def stu_print():
    print(" "*10,"[ 학생성적리스트 ]")
    print("-"*50)
    print(titles,sep="\t")    # 가장 뒤에는 \t 안넣어도 됨. 
    print("-"*50)
    for stus in stu_list:
        print("{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*stus))
    print()
