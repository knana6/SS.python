def getvalue():
     weight= float(input("사용자의 몸무게를 입력하세요(kg): "))
     height= float(input("사용자의 키를 입력하세요(m): "))
     return weight,height

def bmifunc(weight, height):
     bmi= weight/(height*height)
     return bmi

def result_print(bmi):
     if bmi<18.5:
          print("저체중입니다.")
     elif 18.5<=bmi<=22.9:
          print("정상입니다.")
     elif 23.0<=bmi<=24.9:
          print("과체중입니다.")
     elif 25.0<=bmi<=29.9:
          print("경도비만입니다.")
     else:
          print("고도비만입니다.")       
  
#main
w,h=getvalue() #키와 몸무게를 입력받고 반환하는 함수
result_print(bmifunc(w,h)) #result_print함수는 결과를 출력하는 함수
#bmifunc 함수는 BMI 계산 결과를 반환하는 함수


#문제: 키ㅗ드 l을 누르면 서눈 길이 이력ㅊ(초기갓은 10, 10~100 사이로 제한, 잘못시 다시)
# s 펜굵기 이력(1~10사이제한)
# a 각도이력( 1~360 사이제한)
# ㅏㅇ향키 선그리기 (Up,Down: 앞뒤로 이동)
# 마우스로 터틀위치 ㅕㄴ경가능, 위치ㅕㄴ경시 선이 그려지면안됨

#추가ㅏ 왼쪽방향키왼쪽10도회전

def forward_turtle(): #매개 필요엄음
    t.forward(length) #length 전역

def backward_turtle():
    t.backward(length)

def pos_move(x,y):
    t.up() # 선 안그려지게
    t.goto(x,y)
    t.down()

def input_line():
    
##    l=input("길이")
##    return l
    global length #지역->전역
    msg=""
    while True:
        length=int(turtle.textinput("",msg+"선길이")) #length의 양을 할당, 지역임. 전역으로 만들어야
        if 10<=length<=100:
            break
        else:
            msg="10~100 사이로 하자 \n"
    s.listen()

def input_ps():
##    s=input("펜굵기")
##    return s
    msg=" "
    while True:
        ps=int(turtle.textinput("",msg+"선굵기")) #length의 양을 할당, 지역임. 전역으로 만들어야
        if 1<=ps<=10:
            break
        else:
            msg="1~10 사이로 하자 \n"
    t.width(ps) #선 굵기 설정
    s.listen() #다시 스크린 객체에 포커스 맞추기

def input_angle():
##    a=input("각도")
##    return a
    msg=" "
    while True:
        ag=int(turtle.textinput("",msg+"각도")) #length의 양을 할당, 지역임. 전역으로 만들어야
        if 1<=ag<=10:
            break
        else:
            msg="0~360 사이로 하자 \n"
    t.left(ag) #seth 써도됨
    s.listen() #다시 스크린 객체에 포커스 맞추기

def left_click():
    t.lt(10)

def right_click():
    t.rt(10)

#main part
import turtle
t=turtle.Turtle()
t.shape("turtle")
s=turtle.Screen()
length=10
s.onkey(input_line,"l")
s.onkey(input_ps,"s")
s.onkey(input_angle,"a")
s.onkey(forward_turtle,"Up")
s.onkey(backward_turtle,"Down")

s.onkey(right_click,"Right")
s.onkey(left_click,"Left")
s.onhey(t.home,"h")  #매개변수가 없는 함수인 경우 직접 콜백함수로 등록가능

s.onscreenclick(pos_move)
s.listen()
s.mainloop()



#이차함수 그래프 그리기
def f(x):
    return x**2+1

#main#
import turtle
t=turtle.Turtle()
t.shape("turtle")

t.goto(200,0)
t.goto(0,0)
t.goto(0,200)
t.goto(0,0)

for x in range(150):
    t.goto(x,int(0.01*f(x))) #0.01 곱해준이유: 그림상 완만하게 커지는게 보기편해서




#재귀호출은 탈출조건이 있어야 한당

def fact(n):
    if n==1:
        return 1  #예를들어 1나오면 반환되는 곳은 fact(1)로 반환됨. 순서대로 ㅇㅇ
    else:
        return n*fact(n-1) #반복문 대신 재귀함수쓰기

## main part ##
n=int(input("정수입력"))
f=fact(n)
print(f"{n}!은 {f}이다:")



문제: 10부터 1까지출력 프로그램, 재귀함수 이용

