# 산술연산자
# + : 더하기, - : 빼기, * : 곱하기, / : 나누기
# // : 몫, % : 나머지, ** : 제곱
# print(10+20)
# print(10-20)
# print(10*20)
# print(10/20)
# print(10/3)  # 3.333333
# print(10//3) # 3
# print(10%3)  # 1 나머지
# print(10**3) # 10*10*10 = 1000

# 두 수를 입력받아 위의 연산을 축력하시오.
# +, -, *, /, //, %, **
# num1 = int(input("첫번째 숫자를 입력하세요."))
# num2 = int(input("두번째 숫자를 입력하세요."))
# print("더한 값 :",(num1+num2))
# print("뺀 값 :",(num1-num2))
# print("곱한 값:",(num1*num2))
# print("나눈 값 :",(num1/num2))
# print("몫 :",(num1//num2))
# print("나머지 :",(num1%num2))
# print("제곱 :",(num1**num2))

### 780원 동전으로 교환을 하려고 해요.
### 500, 100, 50, 10원짜리 동전 몇개로 교환할까요?
# 값/500-1(몫) 나머지/100-2(몫) 나머지/50-1(몫) 나머지/10-3(몫)

# coin = 123456780
# money1 = coin//500       # 몫
# money2 = coin%500       # 나머지
# money3 = money2//100    # 몫
# money4 = money2%100    # 나머지
# money5 = money4//50     # 몫
# money6 = money4%50     # 나머지
# money7 = money6//10     # 몫
# money8 = money6%10     # 나머지

# print("500원 동전 : %d 개" % money1)
# print("100원 동전 : %d 개" % money3)
# print("50원 동전 : %d 개" % money5)
# print("10원 동전 : %d 개" % money7)


coin = 1597000
# 50000원, 10000원, 5000원, 1000원 몇장이 필요한지
coin1 = coin//50000  # 몫
coin2 = coin%50000
coin3 = coin2//10000  # 몫
coin4 = coin2%10000
coin5 = coin4//5000   # 몫
coin6 = coin4%5000
coin7 = coin6//1000   # 몫
coin8 = coin6%1000    # 동전으로 교환

print("50000원 지폐 : %d 장" % coin1)
print("10000원 지폐 : %d 장" % coin3)
print("5000원 지폐 : %d 장" % coin5)
print("1000원 지폐 : %d 장" % coin7)
print("거스름돈 : %d 원" % coin8)