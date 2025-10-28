# # for 변수 in 범위:
# # for i in [50,3,26,5,9]:
# #     print(i)
# # for i in range(5): # [0,1,2,3,4]
# #     print(i,end=" ")  # ""공백없음 / " "한칸공백  # 옆쪽으로 출력함

# # 1~100까지 합을 구하시오.

# # for i in range(1,101):
# #     sum = 0              # 에러
# sum = 0  
# for i in range(1,101):
#     sum = sum + i
# print("합계 : ",sum)

# # 10을 넘는 위치는 얼마를 더할때 일까요?
# # 1+2+3+4+5+6+7+8+9+10+11+12+13+14
# sum = 0
# for i in range(1,101):
#     if sum>100:
#         break
#     sum = sum + i
#     print(i,sum)
# print(f"{i-1} 번째 : {sum-1}")
# # print(f"{i-1-1} 번째 : {sum-(i-1)}")  # 그 전 숫자


# 1*2*3*4*...*10  결과값 출력하시오.
# result = 1  # 변수
# 1부터 곱해야 함
result = 1
for i in range(1,11):
    result = result * i
    print(i,result)
    if result>100:
        break
print(f"{i}번째 : {result}")