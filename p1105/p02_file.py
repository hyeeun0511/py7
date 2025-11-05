import os   

### 파일복사 - 문자읽기:r, 문자쓰기:w / 파일읽기:rb, 파일쓰기:wb
f = open("c:/down/nct1.jpg","rb")   # 파일읽기
f2 = open("c:/aaa/nct1.jpg","wb")   # 파일쓰기

while True:
    nctfile = f.read(1)   # read() : 파일읽기, # readline(),readline() : 문자읽기  # 1byte씩 읽어 오라는 뜻
    if not nctfile: break   # nct 파일에 아무것도 없으면 중지
    f2.write(nctfile)
    
f.close()
f2.close()
print("복사완료!!")


### 파일입출력

## 방법1

# # with open() 파일입출력
# with open("c:/down/bbb.txt","r",encoding="utf-8") as f:
#     while True:
#         txt = f.readline()
#         if txt == "": break
#         print(txt.strip())
# # f.close()  # 자동으로 입력됨. -> f.close() 안해도 됨.


## 방법2

# f = open("c:/down/aaa.txt","r",encoding="utf-8")
# while True:
#     txt = f.readline()
#     if txt == "": break
#     print(txt.strip())     # 1,홍길동,100,100,100,300,100.00,0
# f.close()


#------------------------------------------
# # a : 추가 모드 _ (안에 있는 것 그대로 두고) 마지막에 쓰기
# f = open("c:/down/ccc.txt","a")   # a:모드
# for i in range(5):
#     f.write(f"안녕하세요. {i} \n")
    
# f.close()

# print('완료!!')






#-----------------------------------------------------------------------------
# # w : 쓰기 모드 - 안에 있는 모든것 지우고 쓰기
# # a : 추가 모드 _ (안에 있는 것 그대로 두고) 마지막에 쓰기
# # 1. 파일 열기
# # f = open("c:/down/ccc.txt","w")   # 파일이 없으면 w(읽기 모드)모드는 파일을 생성
# f = open("c:/down/ccc.txt","a")   # a:모든 # 파일이 있을때 a모드
# stu_data = ""
# for i in range(1):   # 1번 반복
#     txt = input("글자를 입력하세요. >> \n")  
#     stu_data += txt+"\n"
# f.write(stu_data)
# f.close()
# print("완료!")

#--------------------------------------------------------------------------
# 1. 통로(stream) : 파일열기
# r : 읽기모드, w : 쓰기모드, a : 추가모드
# r : 읽기모드
# f = open("c:/down/aaa.txt","r",encoding="utf8")      # studata.txt 파일 하나를 읽어오겠다는 의미   # 한글일때는 encoding="utf8"  # 메모장에 aaa.txt파일로 저장해놓고 진행
#         # c:/파일위치/파일이름    # c:\\down\\aaa.txt 도 가능   # \\ 혹은 /
# while True:   
    # txt = f.read()
    # if txt == "":break
    # print(txt,end="")

# readline() : 1줄씩 가져오기
# while True:
#     txt = f.readline()  # 안녕하세요.  # read()-한 글자씩 읽어옴(속도느림),readline()-한줄씩 읽어옴,readlines()-전체를 다 읽어옴
#     if txt == "": break
#     print(txt,end="")   # print완료후 줄바꿈(enter)을 해줌. # end="" : enter(줄바꿈)을 안함

# realines() : 전체 가져오기
# txt_list = f.readlines()   # 1줄씩 리스트에 담어서 가져옴
# print(txt)      # ['안녕하세요.\n', '반갑습니다.\n', '다음에 봐요\n', 'hello\n', 'see you']  # \n이 모두 포함된 상태로 출력됨
# for txt in txt_list:
#     print(txt,end="")

# f.close()  # 파일을 지우기위해서 # 나중에 쓰기모드를 하게되면 파일 통로가 열려있어서 파일 삭제가 불가능 해지기때문에