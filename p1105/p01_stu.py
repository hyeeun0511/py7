# stu_list = [ 
#     [10101,'홍길동',80,80,80,240,80.00,0],
#     [10102,'유관순',90,90,90,280,90.00,0],
#     [10103,'이순신',100,100,100,300,100.00,0]
# ]

# print(stu_list[1][1])   # [주소][주소]   # 유관순

stu_list = [
    {'stuno':10101,'name':'홍길동','kor':80,'eng':80,'math':80,\
        'total':240,'avg':80.00,'rank':0},
    {'stuno':10102,'name':'유관순','kor':90,'eng':90,'math':90,\
        'total':270,'avg':90.00,'rank':0},
    {'stuno':10103,'name':'이순신','kor':100,'eng':100,'math':100,\
        'total':300,'avg':100.00,'rank':0}
]

#### 퀴즈 ####--------------------
## 문자열로 빼와서 저장하는 방법
# dict타입 -> 문자열로 변환
stu_str = ""
for i in range(len(stu_list)):
    stu_str += f"{stu_list[i]['stuno']},{stu_list[i]['name']},\
{stu_list[i]['kor']},{stu_list[i]['eng']},{stu_list[i]['math']},\
{stu_list[i]['total']},{stu_list[i]['avg']},{stu_list[i]['rank']}\n"
print(stu_str)       
# += 추가시키는 것
# 파일쓰기
f = open("c:/down/aaa.txt","w")
f.write(stu_str)
f.close()

# 파일저장

# 파일 다시 읽어와서, dict타입으로 변경해서
# 출력하시오.





#----------------------------------


# print(stu_list[1]['name'])   # [주소][키워드]   # 유관순

# for stu in stu_list:
#     print(f"{stu['stuno']}\t{stu['name']}\t{stu['kor']}\
# \t{stu['eng']}\t{stu['math']}\t{stu['total']}\
# \t{stu['avg']}\t{stu['rank']}\t")