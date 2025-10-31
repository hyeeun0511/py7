# 튜플 - 리스트와 동일, 수정불가      리스트-[] / 튜플-()
a_list = [1,2,3,4,5]
a_tu = (1,2,3,4,5)
print(a_list)
print(a_tu)
print(a_list[2])
print(a_tu[2])
a_list[0] = 100
print(a_list)
# a_tu[0] = 100      # 에러 # 튜플은 수정불가 
# print(a_tu)
del(a_list[0])
print(a_list)

# del(a_tu[0])       # 에러 # 튜플은 삭제불가
# print(a_tu)