# 로또 맞추기 프로그램
# 로또 1개를 자동번호 추출로 입력받아,
# 몇개가 맞는지 출력하시오.

import random
# 로또 번호
lotto = random.sample(range(1,46),6)
counts = []

# 자동추출 6개 my번호
my_lottos = []
# count = 0
# c_list = [] # 맞춘 리스트
print('[ 로또 번호 ]')
for i in range(5):
    my_lottos.append(random.sample(range(1,46),6))
# print(my_lottos)
# 입력한 my 숫자 번호
print('[ 나의 랜덤 로또 번호 ]')
for my_lotto in my_lottos:
    print(my_lotto)
print("-"*50)

# 번호비교함수
def cal():
    print(lotto,my_lottos)
    for my_lotto in my_lottos:  # 6개묶음 로또번호
        count = 0
        for i in my_lotto:      # 1개 묶음 로또번호
            if i in lotto:      # 1개 번호가 로또번호에 있는지 확인
                count += 1
        counts.append(count)            


# 맞는 개수
print("-"*50)
cal()
print("[ 로또번호 맞춘 개수 ]")
print(counts)


# -----------직접 해본 과정----------#  --에러남
# lotto = random.sample(range(1,46),6)
# lotto.sort()
# print(lotto)

# my_list = []

# for i in range(6):
#     num = int(random.sample(range(1,46),6))  # 자동으로 6개 숫자 추출
#     my_list.append(num)  # 내가 뽑은 번호
# my_list.sort()
# print(my_list)
# ---------------------------------#