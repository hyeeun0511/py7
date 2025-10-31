english = {                                    # {key:value}
    '사랑':'love',              
    '커피':'coffee',
    '컴퓨터':'computer',
    '이름':'name',
    '한국':'korea',
    '개':'dog',
    '나무':'tree',
    '하늘':'sky',
    '손':'hand',
    '피부':'skin',
    '건강':'health',
    '꽃':'flower',
    '얼굴':'face',
    '안경':'glasses',
    '티':'tea',
    '질문':'question',
    '새':'bird',
    '동물':'animal',
    '학생':'student',
    '색':'color'
}

# 20문제중에 랜덤으로 5문제를 뽑아서 퀴즈를 만드시오.
import random
a_list = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
quest = random.sample(a_list,5)          # 랜덤으로 5개 뽑는것 - 20문제중 5개를 추출
quest.sort()                             # 랜덤5개를 순서대로 정렬
quest_dic = {}                           # 정답,오답 입력을 위한 저장공간
# print(quest)  # [0, 11, 12, 14, 17, 19]
num = 1

for i,k in enumerate(english.keys()):    # enumerate : index와 key를 함께 추출
    if i in quest:
        # print(i,k,english[k])
        count = 0
        print("{} 은(는) 영어로 무엇인가요? ".format(k))
        answer = input(">> ")
        # 정답확인
        if answer == english[k]:
            print("띵동! 정답입니다.")
            count = count + 1             # count += 1
            quest_dic[num] = "정답"          # num : 문제 번호 (1.- 2.- ...)
        else:
            print("오답 : ",english[k])
            quest_dic[num] = "오답"
        num = num + 1
# 1:정답 2:오답 3:오답 4:정답 5:정답
print(quest_dic)
print("정답 :",count)
        




# ----------- 내가 풀어본 과정 ---------#
# question = random.sample(range(1,20),5)
# count = 0
# for i in range(5):
#     for k,v in english.items():
#         # 정답입력
#         print("{} 은(는) 영어로 뭘까요? ".format(k))
#         answer = input(">> ")
#         # 정답 or 오답
#         if answer == v:
#             print("띵동! 정답입니다.")
#             count = count + 1   # count += 1 라고 표기해도 같은 의미
#         else:
#             print("오답 : ",v)
#             if answer == 5:
#                 break
        
        
    # 1:정답 2:오답 3:오답 4:정답 5:정답
        
        


# # 영어맞추기 프로그램을 구현하시오.          # key를 보고 value를 맞추는것
# # 사랑 ? love
# count = 0
# for k,v in english.items():
#     # 정답입력
#     print("{} 은(는) 영어로 뭘까요? ".format(k))
#     answer = input(">> ")
#     # 정답확인
#     # 정답 or 오답
#     # answer == v(value)
#     if answer == v:
#         print("띵동! 정답입니다.")
#         count = count + 1   # count += 1 라고 표기해도 같은 의미
#     else:
#         print("오답 : ",v)
        
        
#     # 1:정답 2:오답 3:오답 4:정답 5:정답
# print("정답 :",count)
