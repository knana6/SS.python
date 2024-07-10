#1~100중 20개의 값을 랜덤으로 지정하는 함수를 만든다. 저장은 리스트에 한다.
#리스트내용 출력하는 함수 만든다. 한 라인에 10개씩 출력하도록 하고 3자리 확보하여 출력.
#리스트에 저장된 내용들의 합과 평균을 출력하는 함수를 만든다. 평균은 소수점 2자리까지

import random
sum=0
a=[random.randint(1,100) for i in range (20)]
def f1(): # 랜덤리스트10개씩 2줄 만드는 함수 성공
    print(a[0:10])
    print(a[10:21])

def f2(): #합 출력하는 함수 만들려고함
    for h in range(20):
        sum+=a(h-1)
    print(sum)

f1()
f2()


#교답

##mainpart##
import random
num=[]
random_save(num,20,1,100)
print(num) #확인용
list_print(num) #리스트 내용 출력함수1
nsum,avg=sum_and_avg(num)
print("합 %s 평균 %s" %(nsum,avg))
sum_and_avg2(num)


def random_save(nlist,n,s,e):#그냥 필요한 변수 다 갖다 넣는것!
    for i in range(n):
        nlist.append(random.randint(s,e))

def list_print(nlist):
    for i in range(len(nlist)):
        print("%4s" %(nlist[i]),end=" ") #형식지정자 사용시 퍼센트와s 사이에 숫자=몇칸 여백 공간 놔둘지! 이건 4칸씩 여백있다는의미
        if (i+1)%10==0:#10번 출력했을때 줄바꿈
            print()
        
def list_prin2t(nlist):
    cnt=1 #카운트 변수 생성
    for i in nlist: # i값은 리스트의 요소값
        print("%4s" %(i), end=" ")
        if cnt%10==0:#10번 출력했을 때 줄바꿈
            print()
        cnt+=1
        
def fum_and_avg(nlist):
    nsum=0
    for i in range(len(nlist)):
        nsum+=nlist[i]
        #합 구하기 다른버전
        #for i in nlist:
        #   nsum+=1
    avg=nsum/len(nlist) #리스트 개수 수정하지 않아도 바뀌게끔, 중요 기말떄도 일반화 ㄱㄱ
    print("합 %s 평균 %.2f" %(nsum,avg)) #함수 안에서 출력



#진도: 함수
def calculate_area():
    global result #result 는 대입연산자를 사용했다고 하더라도 global 통해 전역변수가 됨
    result=3.14**2*r #함수 내부에서 값을 할당했다!! =>지역 변수!=> 출력안됨=> global ㄱ

result=0 #전역변수 .. 
r=float(input("원의 반지름")) #r은 함수에서 대입 연산자를 이용해서 값을 할당하지 않아서 전역변수다
calculate_area()
print(result)


#디폴트매개변수 강의보보보보보보
def greet(name,msg="잘 지내죠?"):
    print("안녕",name+","+msg)

def greet2(name=" ",msg="잘 지내죠?"):
    print("안녕", name+","+msg)

##def greet3(msg="잘 지내죠?",name):
##    print("안녕",name+","+msg)

##main##
greet("영희")
greet("철수","반가워")
greet2("철수","반가워")
greet2("반가워") #순서대로 name 변수에 전달된다.
greet2("영희")
greet2()


#위치인수 키워드인수
def f1(x,y,z):
    return x+y+z
def f2(x,y,z=2):
    return x+y+z

##main part##
print(f1(1,3,5))
print(f1(y=7,z=5,x=2))
print(f1(z=2,x=4,y=5))
##print(f1(z=10,20,x=2))#X. 키워드 인수 다음에 위치인수 안됨
##print(f1(5,z=10,y=2))#X, x값이 중복 저장
print(f1 z=1-,20,x=2))
print(f1(5,x=2,z=20))
print(f2(1,4))
print(f2(1,3,5))
print(f2(z=2,t=3))
print(y=3,x=2)
print(x=3,t=2))
print(f2(y=7,z=5,x=2))
pritn(f2(5,y=2))
print(f2(5,z=10,y=2))

 
#터틀 매개변수new 이해 ㄱㄱ
import turtle
t=turtle.Turtle()
t.shape("turtle")
t.circle(100) #양수이므로 반시계
turtle.textinput(" ", "다음")
t.clear()
t.circle(-100) #음수이므로 시계
turtle.textinput(" ","다음")
t.clear()
t.home()
t.circle(100,180) #extent 180 반원, 양수이므로 헤드방향
turtle.textinput(" ","다음")
t.clear()
t.home()
t.circle(100,-180) #extent -180 
turtle.textinput(" ","다음")
t.clear()
t.home()

