# 이름,국어,영어,수학점수를 입력받아
# 홍길동,국어,영어,수학,합계,평균
a_list = ['홍길동',100,90,80,270,90.0000000]
# 이름:홍길동 국어:100
print("이름:{},국어:{},영어:{},수학:{},합계:{},평균:{:.2f}".format\
    (a_list[0],a_list[1],a_list[2],a_list[3],a_list[4],a_list[5]))
print("이름:{},국어:{},영어:{},수학:{},합계:{},평균:{:.2f}".format\
    (*a_list))

a = 10
b = 20
print("1번째값 : {},2번째값 :{}".format(b,a))
print(f"1번째값 : {b},2번째값 :{a}")  # f함수  # 뒤에있는 포멧함수를 앞에 직접 입력함  # 위에 값과 같음



name = input("이름을 입력하세요.")




# 3개의 값을 입력받아, 숫자를 모두 합친 금액을 출력하시오.
# 1000원 이상 입력하세요.
# 총금액 : 1,000,000원

# n1 = int(input("금액을 입력하세요."))
# n2 = int(input("금액을 입력하세요."))
# n3 = int(input("금액을 입력하세요."))
# total = n1+n2+n3
# print("총 금액 : {:,d} 원".format(total))
# print("1번금액 : {:,d} 원\n2번금액 : {:,d}원\n3번금액 : {:,d}원\n \
#     총금액 : {:,d}원".\
#     format(n1,n2,total))



# total_format = "{} 원 {} 원 {} 원".format(n1,n2,n3)
# prnit(total_format)


# year = 2025
# month = 10
# day = 28
# print("%d 년 %d 월 %d 일" % (year,month,day))
# day_format = "{} 년 {:03d} 월 {} 일".format(year,month,day)
# print(day_format)