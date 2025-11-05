# 파일을 읽어오기  (stu_list를 항상 가져오지 않고 파일 읽어오는것)
# 파일 -> dict타입으로 변경해서 리스트에 추가
stu_list = []  
f = open("c:/down/aaa.txt","r")      # encoding="utf-8" -> write할때만 필요  
while True:
    txt = f.readline()
    if txt == "": break   # txt가 아무것도 없다면 끝
    # 문자열 -> 딕셔너리타입으로 변경해주는 명령어
   
    t_list = txt.strip().split(",")   # txt 분산시키기
    
    # 리스트를 딕셔너리로 형태 변경하기
    t_dic = {'stuno':int(t_list[0]),'name':t_list[1],'kor':int(t_list[2]),
             'eng':int(t_list[3]),'math':int(t_list[4]),
             'total':int(t_list[5]),'avg':float(t_list[6]),
             'rank':int(t_list[7]),
             }
    stu_list.append(t_dic)
print(stu_list)

### 파일 -> 리스트[딕셔너리타입] -> 파일
stu_str = ""
for i in range(len(stu_list)):   # 리스트에 있는만큼 돌리라는 뜻
    stu_str += f"{stu_list[i]['stuno']},{stu_list[i]['name']},\
{stu_list[i]['kor']},{stu_list[i]['eng']},{stu_list[i]['math']},\
{stu_list[i]['total']},{stu_list[i]['avg']},{stu_list[i]['rank']}\n"  # 문자열로 변경

# print(stu_str)
f = open("c:/down/aaa.txt","w",encoding="utf-8")
f.write(stu_str)
f.close()




