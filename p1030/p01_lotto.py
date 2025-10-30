#  로또 맞추기 프로그램을 구현하시오.

# 1. 변수선언
# my_list,an_list(answer_list 정답리스트),count,lotto
import random
my_list = []  # 내가 입력한 번호
c_list = []   # 정답 번호
count = 0    # 맞춘 개수
lotto = 0


# 2. 6개 번호 생성
# 6개를 랜덤으로 번호 생성
lotto = random.sample(range(1,46),6)   # 1~45 숫자중 6개 랜덤
print(lotto)    # 로또번호 확인 가능
# 순차적으로 정렬
lotto.sort()   # 작은수부터 오름차순


# 3. 6개 번호 입력
i = 0
while i<6:                # 1~45   46부터는 안됨
    num = input("{}번째 로또번호를 입력하세요.".format(i+1))     # 번호 입력받음
    if not num.isdigit():     # 얜 숫자가 아니냐고 물어보는것.  # isdigit : 문자열이 숫자인지 확인해주는 함수
        print("숫자가 아닙니다. 숫자만 입력가능합니다.")
        continue
        
    num = int(num)
    if 1<= num <= 45:
        my_list.append(num)                     # 입력받은 번호 - my_list에 추가
        i = i + 1
    else:
        print("1~45번까지 번호 또는 숫자만 입력하셔야 합니다.")
my_list.sort()                              # 내가 입력한 번호를오름차순으로 정렬

# for i in range(6):                 # 1~45   46부터는 안됨                               for문 - 실수가 몇번 일어나도 계속 진행됨. 실패해도 count는 증가  //  while문 - 실수가 일어나면 에러남. 실패하면 count 증가X
#     num = int(input("{}번째 로또번호를 입력하세요.".format(i+1)))     # 번호 입력받음
#     if 1<= num <= 45:
#         my_list.append(num)                     # 입력받은 번호 - my_list에 추가
#     else:
#         print("1~45번까지 번호를 입력하셔야 합니다.")
# my_list.sort()                              # 내가 입력한 번호를오름차순으로 정렬

print(lotto)
print(my_list)

# 4. 번호확인            # 내가 입력한 번호 - 정답 번호 확인 for문
for lo in lotto:                # [1,3,9,10,15,45]       (각각들고와서 각각 비교하기때문에 for문 두번 돌아야함)
    for my in my_list:          # [5,9,11,12,36,40]
        if lo == my: #
            c_list.append(i)
            count = count + 1
            break
        
for my in my_list:                # [5,9,11,12,36,40]       (for문 한번 돌아야함)
    #if lo == my: #
    if my in lotto:               # 5  [1,3,9,10,15,45]
        c_list.append(my)
        count = count + 1

# for i in lotto:         # 정답 번호                                헷갈리면=> i->lo(lotto)
#     for j in my_list:   # 내가 입력한 번호                                    j->my
#         if i == j:
#          count = count + 1   # 맞으면 맞춘 개수+1
#          c_list.append(i)   # 작성한 정답 번호 저장됨
#     break                    # for i in lotto로


# 5. 결과출력
print("[ 당첨 결과 ]")
print("-"*50)
print("로또번호 : ",lotto)
print("입력번호 : ",my_list)
print("")


print(lotto)            # 로또 번호 출력
print(my_list)          # 작성한 번호 출력   # 비교
print("맞춘 번호 : ",c_list)           # 맞춘 번호
print("맞춘 개수 : ",count)            # 맞춘 개수
print("당첨 번호 : ",count)
print("당첨 개수 : ",count)


