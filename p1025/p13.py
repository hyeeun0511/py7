#990101-1111111
#070101-3111111
# 1 -> 남자 , 2 -> 여자
# 주민번호를 입력받아, 남자인지, 여자인지 출력하시오.
jumin = input("주민번호를 입력하시오.")
num = int(jumin[7])
if num==1:
    print("남자입니다.")
else:
    print("여자입니다.")
    
# 10월 생 이벤트 대상자입니다.
import datetime
month = datetime.datetime.now()
month = int(jumin[2:4])
if month== 1:
    print("이벤트 대상자입니다.")
else:
    print("이벤트 대상자가 아닙니다.")
    
    
...