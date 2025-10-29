import random  # 선언  # random 클래스에 있는 것을 가져와서 쓰겠다.
print(random.random())   # 0.0000000 <= x < 1.0000000          # random 클래스안에 있는 random이라는 함수를 가져와서 쓰겠다.라는 뜻
print(random.randrange(1,11))     # 1~10 사이의 숫자를 랜덤으로 가져옴.  # 밑에것과 같음.
print(random.randint(1,11))       # 1~10 사이의 숫자를 랜덤으로 가져옴.  # 위에것과 같음.
# 해당리스트에서 2개를 랜덤으로 가져옴. - 중복이 안됨. # 무조건 다른 숫자갖고옴
print(random.sample([1,2,3,4,5],4))    # 무조건 다른 숫자 4개 가져옴
# 해당리스트에서 2개를 랜덤으로 가져옴. - 중복이 가능
print(random.choices([1,2,3,4,5],k=4))    # k     # k로 정해져있음    
# 해당리스트 순서를 랜덤으로 조정
a_list = [1,2,3,4,5]
random.shuffle(a_list)
print(a_list)