t.circle(100,360,3)
turtle.textinput(" ","다음")
t.clear()

t.circle(100,-360,3)
turtle.textinput(" ","다음")
t.clear()

t.circle(-100,180,3)
turtle.textinput(" ","다음")
t.clear()

t.circle(-100,360,3)
turtle.textinput(" ","다음")
t.clear()

t.circle(100,steps=3)


문제
랜덤으로 삼~오각형, 원 그려지도록 한다.시작위치 다각형 크기 랜덤(50~100)
개수 10~20개 잘못되면 다시,함수이용, 각 도형은 circle의 steps 이용

def poly():
    t.circle(r,360,(random.choice(p)))

import turtle,random

t=turtle.Turtle()
t.shape("turtle")
##x=random.randint(-200,200)
##y=random.randint(-200,200)
##r=random.randint(50,100)
cnt=random.randint(10,20)

p=[1,3,4,5,6]
##t.up()
##t.goto(x,y)
##t.down()


for i in range(cnt):#원을 따로 작성해야 할듯, 0이나 1이 아난가 봐 .. .
    x=random.randint(-200,200)
    y=random.randint(-200,200)
    r=random.randint(50,100)
    
    t.up()
    t.goto(x,y)
    t.down()
    poly()



#교답교답 와 깔끔해ㅜㅜㅜ
def poly_num():
    msg=" "
    while True:
        num=int(turtle.textinput(" ",msg+"다각형 개수 입력"))
        if 10<=num<=20:
            break
        else:
            msg="10~20 사이의 수를 입력하세요.\n"
        return num

def poly_size():
    size=random.randint(50,100)
    return size
def eandom_position():
    x=randim.randint(-200,200)
    t.up()
    t.goto(x,y)
    t.down()
def draw_polygon(size):
    p=[3,4,5,6,9] #9는 원으로 사용
    s=random.choice(p)
    if s==9:
        t.circle(size)
    else:
        t.circle(size,steps==s)

##main part##
import turtle,random
t=turtle.Turtle()
t.shape("turtle")
t.speed(0)
for i in range(poly_num()):
    s=poly_sizr()
    random_position()
    draw_polygon()




#문제 BMI 계산기 만들기: 키와 몸무게 입력받고, BMI 18.5, 23, 25,30 저체중 정상 과체중 경도 고도비만
#BMI=몸무게/키X키
##main part##
#w,h=getvalue() #키몸 입력받고 반환하는 함수
#result_print(bmtfunc(w,h)) #result_print함수는 결과를 출력하는 함수
#bmifunc 함수는 bmi계산 결과 반환하는 함수


def getvalue():
    h=float(input("키 입력"))
    w=float(input("몸무게 입력"))
    return bmi

def bmifunc():
    bmi=w/h*h
##    global bmi
    print(f"BMI는 {w/h*h} 입니다")

def result_print():
    if bmi<=18.5:
        print("저체중")
    elif 8.5<bmi<22.9:
        print("정상")
    elif 23<bmi<24.9:
        print("결도비만")

bmi=w/h*h
w,h= getvalue()
result_print(bmifunc(w,h)) #보. 보


# 환전 계산기 266p

def exchange(m,c):
    if c in country_list:
        m_code=country_list.index(c)
    else:
        print("해당 국가 정보가 없습니다")
        return
    result=round(m/rate[m_code],2)
    print(m,"원은",result,unit[n_code],"입니다")
          
##main part##
country+list=['미국','중국','유럽','일본']
unit=['달러','위안','유로','엔']
rate=[1182.5,169.22,1286.74,1078.14]
money1=int(input("환전 원을 입력"))
country=input("국가 입력")
exchange(money1,country)


