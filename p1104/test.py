import stuFunc
while True:
    stuFunc.screen_print()
    choice = int(input("원하는 번호를 입력하세요.>> "))
    
    if choice == 1:
        stuFunc.stu_input()          # 입력
    elif choice == 2:
        stuFunc.stu_print()          # 출력
    elif choice == 3:
        stuFunc.stu_modify()         # 수정
    elif choice == 4:                # 삭제
        stuFunc.stu_delete()