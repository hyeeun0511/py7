# 삼중따옴표는 있는 그대로 출력
print("""abcdefghijklma
    sdf
    jkl;n
    ajksl
    alksjd
    aksl""")


# 문자열
# str = "안녕"
# str = '안녕'
# print(str1)
# print(str1,str2)
# print(str1,"--",str2)           # 문자열출력
# %출력 자리수지정, 빈공백에 0을 표시 %05d, 소수점제한 %.2f
# %s:문자열, %d:정수, %f:실수
# print("%s -- %s" % (str1,str2)) # 문자열출력

print("안녕"*10) # 문자열 반복연산
print("-"*50)
print("이름\t국어\t영어\t수학\t합계\t평균") #\n:줄바꿈

# 문자열 선택  # 한글자씩 떼어올수 있음
name = "안녕하세요"   # 주소값 - 안:0 녕:1 하:2 세:3 요:4
print(name[0])
print(name[-5])
print(name[1])
print(name[2])
print(name[3])
print(name[4])

# 문자슬라이싱 - 안녕하세요.
# print(name[앞:뒤])
print(name[0:4])  # 안녕하세 # 0부터 4앞까지 출력 (0-3)
print(name[0:2])  # 안녕 # 2부터 4앞까지 출력 (2-3)
print(name[2:4])  # 하세
print(name[2:])   # 하세요 # 뒤자리 입력하지 않으면 마지막까지 출력
print(name[:3])   #  앞자리 잎력하지 않으면 처음부터 출력 

# 문자 길이
print(len(name)) # 문자열의 길이 출력

# 슬라이싱 - 스탭 (안.하.세 - 하나씩 띄어서 출력) (안) 녕 (하) 세 (요)
print(name[::2]) # 모든 문자열 2칸씩 띄워 출력
print(name[::-1]) # 반대로 출력
print(name[::3])                         

# 880101-2111111 주민번호
# 1 - 남자, 2 - 여자, 3 - 남자, 4 - 여자
# jumin = "880101-2111311"
        #01234567
jumin = input("주민번호를 입력하세요")
# 2만 출력하시오.
print(jumin[7])

# 홀수:남자 짝수:여자
if(int(jumin[7])%2==0):
    print("여자입니다.")
else:
    print("남자입니다.")
    