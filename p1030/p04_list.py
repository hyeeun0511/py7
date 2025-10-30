# a_list = [1,2,3,4,5]
# b_list = list(range(1,6))
# c_list = [i for i in  range(1,6)]  # 리스트 내포.
# print(a_list)
# print(b_list)
# print(c_list)

# list에 추가하는 방법 - append, insert, extend
# list에서 지우는 방법 - pop, del, remove, clear 
# list에서 수정하는 법 - a_list[index] = 값
# index : 해당위치값 리턴
aa_list = [10,5,15,7,9]
# print(aa_list.index(10))  # aa_list에 있으면 알려줌, 없으면 에러남 ex) index(100)-> 100은 aa_list에 없음 -> 에러

# # 비교
# print(aa_list)                                        
# num = int(input("원하는 번호를 입력하세요.>> "))
# for idx,aa in enumerate(aa_list):
#     if aa == num:             # aa_list안에있는 aa와 num을 비교하는것
#         aa_list[idx] = "X"
# print(aa_list)

# 2. 비교
# print(aa_list)  #[10,5,15,7,9]
# num = int(input("원하는 번호를 입력하세요.>> "))
# if num in aa_list:
#     aa_list[aa_list.index(num)] = "X"
    
# print(aa_list)



# 5* 5의 2차원 형태 리스트를 생성
# 좌표만들기
# if num in aa_list:
#     aa_list[aa_list.index(num)] = "X"  .사용하여.




####---------------------------------------------------내가 해봄-----#
# import random
# print("[좌표맞추기 게임]")
# print("-"*50)
# aa_list = list(range(1,26))     # 리스트 생성
# random.shuffle(aa_list)
# # print(aa_list)      # [10,5,15,7,9]   # print(aa_list)-> 파이썬이 한줄로 출력함  # 5*5형태로 출력하려면 for문 사용
# for i in range(5):                   # 5행
#     for j in range(5):               # 5열
#         print(f"{aa_list[i*5 + j]:>3}", end=" ")
#     print()                          

# num = int(input("원하는 번호를 입력하세요.>> "))

# if num in aa_list:
#     aa_list[aa_list.index(num)] = "X"   # 입력값 -> X

# # 결과값 -> print(aa_list)로 출력시 => 한줄로 출력됨
# for i in range(5):                   # 5행
#     for j in range(5):               # 5열
#         print(f"{aa_list[i*5 + j]:>3}", end=" ")
#     print()                          
    

