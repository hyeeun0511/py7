# stu_dic = {}

# # "no":1,"name":"홍길동","kor":100 딕셔너리 추가해서
# # 키 : 값 으로 모두 출력하시오.
# stu_dic['no'] = 1              # 추가하는 부분
# stu_dic['name'] = '홍길동'      # 내용
# stu_dic['kor'] = 100

# print(stu_dic)

# # k = key(키) / v = value(값)
# # 방법 1
# for k,v in stu_dic.items():    # item() -> ('no',1)의 형태로 분리됨  # ('no',1)
#     print("{}:{}".format(k,v))
    
# # 방법 2    
# for k in stu_dic.keys():
#     print("{}.{}".format(k,stu_dic[k]))     # 'no',stu_dic['no']
    
# # value만 찍고싶을때 (값만 출력하고싶을 경우)
# for v in stu_dic.values():
#     print("값 : {}.".format(v))


# #### 혼자해봄
# # stu_dic = {"no":1,"name":"홍길동","kor":100}
# # print(stu_dic.values())
# # a_list = list(stu_dic.values())
# # print(a_list)                         # [1, '홍길동', 100]


stu_list = [                
    {"no":1,"name":"홍길동","kor":100},
    {"no":2,"name":"유관순","kor":80},
    {"no":3,"name":"이순신","kor":90}
]

# 3번째에 있는 kor -> 50
stu_list[2]['kor']=50
print(stu_list)

# kor이 아닌 숫자로 2를 넣게되면 2는 없는 값이라 추가가됨.
# stu_list[2][2]=50
# print(stu_list)

stus = {"no":3,"name":"이순신","kor":90}
# kor -> 50으로 변경하세요.
stus['kor'] = 50
print(stus)

a_list = [3,'이순신',90]
#90 -> 50점 변경하세요.
a_list[2] = 50
print(a_list)