#문제 2차원 리스트 변환 ㄱㄱ
exchange_list=[['미국','달러'1182.5],['중국','위안',`169.22],['유럽','유로',1286.74],['일본','엔',1078/14]]]

##main part##
exchange_list=[['미국','달러'1182.5],['중국','위안',169.22],['유럽','유로',1286.74],['일본','엔',1078.14]]]
country,money=inputinfo() #국가와 금액을 입력받고 반한(없으면 다시)
exchange(country,money)

def exchange():#내가한건데 너무졸렷 정신을 잃었다
    
    if country in exchange_list:
        m_code=country_list.index(c)
    else:
        print("국가가 없으므로 다시")
        continue

#교답 교답 공부 민하야 공붛 ㅎㅎ... 밀도왜이래
def inputinfo():
    money1=int(input("환전 금액 입력"))
    while True:
        country=input("국가 입력")
        i=0
        while i<len(exchange_list): #4번 반복
            if country in exchange_list[i]:
                break #안쪽 반복문만 탈출
            i+=1
        #i값 리스트요소개수값이 동할한 경우 찾는것이 없없다는 의미
            if i ==len(exchange_list):
                print("해당국가가 없습니다. 다시 입력하세요")
            else:
                break #바깥 무한루프 탈출
        return country,money1

def exchange(c,m): #country, money 순서임
    for i in range(len(exchange_list)):
        if c in exchange_list[i]:
            break
    result=round(m/exchange_list[i][2],2) #환율은 인덱스 2번
    print(f"{m}원은 {result} {exchange_list[i][1]}입니다.")
    #단위는 인덱스 1번

##main part##
exchange_list=[['미국','달러',1182.5],['중국','위안',169.22],['유럽','유로',1286.74],['일본','엔',1078.14]]
country,money=inputinfo() #국가와 금액을 입력받고 반환(해당 국가가 없으면 다시)
exchange(country,money) #환전 결과 출력



#n각형을 그리는 함수 작성하기:다각형 개수, 다각형 모양 수정하는거 셤공부팁임 ㄱㄱ
def n_polygon(n,length):
    for i in range(n):
        t.fd(length)
        t.left(360/n)

##main part##
import turtle
t=turtle.Turtle()

for i in range(20):
    t.lt(20)
    n_polygon(6,100)




#클릭하는 곳에 사각형 그리기

def square(length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

def drawit(x,y): #클릭한 위치의 좌표값 전달:마우스 이벤트+콜백함수만들때는 (x,y)처럼 매개변수2개꼭
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.begin_fill()
    t.color("lightpink")
    square(10)
    t.end_fill()

##main part##
import turtle
t=turtle.Turtle()
s=turtle.Screen()
s.onscreenclick(drawit)# drawit는 함수 이름만 있고 괄호는 없음
#저옆에꺼 질문=클릭하면 실행되는의미?==마우스 관련된 콜백함



#한붓그리기

def draw(x,y):
    t.goto(x,y)

##main part##
import turtle
t=turtle.Turtle()
t.shape("turtle")
t.pensize(10)
s=turtle.Screen()
s.onscreenclick(draw)



#테세우스 터틀 미로 탈출 게임

def draw_maze(x,y):
    for i in range(2):
        t.penup()
        if i==1:
            t.goto(x+100,y+100)
        else:
            t.goto(x,y)
        t.pendown()
        t.forward(300)
        t.right(90)
        t.forward(300)
        t.left(90)
        t.forward(300)

def turn_left():#매개변수가 없음--이유?? 모였지 
    t.left(10)
    t.forward(10)

def turn_right():
    t.right(10)
    t.forward(10)
        
##main##
import turtle
t=turtle.Turtle()
t.shape("turtle")
s=turtle.Screen()
t.speed(0)

draw_maze(-300,200)
s.onkey(turn_left,"Left")
s.onkey(turn_right,"Right")
t.penup()
t.goto(-300,250) #터틀의 시작위치
t.pendown()
s.listen() #keyboard 이벤트를 기다리는 함수
s.mainloop() #터틀을 종료할때까지 실행하는 것! 마우스/키보드 입력 계속 처리해줌


#교재:함수는 return을 만나면 종료한다
def get_sum(start,end):
    sum=0
    for i in range(start,end+1):
        sum+=i
    print("sum=",sum)
get_sum(1,20)
get_sum(1,10)


def calculate_area(r):
    area=3.14*r**2
    return area
##c_area=calculate_area(5.0) #이렇게 한번에 써도
print(calculate_area(5.0))
##
##area_sum=calculate_area(5.0)+calculate_area(10.0)
##print(area_sum)

