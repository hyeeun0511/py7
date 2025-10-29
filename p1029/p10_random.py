## 로또번호 맞추기 프로그램
## 1. 변수선언, 로또번호 생성
## 2. 숫자입력
## 3. 당첨번호 확인
## 4. 결과화면 출력
## 5. 당첨금 출력


# 1. 변수선언, 로또번호 생성
import random
my_list = []   # 입력한 번호
count = 0      # 맞춘개수
c_list = []    # 정답 리스트

lotto = random.sample(range(1,46),6)

# 2. 숫자입력  (로또번호 6개를 입력받아야 함)
for i in range(6):
    num = int(input("숫자를 입력하세요."))
    my_list.append(num)  # append : 리스트에 추가
my_list.sort()   # sort : 리스트 순차정렬
print(my_list)


# 3. 당첨번호 확인
for i in lotto: # 23,1,9,45,20,15 # 정답번호
    for j in my_list: # 내가 작성한 번호
        if i == j: # 정답번호(i)와 작성한 번호(j)비교
            count = count + 1 # 정답번호가 같으면 +1, 즉 count 1개 증가
            c_list.append(i) # append : 리스트에 추가 # 정답 번호를 리스트에 추가
            break # 맞추면 중지 -> for i in lotto로 감


# 4. 결과화면 출력
print("[ 결과화면 ]")
print("-"*50)
print(lotto)
print(my_list)


# 5. 당첨금 출력
