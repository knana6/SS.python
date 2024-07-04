##slist=['영어', '수학','사회','과학']
##print(slist) #리스트 전체
##print(slist[0]) #첫번째 요소
##print(slist[0][0]) #리스트는 문자열이므로 첫번째 요소의 첫번째 글자
##print(slist[2][1])
##
##nlist=[7,12,77,777]
##print(nlist)
##print(nlist[0])


##cart=[] #공백리스트
##cart.append("사과") #리스트에 마지막 위치를 추가할 떄 사용하는 함수
##cart.append("포도") #리스트 마지막에 요소를 추가
##cart2=["오렌지"]
##cart2.append("포도")
##cart2.append("사과")
##print(cart)
##print(cart2)
##cart[1]="바나나" #인덱스 이용해 해당 요소 변경
##print(cart)
##cart2[2]="바나나"
##print(cart2)
##cart2[3]="체리" # 요소가 없는 인덱스에 값 추가나 변경 불가
##print(cart2)


##alist=['a','b','c','d,','e',f',''g','h','i']
##print( alist[2]) #인덱스 이용 요소 하나
##print(alist[2:3]) #슬라이싱 이용 요소 하나-결과는 리스트
##print(alist[2:5]) #슬라이싱 이용 요소 여러개
##print(alist[:5]) #첫번째 요소부터
##print(alist[:5]) # 마지막 요소까지
##print(alist[ : ]) #리스트 전체 추출
##
##
##blist=alist #alist 의 또다른 이름 blist
##clist=alist[:] #alist를 복사한 새로운 clist
##blist[0]='A'
##print(alist)
##print(blist)
##clist[0]='Z'
##print(alist)
##print(clist)


##list1=[1,3,14,True,'string',[1,2,3]]
##print(list1)
##alist=['a','b','c','d','e','f','g','h','i']
##blist=alist[:] #복사
##alist[2:5]='k' #슬라이싱되는 값들이 'k'로 치환
##print(alist)
##alist[2:5]=['c','d'] #슬라이싱에 리스트 요소들로 치환
##blist[2]=['c','d'] #인덱스 위치에 리스트가 요소로 치환,슬라이싱을 사용하면 요소로 바뀌지만 인덱싱을 이용하면 대괄호 자체가 하느이 값으로 들어간
##print(alist)
##print(blist)



##cart=['사과','섬유유연제','화장지','치약']
##cart.append('양말')
##print(cart)
##cart.insert(1,'건전지')
##print(cart)
##cart.insert(0,'라면')
##print(cart)
##cart.insert(len(cart),'칫솔')
##print(cart)



##alist=[]
##blist=list()
##clist=list('string') #괄호안에 시퀀스 넣으면 시퀀스를 하나의 리스트로 만들어
##dlist=list(range(10))
##print(alist)
##print(blist)
##print(clist)
##print(dlist)




##alist=['a','b','c']
##blist=[1,2,3]
##dlist=[4,5,6]
##clist=list('string') 
##clist.extend(alist) #순서대로 확장됨
##print(alist)
##print(clist)
##dlist.extend(blist)
##print(blist)
##print(dlist)
##elist=alist+blist #순서대로 병합됨
##print(elist)




##cart=['사과','세제','화장지','치약','화장지']
##cart.remove('화장지') #첫번째로 발견한 화장지만 삭제됨
##print(cart)
##if '라면' in cart: #if요소 in 리스트: 리스트에 요소가 있다면, 조건문 없으면 valueerror 
##    cart.remone('라면')
##print(cart)




##alist=[1,2,3,4,5,6,7,8,9,10]
##del alist[3]
##print(alist)
##del(alist[3])
##print(alist)
##del alist[2:5]
##print(alist)




##cart=['사과','세제','화장지','치약','화장지']
##item=cart.pop()
##print(cart,item)
##item=cart.pop(0)
###인덱스 사용도 가능, 인데스 위치의 요소를 반환하면서 삭제
##print(cart,item)




