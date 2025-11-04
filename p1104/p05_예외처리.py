# 예외처리 - 오류(에러)가 나도 프로그램을 종료하지 않고 계속 실행시키는 것

# 오류 - 구문오류(실행하기 전에 에러남),런타임오류(실행해야 알수있음)
# a=10
# print(a)
# # prin(a)  # 철자오류 -> 실행 안됨  # 구문오류 - 오타
# # prin(a)  # 실행하기 전에 에러가 남.

# a_list = [1,2,3]
# print(a_list[0])
# # 예외처리 - 외부연결 : 파일입출력,파일읽기,쓰기,프린터기 연결,db연결 (외부로 인해 에러가 났을때)        # 웬만하면 예외처리 안하는게 좋음
# try:    # 에러 날것같은 부분에 try안에 넣어줌 -> 프로그램 잘 돌아감
#     print(a_list[100])  # 에러난지 실행을 해야 알수 있음 - 런타임오류   # 이곳에서 에러가 나면 except부분으로 넘어감 -> "예외가 발생했습니다."
# # except Exception as e:
# #     print("예외가 발생했습니다.")
# #     print(e)      # list index out of range  ->  어떤 에러가 있는지 알려줌
# except Exception as e: print("에러 : ",e) 


# print("프로그램을 종료합니다.")  # 위에 try를 사용한 예외처리를 하지않을 시, 출력안됨 -> 위에서 에러가 나기때문


print(1)
print(2)
try:
    print(3)
    print(4)
    # 에러
    # raise SyntaxError  # 강제로 에러발생하는 명령어  # try 외부에 있을시 그 전까지만 되고 바로 에러 -> except로 넘어감
    print(5) 
except:         # 예외가 발생할때만 실행
    print(6)    
finally:        # 에러가 발생하지 않아도, 발생해도 무조건 실행
    print(7)
print(8)

# 에러
# 1234678
# 에러X
# 1234578
