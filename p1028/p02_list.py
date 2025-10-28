# list = 순서가 있으면서, 여러개의 값을 저장하는 공간
a_list = [1,2,3,4,5,6,7,8,9]
print(a_list[::2])   # 홀수만 출력하고 싶을때
print(a_list[1::2])  # 짝수만 출력하고 싶을때


a_list[0] = 100
print(a_list)
# 입력한 값이 홀수, 짝수인지 출력하시오.
# if num%2==0 :
a_list = [0,5,3,1,2,4,1,5,6]              # 규칙없는 나열에서 짝수만 출력  - 한개씩 빼서 비교
# print("" % (a_list[0],a_))
# 0번째 : 0, 2번째 : 3
print("0번주소 : %d, 2번주소 : %d" % (a_list[0],a_list[2]))




# str1 = "안녕하세요"
# print(str1[1:4])
# print(str1[::-1])
# print(a_list[2:5:2])

