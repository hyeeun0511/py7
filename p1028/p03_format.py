# year = 2025
# month = 10
# day = 28
# # 2025년 10월
# print("%d년 %d월 %d일" % (year,month,day))
# # print("%d-%d-%d" % (year,month,day))    -> 가능
# # format() 함수
# date1 = "{}년 {}월 {}일".format(year,month,day)
# print(date1)
# #  date1 = "{%d}년 {%d}월 {%d}일".format(year,month,day)    => %d 생략 가능


# format - 저장해서 파일로 보내기위해

# a = 100000000
# a_format = "{}".format(a)
# a_format1 = "{:10d}".format(a)
# a_format2 = "{:010,d}".format(a)
# print(a_format)
# print(a_format1)
# print(a_format2)

# b = 25.2345678
# print("{:.2f}".format(b))   # 외우기  # 많이 사용
# print("%.2f" % b)

# b_format = "{}".format(b)
# b_format1 = "{:.2f}".format(b)
# print(b_format)
# print(b_format1)


# list타입 format함수 사용
stus = ['홍길동',100,90,80]
print("이름 : {},국어 : {},영어 : {},수학 : {}".format\
    (stus[0],stus[1],stus[2],stus[3]))
# *stus -> 전개연산자 stus[0],stus[1],stus[2],stus[3]
print("이름:{},국어:{},영어:{},수학{}".format(*stus))


### 
bank = [1,'홍길동',100000]
# 1번 홍길동 100,000원
print("{}번 {} {:,d}원".format(*bank))

name = "유관순"
rank = 3
result = 98.234567
## 이름 : 유관순, 단계 : 3, 성공률 : 98.23%
print("이름 : {}, 단계 : {}, 성공률 : {:.2f}%".format(name,rank,result))
## f
print(f"이름 : {name}, 단계 : {rank}, 성공률 : {result:.2f}%")



## % print
# a = 10
# print("%5d" % a)

# b = 10.2345678
# print("%f" % b)
# print("%.2f" % b)
# print("%7.2f" % b)
# print("%07.2f" % b)

