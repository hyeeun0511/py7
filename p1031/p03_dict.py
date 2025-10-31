# stu_list = [name:'홍길동',kor:100,eng:100,math:100]
# stu_list = {키:값,키:값,키:값,}    # 딕셔너리 : 쌍 2개가 하나로 묶인 자료구조  ex) 'apple:사과'처럼 의미 있는 두 값을 연결해 구성
# 키 - 변경 불가. 값 - 값만 변경할수있음

# 딕셔너리 생성
# list1 = [1,2,3]
# dic1 = {1:'a',2:'b',3:'c'}                 # 키 -> 숫자, 문자열   (키:값)
# dic2 = {"no":1,"name":"홍길동","class":3}

# print(list1)   # [1,2,3]
# print(dic1)    # {1: 'a', 2: 'b', 3: 'c'}

# # 리스트추가 - append,insert,extend
# stu = {"학번":1,"이름":"홍길동","학과":"컴퓨터공학"}
# print(stu)     # {'학번': 1, '이름': '홍길동', '학과': '컴퓨터공학'}
# # 딕셔너리 추가 - 없는 키값 입력하면 추가 됨.
# stu['연락처'] = '010-1111-1111'
# print(stu)     # {'학번': 1, '이름': '홍길동', '학과': '컴퓨터공학', '연락처': '010-1111-1111'}

# # 딕셔너리 수정
# stu['이름'] = '홍길자'
# print(stu) 
# # print(stu['성명'])      # 없는 키를 출력할때 에러발생
# stu['성명1'] = '홍'       # 딕셔너리 추가

# print(stu)
# # 딕셔너리 삭제
# del(stu['성명1'])
# print(stu)

stu_list = [                # 바깥쪽-리스트 / 안쪽-딕셔너리
    {"no":1,"name":"홍길동","kor":100}
]

# 넘버를 알고싶을때
print(stu_list[0]['no'])
print(stu_list[0]['name'])


a_dic = {"no":1,"name":"홍길동","kor":100}
# 국어점수 출력하시오.
print(a_dic['kor'])                  # 100  # 없는 키값 입력시 에러,stop             # 반복적이지 않은 부분에서 주로 사용
# 딕셔너리 get()함수
print(a_dic.get('kor'))              # 100  # 엇는 키값 입력시 None타입 형태로 출력    # 반복적인 부분에서 주로 사용하기 좋음
# a_dic / a_dic.get  -> 둘중에 어떤걸 사용해도 괜찮음

# 딕셔너리 keys()
print(a_dic.keys())            # dict_keys(['no', 'name', 'kor'])
a_list = list(a_dic.keys())    # 타입 변경   딕셔너리 타입(dic) -> 리스트 타입(list)
print(a_list)                  # ['no', 'name', 'kor']
print(a_list[1])               # name

# 딕셔너리 value()
print(a_dic.values())           # dict_values([1, '홍길동', 100])
b_list = list(a_dic.values())   # [1, '홍길동', 100]
print(b_list)

# 딕셔너리 items() - key,value
print(a_dic.items())             # dict_items([('no', 1), ('name', '홍길동'), ('kor', 100)])
c_list = list(a_dic.items())
print(c_list)                    # [('no', 1), ('name', '홍길동'), ('kor', 100)]

aa_list = [                      # 2차원 리스트  -  대괄호 2개 [[]]
    ['no',1], 
    ['name','홍길동'],
    ['kor',100]
]
# 홍길동을 출력하시오.
print(aa_list[1][1])             # 홍길동


# 키 존재 확인
stu_dic = {"no":1,"name":"홍길동","kor":100}
if 'eng' in stu_dic:
    print("키가 존재합니다.")
else:
    print('키가 존재하지 않습니다.')                 # 결과 -> 리스트에 영어(eng)가 없으므로 '키가 존재하지 않습니다.'

stu_dic = {"no":1,"name":"홍길동","kor":100}
if 'kor' in stu_dic:
    print("키가 존재합니다.")
else:
    print('키가 존재하지 않습니다.')                 # 결과 -> 리스트에 국어(kor)가 있으므로 '키가 존재합니다.'