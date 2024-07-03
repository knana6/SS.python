##a=input("문자 입력")
##l=len(a)
##i=0
##while i<=len(a):
##    print(a[:i])
##    i+=1
##
##str1=input("문자열 입력")
##str_len=len(str1)
##i=1
##while i<=str_len:
##    print(str1[:i])
##    i+=1


##for i in range(5):
##    for j in range(10):
##        print("*", end=" ")
##    print(" ")
#질문: 여기서 각 변수는 초깃값 설정을 안해도 되나?


##for i in range(5):
##    print("*"*10)
#이거랑 같다, 연산자 이용하면 간단하게 나타낼 수 있어용



#별 삼각형 그리기
##for i in range(1,6):
##    for j in range(1,i+1):
##        print("*",end=" ")
##    print("")


##
##for i in range(4):
##    for j in range(4):
##        print("(%s,%s)"%(i,j), end="")
##        if j==1:
##          break
##    print()


##for n in range(10):
##    if n%2==0:
##        continue
##
##print(n)
##
##
##n2=-0
##while n2<=9:
##    n2+=1
##    if n2%2==0:
##        coninue
##    print(n2)
##
##%continue 이용
##for i in range(4):
##    for j in range(4):
##        if j==2:
##            continue
##        print("(%s,%s)"%(i,j),end=" ")
##    print()


##import turtle
##t=turtle.Turtle()
##for i in range(6):
##    t.circle(100)
##    t.lt(60) #t.lt(360/6)



#내가쓴답 (오답)
##import turtle,random
##t=turtle.Turtle()
##a=int(turtle.textinput("", "원의 개수 입력 3~6개"))
##b=random.randint(100,200)
##
##if 3<=a<=6:
##    for i in range(a):
##        t.circle(b)
##        t.lt(360/a)
##        break #이렇게 쓰면 for문 안에 있으므로 안된다, 무한루프 쓸떄 for문 밖에 break 쓰기
##else:
##    t.write("다시 입력해주세요")



##정답( 다시입력받을수있음, break의 올바른이용)
##import turtle,random
##t=turtle.Turtle()
##a=int(turtle.textinput("", "원의 개수 입력 3~6개"))
##radius=randon.radnint(100.250)
##while true:
##    n=int(turtle.textinput(" ","3456 입력"))
##    if 3<=n<=6:
##        for i in range(n):
##            t.circle(radius)
##            t.lt(360/n)


#lab03. n강형 그리기
##import turtle,random
##t=turtle.Turtle()
##t.shape("turtle")
##s=int(turtle.textinput("","몇각형을 원하시나요?"))
##for i in range(s):
##    t.fd(100)
##    t.lt(360/s)



#문제) n각형, 길이 50~250, 3~12각형, 잘못하면 다시입력

##import turtle,random
##t=turtle.Turtle()
##t.shape("turtle")
##
##
##b=random.randint(50,250)
##
##while True:
##    a=int(turtle.textinput(" ", "몇각형을 원하시나요"))
##    #얘를 무한 반복문 안에 넣는 이유는 틀렸을 시 다시 입력을 받기 위함이다
##    if not 3<=a<=12:
##        continue
##    for i in range(a):
##        t.fd(b)
##        t.lt(360/a)
##    break

#질문: 왜 continue 가 안될까?
    

#랜덤 워크
##import turtle, random
##t=turtle.Turtle()
##t.shape("turtle")
##for i in range(30):
##    length=random.randint(1,100)
##    t.fd(length)
##    angle=random.randint(-180,180)
##    t.rt(angle)



#범인 찾기 응용: 2번 틀릴때마다 범인의 위치를 랜덤으로 변경시킨다<<가 어렵다
##해결 방법: 틀릴 때마다 +1되는 변수를 하나더 만들기 ㅋㅋ
##import random
##score=100
##wrong=0
##room=random.randint(1,3)
##
##while True:
##    n=int(input("방 번호를 입력하세요"))
##    if n==room:
##        print("범인 체포")
##        score+=100
##        break
##    elif n>3:
##        print(n,"번 방은 없습니다.")
##    if not n==room:
##        room=random.randint(1,3)
##    else:
##        print("범인이 없습니다")
##        score-=10
##print("게임종료")
##print(f"점수:{score}점")


##
##import turtle,random
##t=turtle.Turtle()
##t.pensize(10)
##t.speed(0)
##many=1
##for i in range(20):
##    r=random.random()
##    g=random.random()
##    b=random.random()
##    r2=random.random()
##    g2=random.random()
##    b2=random.random()
##   
##   
##    x=random.randint(-300,300)
##    y=random.randint(-300,300)
##
##    length=random.randint(10,300)
##    a=random.randint(3,12)
##    b=random.randint(10,20)
##    c=random.randint(10,100)
##    
##    t.penup()
##    t.goto(x,y)
##    t.pendown()
##    t.color((r,g,b),(r2,g2,b2))
##
##while many<=b:
##    t.begin_fill()
##    for j in range(a):
##        t.fd(c)
##        t.rt(360//a)
##        many+=1
##    t.end_fill()

    # 길고긴 보투, 헤드방햫 0도로 설정하지않ㄴ는이상 도형은 비뚤어져있을것임

##
##n=int(input("자연수 입력"))
##for m in range(1,n+1):
##    if n%m==0:
##        print(m,end=" ")
##
##print()
##for m in range(n+1):
##        if n%(m:1):
##              print((m+1, end"")) #보충333


# 최대공약수
##n1,n2=input("정수 2개 입력").split(" ")
##n1, n2=int(n1), int(n2)
##if n1<n2:
##    n1,n2=n2,n1 #두 값을 교환
##while n2>0:
##    r=n1%n2
##    n1, n2= n2, r # n1, n2를 n2, r 으로 변경
##
##if n1!=1:
##    print("두 수의 최대공약수",n1)
##else:
##    print("두 수는 서로소")


import random
tries=0 #시도횟수
guess=0

answer=random.randint(1,100)
print("1부터 100 사이의 숫자를 맞추시오")

while guess!=answer:
    guess=int(input("숫자를 입력하세요"))
    tries+=1
    if guess<answer:
        print("낮음")
    elif guess>answer:
        print("높음")
    if tries==5:
        break
 
if guess==answer:
    print("축합니당. 시도횟수=", tries)
else:
    print("실패했습니다 정답은:", answer)
