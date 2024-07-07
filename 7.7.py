#최근 문제

#리스트
import random
a=['치약','샴푸','린스','주방세제','키친타올','칫솔']

while True:
    n=input("추가할 물품 입력")
    a.insert(random.randrange(0,6),n) #랜덤위치 삽입은 insert(인덱스,요소)
    print(a)
    
    get=input("모살거야?")
    if get in a:
        print(f" {get}는 {a.index(get)+1}번째에 있습니다")
        a.remove(get)
        a.sort(reverse=True) #내림차순은 리버스 트루, 오름차순은 소트.
        print(f"내림차순 정렬:{a}")
    else:
        print("물품이 없는데용")
        

#교수님 답안
import random
plist=['치약','샴푸','린스','주방세제','키친타올'.'찻솔']
prod=input('구매할 물품 입력')
n=random.randint(0,len(plist)) #n을 0~끝요소 인덱스 로 먼저 숫자뽑기
plist.insert(n,prod)# isert(인덱스,요소)
print(plist)


#숫자맞추기 
import random

b=random.randint(1,100)
for i in range(5):
    a=int(input("1부터 100까지의 숫자 입력")) #계속 입력받을 거니까 반복문 안에 넣어주쟈
    if a>b:
        print('다운~')
    elif a<b:
        print('업!')
    else:
        print('정답입니다 ㅎㅎ')
print(f"실패, 정답은 {b}입니다")


#범인 잡아라
import random
score=100
wrong=0
room=random.randint(1,3)

while True:
    n=int(input("방 번호를 입력하세용"))
    if not (1<=n<=3):
        print("잘못 입력했쥬")
        continue
    if n==room:
        print(n,"번 방에 범인의 모습이..두둥..")
        break
    else:
        print(n,"번 방에는 범인은 없고 먼지뿐이다..수북하구만,,")
        score-=10
        print("현재 점수는 %s점" %(score))
        if score<=0:
            break
        wrong+=1
        if wrong==2:
            room=random.randint(1,3) #2번 틀렸다면 범인 위치 초기화 ㅎㅎ
            print("범인 위치: %s" %(room))



#문자열 길이만큼 반복, 완성하기
a=input('문자열 입력')
n=1

#case1 range 이용
for i in range(len(a)):
    print (a[0:n])
    n+=1

#case2 while 이용
while n<=len(a):
    print(a[0:n])
    n+=1



#사용자가 원하는 도형 그리기
import turtle
t=turtle.Turtle()
t.shape("turtle")
s=turtle.textinput(" ", "도형을 입력하세요")

if s=="직사각형":
    w=int(turtle.textinput(" ","가로 길이 입력"))
    h=int(turtle.textinput(" ", "세로 길이 입력"))
    t.fd(w)
    t.lt(90)
    t.fd(h)
    t.lt(90)
    t.fd(w)
    t.lt(90)
    t.fd(h)
    t.lt(90)

if s=="정삼각형":
    w=int(turtle.textinput(" ","한 변의 길이 입력"))
    t.fd(w)
    t.lt(120)
    t.fd(w)
    t.lt(120)
    t.fd(w)
    t.lt(120)    

elif s=='원':
    r=int(turtle.textinput(" ","반지름 길이 입력"))
    t.circle(r)

