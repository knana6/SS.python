# 학번: 202421405



import random #사용할 모듈

def biglist(q): #대문자 q(0~3)개 랜덤 리스트 제작
    qnum = random.sample(range(65, 91), q)
    qlist = [chr(i) for i in qnum] #숫자 영문 변환 함수 사용
    return qlist

def smalllist(s):#소문자 s개 랜덤 리스트 제작
    snum = random.sample(range(97, 123), s)
    slist = [chr(i) for i in snum]
    return slist

def all_shuffle(finlist): #모든 셔플 경우를 출력하는 함수
    allcase = [] #결과 저장할 리스트, append 로 새로운 케이스 추가할 것
    while len(allcase) < 6: #경우의 수 6가지 (3*2)
        shuffled_list = finlist[:]  # 리스트 복사, 셔플할 리스트 만들기
        random.shuffle(shuffled_list)  # 셔플 리스트 셔플
        if shuffled_list not in allcase:  # 중복 결과는 제외
            allcase.append(shuffled_list)# 셔플된 리스트를 추가
        else:
            continue 
    return allcase


## main part ##
q = random.randint(0, 3)
list1 = biglist(q)
s = 3 - q
list2 = smalllist(s) #여기까지 대문자, 소문자 리스트 따로 생성

finlist = list1 + list2 #리스트 병합
random.shuffle(finlist) #리스트 셔플(순서도 랜덤이기에)
print(f"추출된 문자 3개: {finlist}") #영문 3개 랜덤 리스트 최종 출력

allcase= all_shuffle(finlist)
print(f"문자들을 조합한 요소를 갖는 리스트 출력:{allcase}")

allcase1=sorted(allcase)# 정렬 리스트 따로 저장

for u in allcase1: #각 리스트(3문자당 리스트 하나)들 순회
    allcasefin='' #여기에 저장할 것
    for d in u: #u가 순회하며 d는 더 안쪽의 요소들을 순회(u 안의 각 요소)
        allcasefin+=d #여기에 하나씩 추가(문자열끼리 +가능)
    print(allcasefin, end=" ") # 3개당 한 묶음처럼 보이게 여백 한칸 남겨두기


 #마지막 과제라니 뭔가 시원섭섭합니다 :)

