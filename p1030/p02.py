## 빙고게임같음

import random
# 3*3(3콤마 3) 리스트 출력
a_list = list(range(1,10))
print(a_list)

# 랜덤섞기
random.shuffle(a_list)
print(a_list)

# 무한반복 실행 ---------------------------------
while True:
    print("[ 좌표 맞추기 게임 ]")
    print("-"*30)
    # 3,3 으로 나누기 (배열)
    for idx,a in enumerate(a_list):              # 1,2,3,4,5,6,7,8,9
        print(a,end="\t")  # end -> 옆으로 출력   
        if (idx+1)%3 == 0:       # 3으로 나누었을때 0이면
            print()
    print("-"*30)
    num = int(input("원하는 번호를 입력하세요. >> "))
    # 9번자리가 X가 되어야 함.
    for idx, a in enumerate(a_list):              # for a in a_list - > 값만 넘어옴
        if a == num:
            a_list[idx] = "X"
            break

# ----------------------------------------------
# c_list = [1,2,3]
# c_list[1] = 100   # 값이 바뀜