def rec_num(n):

    if n<=0:
        return("양수를 입력해주라")
    else:
        print(n)
        return(n-1)

##mainpart
rec_num(10)

def rec_num(n):
    if n>0: #탈출조건
        print ("%3s" %(n),end=" ") #자기자신을 호출하는 위치가 중요하다
        rec_num(n-1) # 이 2줄 자리 바꾸면 출력이 달라진다

rec_num(10)

#문제: 1~10 출력

def num(n):
    if n<11:
        print("%3s" %(n), end=" ")
        num(n+1)

num(1)


phone_book={'홍길동':'010-1234-5678','강감찬':'010-1111-2222',
            '이순신':'010-2222-3333','홍길동':'010-1231-8765'}
#딕셔너리 생성과 초기화 역할, 키값이 중복되었다면 하나만 남게 됨, 근데 랜덤임(어떤게 남을지 모름)
#list 와 같이 값이 변경될 수 있는 자료형은 key로 사용불가
#key 를 입력하면 value 값이 나온다, 대괄호에 킷값 사용 !!
print(phone_book['홍길동']) #인덱스 사용이 아닌 카값으로 접근
print(phone_book)
phone_book2={} #공백 딕셔너리
phone_book2['홍길동']='010-1234-5678' #항목 추가
phone_book2['홍길동']='010-1234-0000' #키값 중복저장 불가, value 변경(수정)
phone_book2['강감찬']='010-1111-2222'
phone_book2['이순신']='010-3333-4444'
print(phone_book2)

phone_book={'홍길동':'010-1234-5678','강감찬':'010-1111-2222',
            '이순신':'010-2222-3333'}
print(phone_book.keys()) #출력시 값들이 쭉 나열되어있음. 주의 대괄호 있다고 list 아님.
for key in sorted(phone_book.keys()): #오름차순 정렬이 되.>> ['강','이','홍']
    print(key, phone_book[key]) #강감찬부터 들어감, 대괄호 썼다고 해서 리스트 아님
print(phone_book.values()) #>> dict_values(["","",""})
print(phone_book.items()) #key 와 walue 값을 튜플 형채로 출력(소괄호)
#>> dict_items([("홍길동","010-1234-5678).(),()}

del phone_book["홍길동"]4
# del phone_nppk{"홍길순"} #해당키가 없으면 에러
print(phone_book)
print(phone_book.pop("이순신"))
#
print(phone_book()) #에러
print(phone_=_book.pop("강감천")) #딕셔너리에 없는 키 에러
phone_book.clear()
print(phone_book)

items={'커피':7,'펜':3,'종이컵':10,'우유':5,'콜라':4,'라면':11}
print("판매 전 재고",items)
sell=input("판매한 물건을 입력하세요:")
if sell in items.keys(): #if sell in items:
    items[sell]-=1 #items[sell]=items[sell]-1
else:
    print("판매제품이 아닙니다")
print("판매 후 재고",items)


#딕셔너리와 반복문의 궁합
items={'커피':7,'펜':3,'종이컵':10,'우유':5,'콜라':4,'라면':11}
for k in items:
    print(k,end=" ")
print()
for k in items.keys():
    print(k,end=" ")
print()
for v in items.values():#value 값들만 반복문을 이용해서 사용하겠다
    print(v,end=" ")
print()
for k in items.items(): #key와 value의 쌍을 변환(튜플)
    print(k,k[0],k[1],end=" ") #튜플의 각 요소를 index로 접근할 수 있다. (....어렵네)
print()
for k,v in items.items(): #변수 2개 쓰면 key와 value를 각각 k,v에 저장
    print(k,",",v)

list1=[]#,list()
tu1=()#,tuple()  공백 튜플 만들때 소괄호 이용, 튜릉리아는 함수 이용해 소괄호 생성가능
dic1={}#,dict() 
s1=set() #{} (X) 공집합이 아니라 공백 딕셔너리. 집합은 set 이라는 함수 이용해서 공집합 만듦
#set()=공집
print(list1,type(list1))
print(tu1,type(tu1))
print(dic1,type(dic1))
print(s1,type(s1))

s1={1,1,2,3,5,5,5}
print(s1) #원소가 하나로 되어있으면 집합자료형
s1.add(6)
s1.add(7)
s1.add(2) #집합은 중복을 허용하지 않음
print(s1)
print(s1[0]) #순서가 없기에 인덱싱 불가
