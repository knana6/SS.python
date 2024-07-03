##import turtle, random
##scr=turtle.Screen()
##front='./img/front.gif'
##back='./img/back.gif' # 경로 포함 파일명, 확장자까지 문자열을 저장
##scr.addshape(front) # 이미지 등록
##scr.addshape(back) # 이미지 등록
##t=turtle.Turtle()
##coin=random.randint(0,1) # 0은 앞면, 1은 뒷면으로 저장
##if coin==0:
##    t.shape(front)
##else:
##    t.shape(back)
###파일 경로랑 이미지 폴더 경로를 같은 폴더에 저장해야 함


##import turtle,random
##scr=turtle.Screen() #스크린 객체 생성, 화면에 표시되는 것 제어!
##
##dice1='./img/dice1.gif'
##dice2='./img/dice2.gif'
##dice3='./img/dice3.gif'
##dice4='./img/dice4.gif'
##dice5='./img/dice5.gif'
##dice6='./img/dice6.gif'
##
##scr.addshape(dice1) # 스크린이 쓸 수있도록 파일을 등록하는 
##scr.addshape(dice2)
##scr.addshape(dice3)
##scr.addshape(dice4)
##scr.addshape(dice5)
##scr.addshape(dice6)
##
##t=turtle.Turtle()
##dice=random.randint(1,6)
##if dice==1:
##    t.shape(dice1)
##if dice==2:
##    t.shape(dice2)
##if dice==3:
##    t.shape(dice3)
##if dice==4:
##    t.shape(dice4)
##if dice==5:
##    t.shape(dice5)
##if dice==6:
##    t.shape(dice6)


##import turtle,random
##scr=turtle.Screen()
##front='img/front.gif'
##back='img/back.gif'
##
##scr.addshape(front)
##scr.addshape(back)


##t=turtle.Turtle()
##coin1=random.randint(0,1)
##coin2=random.randint(0,1)
##t.up()
##t.goto(-200,0)
##
##if coin1==0 and coin2==0:
##    t.shape(front)
##    t.stamp()
##    t.up()
##    t.goto(200,0)
##    t.shape(front)
##    t,stamp()
##    t.shape("turtle")
##    t.up()
##    t.goto(0,300)
##    t.write("성공", False, "center",(" ",20, "bold"))
##    
##if coin1==1 and coin2==1:
##    t.shape(back)
##    t.stamp()
##    t.up()
##    t.goto(200,0)
##    t.shape(back)
##    t.stamp()
##    t.shape("turtle")
##    t.up()
##    t.goto(0,300)
##    t.write("성공", False, "center",(" ",20, "bold"))
##
##if coin1==1 and coin2==0:
##    t.shape(back)
##    t.stamp()
##    t.up()
##    t.goto(200,0)
##    t.shape(front)
##    t.stamp()
##    t.shape("turtle")
##    t.up()
##    t.goto(0,300)
##    t.write("실패", False, "center",(" ",20, "bold"))
##
##if coin1==0 and coin2==1:
##    t.shape(front)
##    t.stamp()
##    t.up()
##    t.goto(200,0)
##    t.shape(back)
##    t.stamp()
##    t.shape("turtle")
##    t.up()
##    t.goto(0,300)
##    t.write("실패", False, "center",(" ",20, "bold"))


##import turtle,random
##t1=turtle.Turtle()
##t2=turtle.Turtle()
##
##coin=random.randint(0,1)
##coin2
##t1.up()
##t1.goto(-150,0)
##t2.up()
##t2.goto(150,0)
##if coin==0:
##    t1.shape(front)
##else:
##    t1.shape(back)
###두번째 방법은 hide랑 터틀 2개 사용, 보충하기 코드 보면서!


##import turtle,random
##t1=turtle.Turtle()
##t2=turtle.Turtle()
##
##t1.shape("turtle")
##t2.shape("turtle")
##
##scr=turtle.Screen()
##
##front='img/front.gif'
##back='img/back.gif'
##
##scr.addshape(front)
##scr.addshape(back)
##
##coin=random.randint(0,1)
##coin2=random.randint(0,1)
##
##t1.up()
##t1.goto(-150,0)
##
##t2.up()
##t2.goto(150,0)
##
##if coin==0:
##    t1.shape(front)
##else:
##    t1.shape(back)
##    
##t1.stamp()
##
##if coin2==0:
##    t2.shape(front)
##else:
##    t2.shape(back)
##
##t2.stamp()
##t2.hideturtle()
##t2.goto(0,250)
##
##if coin==coin2:
##    t2.write("성공", False,"center",(" ",30,"bold"))
##else:
##    t2.write("실패",False,"center",(" ",30,"bold"))




##a,b=input("1번, 2번 전지 유무 입력(y/n)").split(" ")
##if a.upper()=='Y' and b.upper()=='Y':
##    print("직렬연결, 전구에 불이 켜집니다")
##else:
##    print("직렬연결: 전구에 불이 꺼집니다")
##if a.lower()=='Y' or b.lower()=='Y':
##    print("병렬연결: 전구에 불이 켜집니다")
##else:
##    print("병렬연결: 전구에 불이 꺼집니다.")
### 이거 다시 작성


##year=int(input("연도입력:"))
##if year%4==0 and year%100!=0 or year%400==0:
##    print(f"{year}년은 윤년입니다")
##else:
##    print(f"{year}년은 윤년이 아닙니다")


