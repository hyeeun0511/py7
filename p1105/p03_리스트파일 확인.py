a_list = []
# bbb.txt 에서 3개 출력하시오.
# 3개를 a_list 리스트 추가(append)하시오.
# [['안녕','hello'],['사랑','love'],['감사','thank']]
# 1. 출력 
f = open("c:/down/bbb.txt","r",encoding="utf8")
while True:
    txt = f.readline()
    if txt == "":break
    a_list.append(txt.strip().split(","))  # 리스트추가  
    # print(txt.strip())  # 공백제거
f.close()

print(a_list)    # [['안녕', 'hello'], ['사랑', 'love'], ['감사', 'thank']]


    



# print("안녕하세요. 홍길동입니다.")    
# print('안녕하세요. "홍길동"입니다.')
# # "안녕하세요. "홍길동"입니다. - 불가능
# print("안녕하세요. \"홍길동\" 입니다.")   # 안녕하세요. "홍길동" 입니다.   # \: 뒤에 오는걸 문자로 인식하는 기호  # \"홍길동\"-> "를 문자로 인식

# f = open("c:/down/aaa.txt","r",encoding="utf8") 
# readline() : 1줄씩 가져오기
# while True:
#     txt = f.readline()  # 안녕하세요.  # read()-한 글자씩 읽어옴(속도느림),readline()-한줄씩 읽어옴,readlines()-전체를 다 읽어옴
#     if txt == "": break
#     print(txt,end="")   # print완료후 줄바꿈(enter)을 해줌. # end="" : enter(줄바꿈)을 안함
# f.close()  # 파일을 지우기위해서 # 나중에 쓰기모드를 하게되면 파일 통로가 열려있어서 파일 삭제가 불가능 해지기때문에



### 홍길동 출력(txt파일)  # readline(): 1줄씩 가져오기
# f = open("c:/down/aaa.txt","r",encoding="utf8")
# txt = f.readline()
# # while True:
# #     txt = f.readline()
# #     txt = "1,홍길동,100,100,100,300,100.00,0"  # 구분자 : , -> 구분자를 통해 파일을 나눌수있음
# #     if txt == "": break
# #     print(txt.strip())  # 공백제거
# #     # print(txt,end="")   # 줄바꿈 하지말고 엔터키를 적용해라
# #     # print(txt)
# print(txt.strip())   # 문자열타입 - strip : 공백제거    # 1,홍길동,100,100,100,300,100.00,0  # ,(컴마)로 구분하는 문자열 타입 - 메모장에서 오면 문자열로 나옴
# print(txt.strip().split(","))   # 리스트타입 - strip:공백제거,split():분리
# print(txt.strip().split(",")[5])   # 합계  # 문자열타입
# f.close()