cart=['사과','세제','화장지','치약','화장지']
cart[1:3]=[] #리스트 1~2 위치의 요소를 삭제
print(cart)
##cart.clear() #리스트 전체 요소를 삭제, 공백 리스트가 됨
##del cart[:]
##cart[:]=[]
##cart=[] #공백 리스트로 치환
##del cart #변수 자체가 소멸되므로 이후에 변수를 찾을 수 없음
print(cart)
### 위에 샵 된것들 질문하자,. ㅎㅎ ㅎㅎㅎㅎ ㅎㅎ



##
##cart=['사과','세제','화장지','치약','화장지','샴푸','린스']
##print(cart.index('화장지'))
##if '라면' in cart:
##    print(cart.index('라면'))
##print(cart.index('화장지',3,6))
###print(cart.index('린스',3,6)) # 이건 범위 내에 린스가 없기 때문에 에러가 발생, 린스 위치 못찾음
##print(cart.index('린스',3,len(cart)))




# 오름차순 내림차순 역순 원본 변경 등 응용되는 표현들(중요)
##cart=['사과','세제','화장지','치약','화장지','샴푸','린스']
##cart2=cart[:] #리스트 복사
##cart3=cart[:] #리스트 또복사
##cart.sort() #오름차순 정렬
##print(cart) #원본 변경
##cart2.sort(reverse=True) #내림차순 정렬
##print(cart2)
##c1=sorted(cart3) #오름차순 정렬된 새 리스트 생성
##print(c1)
##c2=sorted(cart2,reverse=True) #내림차순 정렬된 새 리스트 생성, sorted 쓰면 원본은 변경되지 않음
##print(c2)
##cart2.reverse() #순서를 역순으로 변경
##print(cart3) #원본 변경됨
##cart3.sort() #오름차순 정렬한 후
##cart3.reverse() # 순서를 역순으로 변경하면
##print(cart3) # 내림차순 정렬
##



##import random
##alist=[1,3,8,3,9,4,6,3,7,2,1,6,5,3,7]
##print(alist.count(3))
##print(alist.count(10))
##blist=[random.randint(1,10) for i in range(10)]
##print(blist)
### blist 작성법은 clist 작성법을 한문장으로 간단하게 나타내는 방법이다. (중요)
##clist=[]
##for i in range(10):
##    clist.append(random.randint(1,10))
##print(clist)


##import random
##alist=[random.randint(1,100) for i in range(10)] #랜덤값 10개 저장, 같은 값이 나올수도 있음
##print(alist)
##print(random.choice(alist))
##print(random.choice(range(1,11)))
##print(random.choice("Good morning")) #굿모닝 중 랜덤값 하나반환
##
##
##blist=[1,2,3,4,5,6,7]
##list1=random.sample(blist,2) #sample 에서는 중복 추출 안됨.
##list2=random.sample(range(1,21),3)
##list3=random.sample("Good morning",3) # sample이니 같은 문자가 있다고 해도 중복이 아님
##list4=random.sample(blist,7) #전체를 샘플링해도 중복이 없음
###list5=random.sample(blist,8) #샘플 개수가 더 많으면 안됨
##list6=random.sample(blist,1) # 샘플이 하나라도 결과는 리스트
##print(list1,list2,list3,list4,list6)
##
##
##clist=blist.copy()
##random.shuffle(clist)
##print(clist)


##import random
##alist=[random.randint(1,6) for i in range(10)]
##print(alist)
##
##dice2=list() #공백리스트 생성
##for i in range(10):
##    dice2.append(random.randint(1,6))
##print(dice2)


import random
alist=[]
for i in range(5):
    alist.append(input("해야할일")) #split 대신 멀 써야 하지 ,쓸수는잇다!
print(alist)
random.shuffle(alist)
print(alist)
a=random.sample(alist,1)
alist.remove(a)
print(alist)  # 오류 뜨는 이유 여쭤보자 ㄹㅇ 이게 외않되?, 초이스랑 샘플 차이점; 문자열인지 리스틔인지



##import random
##dolist=[inpur(f"해야 할 일 입력({i+1}):") for i in range(5)]
##print("해야 할 일", dolist)
##random.shuffle(dolist)
##print("해야 할 일",dolist)
### 리무브 쓸떄는 이프문 같이 써줘라
