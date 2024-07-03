##import turtle
##t=turtle.Turtle()
##t.shape("turtle")
##radius= int(input("원의 반지름을 입력하세요"))
##color=input("원의 색깔 입력")
##t.color(color)
##t.begin_fill()
##t.circle(radius)
##t.end_fill()


##import turtle
##t=turtle.Turtle()
##t.shape("turtle")
##a=int(input("길이 입력"))
##b=input("색상 입력")
##t.color(b)
##t.begin_fill()
####t.triangle(a)
##t.fd(a)
##t.lt(120)
##t.fd(a)
##t.lt(120)
##t.fd(a)
##t.lt(120)
##
##t.end_fill()



##import turtle
##t=turtle.Turtle()
##t.shape("turtle")
##radius=int(input("길이 입력"))
##b=input("색상 입력")
##t.color(b)
##t.begin_fill()
##t.circle(radius)
##t.end_fill()
##
##t.up()
##t.goto(100,100)
##t.down()
##t.begin_fill()
##t.circle(radius+20)
##t.end_fill()
##
##t.up()
##t.goto(200,200)
##t.down()
##t.begin_fill()
##t.circle(radius+40)
##t.end_fill()
####
####->왜 두개밖에 안그려지지??

##
##sec=int(input("측정 시간(초) 입력"))
##distance=340*sec
##print(" 자신의 위치에서 번개가 친 장소까지의 거리=",distance,"m")
##print("자신의 위치에서 번개까지의 거리{}".format(distance))
##print("자신의 위치에서 번개까지의 거리%s m"%(distance))
##print(f"자신의 위치에서 번개까지의 거리{distance}m")
###print("자신의 위치에서 번개까지의 거리" ,+str(distance)+,"m")
##print("자신의 위치에서 번개까지의 거리" + str(distance) + "m")
###얘도 다시 봐야함 .


##a=input("문자 입력")
##b=int(input("숫자 입력"))
##print(a*b)


###따로따로 입력받는 방법
##x=int(input("첫번째수"))
##y=int(input("두번째수"))
##z=int(input("세번째수"))
##avg=(x+y+z/3)
####print("평균=", avg)


###같이 입력받는 방법:스트링 하나 더 보충해야해
##x,y,z=input("수 3개 입력").split(" ")
##x,y,z=int(x),int(y),int(z)
##avg=(x+y+z)/3
##print("평균",round(avg,2))
##print("평균: {:.2f} ".format(avg))
##print("평균 : %.2f" %(avg))
##print(f"평균: {avg:.2f}")


###화씨온도를 입력받아서 섭씨온도로 변환하여 출력하기
##f=int(input("화씨 온도를 입력하세요"))
##c=(f-32)*5/9
##print("섭씨 온도", round(c,2))
##print("섭씨 온도: {:.2f}" .format(c))
##print("섭씨 온도: %.2f" %(c))
##print(f"섭씨 온도: {c:.2f}")
##print("섭씨 온도:" +str(round(c,2)))


##x1, y1 =input("x1,y1 좌표 입력:").split(" ")
##x1,y1 =int(x1), int(y1)
##x2, y2 = input("x2, y2 좌표 입력:").split(" ")
##x2, y2 = int(x2), int(y2)
##distance= ((x2-x1)**2+ (y2-y1)**2)**0.5
##print(f"두 점 사이의 거리 : {distance:.2f}")


### 각도바꾸기 거북이의 머리 각도바꾸기
##import turtle
##t= turtle.Turtle()
##t.shape("turtle")
##t.goto(0,0)
##t.setheading(45)
##t.fd(141.4)

##
##t.up()
##t.goto(0,0)
##t.down()
##t.seth(0)
##t.fd(100)
##t.seth(90)
##t.fd(100)


### 터틀여러마리...?
##import turtle
##t1=turtle.Turtle()
##t1.shape("turtle")
##t1.color("red")
##t. seth(45)
##t.fd(141.4)
##
##t2=turtle.Turtle()
##t2.shape("turtle")
##t2.color("purple")
##t2.fd(100)
##t2.seth(90)
##t2.fd(100)##
##t.up()
##t.goto(0,0)
##t.down()
##t.seth(0)
##t.fd(100)
##t.seth(90)
##t.fd(100)


### 터틀여러마리...?
##import turtle
##t1=turtle.Turtle()
##t1.shape("turtle")
##t1.color("red")
##t. seth(45)
##t.fd(141.4)
##
##t2=turtle.Turtle()
##t2.shape("turtle")
##t2.color("purple")
##t2.fd(100)
##t2.seth(90)
##t2.fd(100)##
##t.up()
##t.goto(0,0)
##t.down()
##t.seth(0)
##t.fd(100)
##t.seth(90)
##t.fd(100)


### 터틀여러마리...?
##import turtle
##t1=turtle.Turtle()
##t1.shape("turtle")
##t1.color("red")
##t. seth(45)
##t.fd(141.4)
##
##t2=turtle.Turtle()
##t2.shape("turtle")
##t2.color("purple")
##t2.fd(100)
##t2.seth(90)
##t2.fd(100)


### time 모듈 이용
##import time
##
##fseconds=time.time()
##print(fseconds)
##total_sec= int(fseconds)
##total_min=total_sec//60
##minute= total_min%60
##total_hour=total_min//60
##hour=total_hour%24+9 # 그리니치 시간에서 한국이 9시간 빠르다
##print(f"현재 한국 시간: {hour}시 {minute}분")


# 계산대 프로그램
money=int(input("투입한 돈"))
price=int(input("물건가격"))
change=money-price
print("거스름돈",change)
coin500s=change//500
change%=500
coin100s=change//100
print(f"500원 동전개수 : {coin500s}")
print(f"100원 동전개수 : {coin100s}")
