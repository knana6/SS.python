import random
a=[random.randint(1,6)for i in range(50)]
print(a)
print(a.count(input("출력할 요소를 입력하세요")))
##if b in not a:
##    continue
##else:
##    print(b)
while True:
    num=int(input("주사위 눈값(1~6)입력"))
    if not(1<=num<=6): #1~6사이의 값이 아니라면
        print("잘못 입력하였습니다. 다시 입력하세요")
        continue
    print(f"{num}눈값의 개수: {a.count(num)}개")
    break #무한루프 탈출



#2차원 리스트
num=[[10,20,30],[40,50,60],[70,80]]
slist1=['Love','Like','Excellent','Good','Great']
slist2=[['Python','C programming'],['Java','C++']]
print(num)
print(num[0])
print(num([0][0]))
print(slist1)
print(slist1[0])
print(slist1[0][0])
print(slist2)
print(slist2[0])
print(slist2[0][0])
print(slist2[0][0][0])
#순서: 리스트-요소-글자(문자)
print(num[1][1])
print(slist1[2][1])
print(slist2[1][0])


#list comprehension 이용
a=[input("영웅들의 이름을 입력하세요")for i in range(5)]


#split()이용
heroes=input("영웅들 이름 입력").split(" ")
print(heroes)


for i in[1,2,3,4,5]:
    print(i,end=" ")
print()
for i in range(5):
    print(1,end="")
print()

#인덱스 필요없고 요소값만 출력하면 된다
list1=[10,20,30,40,50,]
for i in list1:
    print(i ,end=" ")
print()

#인덱스 번호도 필요한 경우, range를 이용해서 [i]이용하기 
for i in range(len(list1)):
    print(f"{i}:{list1[i]}",end=" ")


#왕이름 알려주는 코드 작성
k=[]
for i in range(4):
    king=input("조선시대 왕 순서 입력")
    k.append(king)

print(k)
count=1
for i in k:
    for j in i:
        if j=='연':
            print("연산군")
        elif j=='광':
            print("광해군")
        elif count in [1,7,14,16,21,22,23]:
            print(j+"조")
        else:
            print(j+"종")
        count+=1



#문제인데 보충 .. 
import random
a=(random.randiant(1,100) for i in range(30))
print(a)
num=0
for i in a: #요소 하나씩 가져와서 50 이상인지 확인하기
    if i>=50:
        print(i,end=" ")
        num+=1
prin(num)
print(b)



#오류뜨는 오느르이 명언
import random
q=[]
q.append("꿈을 지녀라, 그러면 어려운 현실은 이길 수 있다")
q.append("분노는 바보들의 가슴 속에서만 살아간다")
q.append("고생없이 얻을 수 있는 진실로 뒤중한 것은 하나도 없다")
q.append("사람은 사랑할 떄 누구나 시인이 된다")
q.append("시작이 반이다")
dq=random.choice(q)
print("#"*20)
print("#"+" "*3+"오늘의 명언")
print("#"*20)
print()
print*dq



#멋있는 스파이럴 그리기.. 근데 외않되?
import turtle
t=turtle.Turtle()
t.speed(0)
t.width(3)
length=10
colors=['red','purple','blue','green','yellow','orange']
while length<500:
    t.fd(length)
    t.pencolor(colors[length%6]) #6으로 나는 나머지(0~5)를 인덱스로 사용
    t.rt(89)
    length+=5

#리스트를 불러올 수 없는 오류



#오륜기 그리는 활동
import turtle
t=turtle.Turtle()
positions=[[0,0,'green'],[-120,0,'yellow'],[60,60,'red'],[-60,60,'black'],[-180,60,'blue']]
t.pensize(5)
for x,y,c in positions #리스트 안에 요소 수에 맞춰 변수를 할당한다
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color(c,c) #컬러두개쓰면 선색, 채우기색 순서임, 채우기색도 지정했지만 begin end 안시켜서 소용없음
    t.circle(60)




#교재 문제: 1차원 리스트 이용
temp_list=[0,10,20,30]
vapor_list=[4.8,9.4,17.3,30.4]

vapor=float(input("현재 수증기량 입력"))
temp=int(input("현재 온도 입력"))

if temp in temp_list:
    humidity=(vapor/vapor_list[temp_list.index(temp)])*100
    print("현재 습도는", round(humidity,2), "%입니다")




#응용 문제: 2차원 리스트 이용
a=[[0,4.8],[10,9.4],[20,17.3],[30,30.4]]
b=float(input("현재 수증기량 입력"))
if b in a:
    al=a.index(b)
    humidity=a.index(b+1)
    print(humidity)




#정답..인데 작동원리를 파악못함 아 
a=[[0,4.8],[10,9.4],[20,17.3],[30,30.4]]
v=float(input("현재 수증기량 입력"))
t=int(input("현재 온도 입력"))
for i in a:
    if t in i:
        humidity=(v/i[1])*100
        print("현재습도는", round(humidity,2),"%입니다")




#추가문제: 내꺼 왜안되는지 알아보고 수정을 하자.
import random
a=['치약','샴푸','린스','주방세제','키친타올','칫솔']

while True:
    a.insert(random.randint(0,len(a)), input("구매할 추가 물품 하나를 입력"))
    print(a)

    b=input("구매할 물품")
    if b in a:
        bi=print(a.index(b))
        print(f"{b}는 {bi+1} 번째에 있습니다")
        a.remove(b)
        print(a.sort(reverse=True))
    else:
        print("물품이 리스트에 없습니다")




#패널티킥 5번하는 게임
import random
a=['오른쪽','왼쪽','가운데']
b=['상단','하단']
count=0

for i in range(5):
    ac=random.randint(0,len(a))
    bc=random.randint(0,len(b))
    #print(ac,bc)

    ag=input("오른쪽 왼쪽 가운데 중 하나 입력")
    bg=input("상단 하단 중 하나 입력")
    ai=a.index(ag)
    bi=b.index(bg)
    #print(ai,bi)

    if ac==ai and bc==bi:
        print("패널티킥 실패")
        continue  
    else:
        print("패널티킥 성공")
        count+=1
        continue
    
print(f"총{count}번 성공했다!")


#교수님 정답(리스트만 보충)
import random
goal=
goal2=
i,cnt=0,0
while i<5:
    com=random.choice(goal)
    print(com)
    while True:
        me1=input("왼쪽 오른쪽 가운데 중 하나를 입력")
        if me in goal2:
            break
        else:
            print("다시 입력해주세요")
    me2=input("상단 하단 중 하나를 입력")
    me=f"{me1} {me2}" #덧셈연산자쓸거면 me1+" "+me2: 리스트에 있는 문자열 형태
    if com==me:
        print("패널티킥 실패")
    else:
        print(f"com:{com}")
        print(f"me:{me}")
        print("패널티킥 성공")
        cnt+=1
    i+=1
print(f"총 {cnt}번 성공")


#가위바위보게임
import random
l=['가위','바위','보']
while True:
    cl=random.choice(l)
    ml=input("가위 바위 보중 하나를 입력")
    if ml not in l:
        print("잘못 입력, 다시 입력해라")
        continue
    if ml==cl:
        print("비겼습니다")
    if ml=='가위'and cl=='바위':
        print("졌습니다")
    if ml=='가위'and cl=='보':
        print("이겼습니다")
    if ml=='바위'and cl=='보':
        print("졌습니다")
    if ml=='바위'and cl=='가위':
        print("이겼습니다")
    if ml=='보'and cl=='바위':
        print("이겼습니다")
    if ml=='보'and cl=='가위':
        print("졌습니다")
    break        
