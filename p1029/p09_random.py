import random
my_list = []
count = 0

# 1,45까지 6개의 랜덤숫자를 출력하시오.
# 중복은 안됨
# print(random.sample(range(1,46),6))
lotto = random.sample(range(1,46),6)
lotto.sort()
print(lotto)
# 6개 숫자를 입력받아 출력하시오.
for i in range(6):
    num = int(input("숫자를 입력하세요."))
    my_list.append(num)
my_list.sort()    
print("[ 결과화면 ]")
print("-"*50)
print(lotto)
print(my_list)

# lotto =  [ 5,9,24,36,44,45]
# my_list = [ 1,2,7,15,24,30,36]
for i in lotto:
    for j in my_list:
        if i == j:
            count = count + 1
            break # 가장가까운 for만 중지 - for i in lotto:로 감

print("정답개수 :",count)
            