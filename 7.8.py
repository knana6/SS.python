#이미지 등록이 왜 안될까..>> 피드백: 변수의 숫자를 변경하는 거는 불가능하다.. 그러니까 리스트만들기
import turtle, random
t=turtle.Turtle()
scr=turtle.Screen()
dice1='./img/dice1.gif'
dice2='./img/dice2.gif'
dice3='./img/dice3.gif'
dice4='./img/dice4.gif'
dice5='./img/dice5.gif'
dice6='./img/dice6.gif'
dice = [dice1, dice2, dice3, dice4, dice5, dice6]


scr.addshape(dice1)
scr.addshape(dice2)
scr.addshape(dice3)
scr.addshape(dice4)
scr.addshape(dice5)
scr.addshape(dice6)

c=0

while True:
    d1=random.randint(1,6)
    d2=random.randint(1,6)
    t.up()
    t.goto(-200,0)
    t.shape(dice[d1-1])
    t.goto(200,0)
    t.shape(dice[d2-1])

    if d1!=d2:
        turtle.textinput(" ","다시 합니다")
        c+=1
    else:
        t.write("f{c}번 만에 성공했다!")



#터틀 한마리
import turtle,random
scr=turtle.Screen()
t=turtle.Turtle()
dice=[]
cnt=1
for i in range(6):
    dice.append(f"img/dice{i+1}.gif")
    scr.addshape(dice[i])
while True:
    f_dice=random.randint(1,6)
    s_dice=random.randint(1,6)
    t.up()
    t.goto(-100,0)
    t.shape(dice[f_dice-1]) #리스트니까 0번부터 시작-> 랜덤값-1로 설정
    t.stamp()
    t.goto(100,0)
    t.shape(dice[s_dice-1])
    t.stamp()
    if f_dice==s_dice:
        t.ht()
        t.goto(0,250)
        t.write(f"{cnt}번에 성공")
        break
    else:
        cnt+=1
        turtle.textinput(" ","다시합니다")


#터틀 2마리: 미리 배치하기, 스탬프 안찍어도됨



#문제2.승진시험, 두과목 70점 이상 받아야 함
import random
person=1
count=0

for i in range(7):
    t1=random.randint(50,100)
    t2=random.randint(50,100)
    if t1>=70 and t2>=70:
        print(f"{person} 번은 승진 대상입니다")
        count+=1
        continue
    else:
        continue
print("f{count}명이 승진")

import random
jlist=[[random.randint(50,100) for i in range(2)] for j in range(7)]
print(jlist)
num,cnt=1,0
for i, j in jlist:
    if i>=70 and j>=70: #두과목 모두 70점 이상
        print("%s번: 승진 대상" %(num))
        cnt+=1 #승진댓ㅇ 인원수 카운
    num+=1
print("승진대상은 총 %s명" %(cnt))




#8장 함수
def print_address():
    print("서울특별시 종로구 1번지")
    print("파이썬 빌딩 7층")
    print("홍길동")
print_address("홍길동")
#실행을 시킬려면 정의를하고 호출을 해야한다


def func1(): #매개변수 없는 함수
    print("매개변수 없는 함수")
def func2(a):#매개변수 있는 함수
    print(f"a:{a} 매개변수 있는 함수")
def func3(a,b): #매개변수 있는 함수
    print(f"a,b:{a},{b} 매개변수 있는 함수")

    
## 함수 호출 시
func1() # 매개변수 없는 함수 호출, 인수 없음
func2(3) #매개변수 있는 함수 호출, 인수 있음
func3(10,20) #매개변수 개수와 인수 개수 일치


문제: 입력받은 수가 양수 음수 0인지를 출력

def func1(): #수정하기
    if n >0:
        print("양수")
    elif n <0:
        print("음수")
    else: 
        print("0")
        

def a(k):
    if int(k)>0:
        print("양수")
    elif int(k)==0:
        print("0입니다")
    else:
        print("음수")

func1()
n=int(input("수 입력")) #키보드로 입력한 값을 판별
func2(num) #num은 인수로 전달


#문제2. 정수2개 곱 출력.. 이걸 어케 표현하냐. ㅜㅜ 슬프내..
def f1(a,b):
    input(a,b)
    print(a*b)

f1(a,b)


#수정.. ㄹㅇ 어렵네
def mulit1():
    n1,n2=input("수2개입력").split(" ")
    n1,n2=int(n1),int(n2)
    print("%s X %s= %s" %(n1,n2,n1*n2))

defmulti2(n1,n2):
    print("%sX %s= %s"%(n1,n2,n1*n2))

multi1()
n1,n2=input("수2개입력").split(" ")
n1,n2=int(n1),int(n2)

multi2(n1,n2)


def calc_area(radius):
    calc_area=3.14*radius**2
    return calc_area

c_area=calc_area(5.0) #대입연산자를썻다=>어떤값을 반환한다는것
print(c_area)

sum=calc_area(5.0)+calc_area(10,0)
print(sum)


def get_input():
    return 2,3

x,y=get_input()
print(f"{x},{y}")
a=get_input()
print(f"{a}")
print(f"{a[0]},{b[0]}")

def judge(num):
    if num%2==0:
        print("짝수")
        return #반환값은 없지만 함수는 종료
    print("홀수")
def judge2(num):
    if num%2==0:
        print("짝수")
    else:
        print("홀수")
## main ##
num=int(input("자연수 입력"))
judge(num)
judge2(num)


#매개변수와 반환 4case
# 매 0 반 0 : 키보드로 입력받는 값은 함수 밖에서 처리하고, 입력한 값은 인수로 전달, 판별은 함수 내부에서, 출력값은 내부에서 하는건 아님 반환된 값은 변수에 저장하지않고 바로 화면에 출력하도록
def a(na):
    if na==0:
        print("거짓")
    else:
        print("참")

#매 X 반 0  :전달되는 값은 없음, 따라서 키보드로 입력한 값에 따라 함수 내부에서 반환, 화면출력 X, 함수 바깥에서 반환받아서 출력함      
def b():
    nb=input("숫자입력")
    if b==0:
        print("거짓")
    else:
        print("참")

#매 0 반 X : 함수는 판별해서 출력하는 것만
def c(nc):
    if nc==0:
        print("거짓")
    else:
        print("참")

# 매 X 반 X : 안에서 다 처리되도록 작성
drf d():
    nd=int(input("숫자입력"))
    if


## main part## : 매개변수 있는 경우에 전달되도록 작성
d()
nd=int(input("숫자입력")) #보충 


#사각형 그리는거북이
def square(length):
    for i in range(4):
        t.fd(length)
        t,lt(90)
#main: 코드의 흐름은 메인파트를 봐야한다
import turtle
t=turtle.Turtle()
t.shape("turtle")
square(100)
t.up()
t.gotp(-200,0)
t.down()
square(200) #보보보보


import turtle, random
def triangle(a):
    for i in range(3):
        t.fd(a)
        t.lt(120)
def square(a):
    for i in range(4):
        t.fd(a)
        t,lt(90)
def pentagon(a):
    for i in range(5):
        t.fd(a)
        t.lt(72)
def hexagon(a):
    for i in range(6):
        t.fd(a)
        t.lt(60)
n=random.randint(3,7)
if n==3:
    triangle ## 보보보보보보보 사진.. 10분뒤에 시험이다



    
