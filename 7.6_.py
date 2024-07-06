#교수님코드-문제복습
import random

srp=['가위','바위','보']
random.shuffle(srp)
my_srp=com_srp='가위'

while my_srp==com_srp:
    com_srp=random.choice(srp)
    #print(com_srp)
    while True:
        my_srp=input("가위 바위 보 중 하나를 입력")
        if my_srp in srp:
            break
        else:
            print('잘못 입력하였습니다. 다시 입력해주세요')
    if my_srp==com_srp:
        print('비겼습니다. 다시합니다')
    elif (my_srp=='가위' and com_srp=='보')or (my_srp=='바위' and com_srp=='가위')or( my_srp=='보'and com_srp=='바위'):
        print('당신이 이겼습니다')
    else:
        print('당신이 졌습니다')


#수정된 코드
import random

srp = ['가위', '바위', '보']
random.shuffle(srp)
my_srp = com_srp = '가위'

while my_srp == com_srp:
    com_srp = random.choice(srp)
    #print(com_srp)
    while True:
        my_srp = input("가위 바위 보 중 하나를 입력: ")
        if my_srp in srp:
            break
        else:
            print('잘못 입력하였습니다. 다시 입력해주세요')
    if my_srp == com_srp:
        print('비겼습니다. 다시합니다')
    elif (my_srp == '가위' and com_srp == '보') or (my_srp == '바위' and com_srp == '가위') or (my_srp == '보' and com_srp == '바위'):
        print('당신이 이겼습니다')
    else:
        print('당신이 졌습니다')




#list 정리
a=['1','2','3','4','5','6']
print(a)
#print(a[])
print(a[:])
print(a[ : ])
#->모든 요소 출력하는 건 다 똑같음. 쉽다
a.append('나나')
a.append('나나')
print(a)
a.insert(3,'나나')
print(a)

a.remove('나나') #remove는 첫번쨰 요소만 출력
print(a)
del a[6:8] #del은 슬라이싱으로 구간 단위로 삭제
print(a)
b=a.pop(0) #0번쨰 요소만 삭제시킴
print(b)

print(a.index('6'))
#a.sort()
#print(a.sort())>>None: a.sort()는 리스트를 정렬하지만 반환값은 None이다.
a.sort()
print(a) #print는 반환값은 없지만 출력을 해주니까!
#오름차순 정렬(작은것부터)하는 리스트 컴프리헨션 먼저


a.sort(reverse=True)
print(a)

#추가적으로 수업시간에 배운
a=['1','2','3','4','5','6','7']
a.reverse() #순서 역순으로 변경
b=sorted(a) #sorted(list)는 원본 변경 X, a와 동일한 다른 리스트 반환!
print(a)#역순a출력
print(b) #a출력
print(a.index('4'))