##a,b,c=input("a b c 값을 순서대로 입력").split(" ")
##a,b,c=int(a), int(b), int(c)
##D=b*b-4*a*c
##if D>0:
##    print("서로 다른 두 실근")
##elif D==0:
##    print("서로 다른 두 실근")
##else:
##    print("서고 다른 두 허근")



import turtle
t=turtle.Turtle()
t.shape("turtle")
s=turtle.textinput(" ", "도형을 입력하세요")

if s=="직사각형":
    w=int(turtle.textinput(" ", "가로 길이 입력"))
    h=int(turtle.textinput(" ", "세로 길이 입력"))
    t.fd(w)
    t.lt(90)
    t.fd(h)
    t.lt(90)
    t.fd(h)
    t.lt(90)
    t.fd(h)
    t.lt(90)
    t.goto(0,250)
    if w==h:
        t.write("정사각형",False,"center",("", 15,"bold"))
    else:
        t.write("직사각형",False,"center",("",15,"bold"))

elif s=="정삼각형":
    w=int(turtle.textinput("","한 변의 길이 입력"))
    t.fd(w)
    t.lt(120)
    t.fd(w)
    t.lt(120)
    t.fd(w)
    t.lt(120)
elif s=="원":
    r=int(turtle.textinput("","반지름 길이 입력:"))
    t.circle(r)
    
### 교재 문제인데 졸려서 보충해야함 아 간단한데 아 아 제발 아아아아 아아아먹자


##import turtle
##t=turtle.Turtle()
##t.shape("turtle")
##a=turtle.textinput(" ", "도형을 입력하세요")
##if a=="사각형":
##    w= int(turtle.textinput("", "가로 길이 입력"))
##
##
##    if w==h:
##          t.write("정사각형, False, "center",(" ",14, "bold"))
##    else:
##        t.
###완벽하게 보충


##import turtle
##t=turtle.Turtle()
##t.shape("turtle")
##
##x1,y1,r1=turtle.textinput(" ", "큰원 중심좌표와 반지름을 순서대로 입력").split(" ")
##x1,y1,r1=int(x1),int(y1),int(r1)
##x2,y2,r2=turtle.textinput(" ", "작은원 중심좌표와 반지름을 순서대로 입력").split(" ")
##x2,y2,r2=int(x2),int(y2),int(r2)
##
##t.penup()
##t.goto(x1,y1)
##yy1=y1-r1
##t.goto(x1,yy1)
##t.pendown()
##t.circle(r1)
##t.penup()
##t.goto(x2,y2)
##yy2=y2-r2
##t.goto(x2,yy2)
##t.pendown()
##t.circle(r2)
##dist=((x1-x2)**2+(y1-y2)**2)**0.5
##t.up()
##t.goto(0,250)
##if dist==0:
##    t.write("동심원", False,"center",(" ",20,"bold"))
##elif dist==r1-r2:
##    t.write("내접")
##elif r1-r2<dist<r1+r2:
##    t.write("두 점에서 만납니다")
##elif dist>r1+r2:
##    t.write("만나지 않고 외부에 있습니다")
##elif dist==r1+r2:
##    t.write("외접")
##else:
##    t.write("만나지 않고 내부에 있습니다")


##for i in range (1,6,1):
##    print(i,end=" ")
##print()
##for i in range(10,0,1):
##    print(i,end=" ")
##print()
### 1부터 20까지 짝수만 출력
##for i in range(2,21,2):
##    print(i,end=" ")
##print()
##for i in range(1,21,2):
##    print(i+1,end=" ")
##print()
###이해를 해야 한다.


###시그마합 계산
##sum1=0
##for i in range(1,101):
##    sum1+=i
##print(f"1부터 100까지의 합은 {sum1}이다")


###팩토리얼 계산
##n=int(input("정수를 입력:"))
##fact=1
##for a in range(1,n+1):
##      fact*=a
##print(f"{n}!은 {fact}이다")



##a=input("문자를 입력하세요")
##for n in range(1,6):
##    print(a*n)


##
##a=input("문자를 입력하세요")
##for i in range(len(a)):
##    print(a[i]+" ", end=" ") #문자열의 인덱스 사용함으로써 글자 분리하기
##
##print(" ")

##a=input("문자를 입력하세요")
##for i in a: #문자열도 하나의 시퀸스
##    print(i+" ", end=" ")



##import turtle, random
##t=turtle.Turtle()
##t.shape("turtle")
##a=random.randrange(50,201)
##for i in range(5):
##    t.fd(a)
##    t.rt(144) #음.. 각도는 생각해보도록 하자 어렵



##import turtle, random
##t = turtle.Turtle()
##c= random.randint(50, 200)
##for i in range (5):
##    t.fd(c)
##    t.rt(144)
##window = turtle.Screen()
##window.exitonclick()



##
##a=int(input("단을 입력:"))
##b=1
##for b in range(1,10):
##    print(str(a)+"X"+str(b)+"="+str(a*b))
#####보충필요
##
##a = int(input("단을 입력: "))
##if 1 <= a <= 9:
##    for i in range (1,10):
##        print( f"{a}  * {i}  = {a*i}")
##else: print("NO ")



##response='아니'
##while response=='아니':
##    response=input("엄마 다 됐어?")
##print("먹자")
