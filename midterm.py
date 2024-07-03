#오늘의 공부 순서: 오늘 진도 문제 다풀기, 교재 복습, 노션 정리 마무리 !
##a=input("문자를 입력하세요")
##for i in range(len(a)):
##    print(a[:i+1])


##import turtle
##t=turtle.Turtle()
##t.shape("turtle")
##a=int(turtle.textinput("","다각형을 입력하세요"))
##for i in range(a):
##    t.fd(100)
##    t.lt(360/a)



#순서쌍 만들기
##for i in range(4):
##    for j in range(4):
##        print("(%s,%s)"%(i,j),end="")
##        if j==1:
##            break
##        print()



# 1부터 100까지 합
##count=1
##sum=0
##while count<=100:
##    sum+=count
##    count+=1
##print(sum)



#비밀번호 입력
##password=""
##while password!="pythonisfun":
##    password=input("암호를 입력하세요")
##print("로그인 성공")



##for i in range(5):
##    for j in range(10):
##        print("*", end="")
##    print()



##for i in range(5):
##    for j in range(i+1):
##        print("*",end="")
##    print()
        


##sign=True
##
##while sign:
##    light=input('신호등 색상을 입력하시오')
##    if light=='blue':
##        sign=False
##print('전진')



##
##for n in range(10):
##    if n%2==0:
##        continue
##    print(n)
##    # 2의 배수일때만 반복문 안에있고, 나머지 있을시 탈출하므로 print



#lab1. 코드 줄이기
##import turtle
##t=turtle.Turtle()
##t.shape("turtle")
##n=0
##
##while True:
##    t.circle(100)
##    t.lt(60)
##    
##    n+=1
##    if n==6:
##        brake

    
#<=>
##import turtle
##t=turtle.Turtle()
##for i in range(6):
##    t.circle(100)
##    t.left(60)



##import random
##tries=0
##guess=0
##
##answer=random.randint(1,100)
##print("1부터 100사이의 숫자를 맞추시오")
##
##while guess!=answer:
##    guess=int(input("숫자를 입력하세요"))
##    tries+=1
##    if guess<answer:
##        print("낮음")
##    elif guess>answer:
##        print("높음")
##    if tries==5:
##        break
##if guess==answer:
##    print("축하합니다, 시소횟수는", tries,"회")
##
##else:
##    print("실패했습니다 정답은",answer,"입니다")


#오류해결해야
##import turtle,random
##t=turtle.Turtle()
##t.speed(0)
##t.pensize(10)
##
##pnum=random.randint(10,20)
##for i in range(pnum):
##    r=random.random()
##    g=random.random()
##    b=random.random()
##    r2=random.random()
##    g2=random.random()
##    b2=random.random()
##    x=random.randint(-300,300)
##    y=random.randint(-300,300)
##    length=random.randint(10,100)
##    
##    t.penup()
##    t.goto(x,y)
##    t.pendown()
##    t.pencolor(r,g,b)
##    t.fillcolor(r2,b2,g2)
##    #t.color((r,g,b),(r2,g2,b2))
##    
##    poly=random.randint(3,12)
##    t.begin_fill()
##    for kin range (poly):
##        t.fd(length)
##        t.lt(360//poly)
##    t.end_fill()



#최대공약수
n=int(input("정수1"))
m=int(input("정수2"))

if n<m:
    n,m=m,n

while m>0:
    r=n%m
    n,m=m,r
if n!=1:
    print("두수의치대공약수",n)
else:
    print("두수는 서로소")    





















































































































































































