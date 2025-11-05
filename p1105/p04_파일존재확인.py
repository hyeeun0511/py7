import os
# os 안에 해당 파일의 이름. 수정한 날짜. 유형. 크기 불러올수있음

#
fname = input("검색하려는 파일이름을 입력하세요.")
# fname = file name

# 파일이 존재하는지 확인
if os.path.exists("c:/down/"+fname):
    print("존재")  # aaa라는 파일이 존재하면 - "존재"     # 존재 - ccc.txt(메모장)라는 파일이 있기 때문
else:
    print("없음")

# 현재위치에 존재하는 모든 파일을 출력 - os.listdir - list
# print(os.listdir("c:/down/"))


