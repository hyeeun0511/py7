## 빙고게임 (좌표맞추기 게임) ##

import random

# [ 5*5 = 25 ]
# 리스트 생성
a_list = list(range(1,26))
# 리스트 섞기
random.shuffle(a_list)
print(a_list)

while True:
    # 리스트 화면출력
    print("        [ 좌표맞추기 게임 ]")
    print("-"*50)
    for idx,a in enumerate(a_list):
        print(a,end="\t")
        if (idx+1)%5 == 0:
            print()
    print("-"*50)
    num = int(input("원하는 번호를 입력하세요.>>"))
    print()
    
    # 번호비교
    for idx,a in enumerate(a_list):
        if num == a:
            a_list[idx] = "X"       # 입력된 값이 있을시 -> X로 변환
            break