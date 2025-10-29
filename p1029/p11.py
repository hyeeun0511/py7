import random

# a_list = [9,1,2,5,6,8,3,4,7]
# 3 * 3 형태로 출력
# 9 1 2
# 5 6 8
# 3 4 7

# for i,val in enumerate(a_list):    # i:번호  val:값   # enumerate : 번호를 물어보는것
#     print(val,end="\t")
#     if (i+1)%3 == 0:   # 0번부터가 아닌 그 다음부터 시작
#         print()

a_list = list(range(1,17))
random.shuffle(a_list)
print(a_list)
### 4 * 4 리스트 형태로 출력하시오.  # 1차원 -> for문 한번
for i,val in enumerate(a_list):
    print(val,end="\t")
    if (i+1)%4 == 0:
        print()




# # [3 * 3 리스트 형태]
# a_list = [
#     [1,2,3],  [4,5,6], [7,8,9]
# ]


# # print(a_list[0])   # -> 1 # [1,2,3]이 한묶음이라

# # b_list = [1,2,3]
# # print(b_list[0])


# # [ [1,2,3], [4,5,6], [7,8,9]]
# # 3 * 3 형태로 출력하시오.
# for aa in a_list: # [1,2,3]  [4,5,6]  [7,8,9]  # 임의로 aa라 해놓은것 -> bb,bb111... 라고 해놔도 됨
#     for a in aa: # [1,2,3]
#         print(a,end="\t")
#     print()





# # [ 3 * 3 리스트 형태]
# # a_list = list(range(1,10))
# # b_list = []
# # [
# #     [1,2,3],
# #     [4,5,6],
# #     [7,8,9]
# # ]
# # 1 2 3
# # 4 5 6
# # 7 8 9
# # print(a_list)
# # for i in a_list: # 9번 돌리라는 의미
# #     print(i,end="\t") # 옆쪽으로 띄어져서 출력
# #     # print(i,end=" ") # 옆쪽으로 출력
# #     if i%3 == 0:  #3의 배수로 출력
# #         print() 
        
        
# # 4*4 리스트형태로 출력하시오.
# # [ 4 * 4 리스트 형태 ]
# a_list = list(range(1,17))  # 1~16
# for i in a_list:
#     print(i,end="\t")       # 띄어서 옆으로(end=" ") 나열
#     if i%4 == 0:            
#         print()
        
        
# # [ 5*5 리스트 형태 ]
# a_list = list(range(1,26))
# for i in a_list:
#     print(i,end="\t")
#     if i%5 == 0:
#         print()


# 1 2 3 4
# 5 6 7 8
# 9 10 11 12
# 13 14 15 16    #으로 출력하라는 의미



# ## list를 자동으로 만드는 방법

# a_list = [1,2,3,4,5,6,7,8,9]
# print(a_list)
# b_list = list(range(1,10))  # 외우기
# print(b_list)               # 외우기
# c_list = [i for i in range(1,10)]
# print(c_list)

# d_list = ['0','0','0','0','0','0','0','0','0',]
# print(d_list)
# e_list = list('0' * 9)  # 외우기
# print(e_list)           # 외우기
# f_list = ['0' for i in range(9)]    # i 대신 _ 넣어도 상관없음
# print(f_list)