# 딕셔너리 - {키:값}
stu_dic = {"no":1,"name":"홍길동","kor":100}

# dict추가    # 딕셔너리
stu_dic['eng'] = 90   # 없는 값을 넣게되면 -> 추가
# dict수정
stu_dic['kor'] = 10   # 있는것에 값을 넣게되면 -> 수정
# dict삭제
# del stu_dic['name']

# key출력
print(stu_dic.keys())          # dict_keys(['no', 'kor', 'eng'])
print(list(stu_dic.keys()))    # ['no', 'kor', 'eng']
for k in stu_dic.keys():
    # print(stu_dic[k])          # value값이 출력됨
    print("{} : {}".format(k,stu_dic[k]))          # key,value값이 출력됨
    
# value() 출력
print(stu_dic.values())        # dict_values([1, 10, 90])
print(list(stu_dic.values()))  # [1, 10, 90]
for i,v in enumerate(stu_dic.values()):
    print("{} , {}".format(i,v))

# items() 출력 - k,v
print(stu_dic.items())  # 튜플형태로 출력
print(list(stu_dic.items()))
for k,v in stu_dic.items():
    print("{} : {}".format(k,v))
    
# 딕셔너리 출력 방법
print(stu_dic['no'])  # no : 넘버  
print(stu_dic['name'])
print(stu_dic['kor'])
# print(stu_dic['math'])  # 없는 key를 출력시 에러발생
print(stu_dic.get('kor'))
print(stu_dic.get('math'))  # 없는 key를 출력시 실행됨. - None 출력  # get을 넣었기때문

# 딕셔너리 정렬
import operator
names = {"홍길동":100,"유관순":80,"이순신":90,"김구":99,"강감찬":95}
names2 = sorted(names.items(),key=operator.itemgetter(0))
# reverse = True : 역순정렬, reverse=False : 순차정렬
# itempetter(0):키, itemgetter(1):값
names2 = sorted(names.items(),key=operator.itemgetter(0),reverse=True)
# names2 = sorted(names.items(),key=operator.itemgetter(1),reverse=True)
print(names)
print(names2)

# 리스트 정렬
a_list = [1,5,9,4,3]
## sort() -> 해당리스트 자체를 정렬, 원본 변경
# a_list.sort()    # a_list 값 자체가 sort로 변경됨
a_list.reverse() # 1,5,9,4,3 -> 3,4,9,5,1  # 순서가 변경
## sorted() -> 다른변수에 저장가능, 원본은 변경안됨.
# reverse = True : 역순정렬
b_list = sorted(a_list,reverse=True)
print(a_list)
print(b_list)

# 리스트 최대값 - max : 리스트에서 최대값 출력
print(max(a_list))        # 리스트에서 최대값 출력
print(min(a_list))        # 리스트에서 최소값 출력