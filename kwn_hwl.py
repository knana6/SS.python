#202421405 


import turtle #터틀 모듈 호출
import random


t=turtle.Turtle() #t라는 이름으로 turtle 객체 설정
t.shape("turtle") #터틀 모양 설정
a=turtle.textinput("가위바위보", "가위, 바위, 보 중 하나를 입력하세요") #사용자 입력 받기


if a not in ["가위","바위","보"]: 
    t.write("잘못 입력하였습니다",False, "center",(" ", 20, "normal")) #잘못 입력했을 때 출력


else:     
    t.penup() 
    t.goto(-200,200)
    t.write(a ,False,"center",(" ",40,"normal")) #사용자 입력 값 출력


    t.penup()
    computer=random.randint(1,3) # 컴퓨터 값 1~3 랜덤 지정
    t.goto(200,200)


    if computer==1:
        t.write("가위",False, "center",(" ", 40, "normal"))
    if computer==2:
        t.write("바위",False, "center",(" ", 40, "normal"))
    if computer==3:
        t.write("보",False, "center",(" ", 40, "normal")) # 컴퓨터 값 출력


    t.penup()
    t.goto(0,0)
    if a=="가위"and computer==1:
        t.write("무승부", False,"center", (" ", 20, "normal"))
    if a=="바위"and computer==2:
        t.write("무승부", False,"center", (" ", 20, "normal"))
    if a=="보"and computer==3:
        t.write("무승부", False,"center", (" ", 20, "normal")) # 무승부 결과 출력
    
    
    
    if a=="가위"and computer==2:
        t.write("컴퓨터 승리", False,"center", (" ", 20, "normal"))
    if a=="바위"and computer==3:
        t.write("컴퓨터 승리", False,"center", (" ", 20, "normal"))
    if a=="보"and computer==1:
        t.write("컴퓨터 승리", False,"center", (" ", 20, "normal")) # 컴퓨터 승리 결과 출력
    
    
    
    if a=="가위"and computer==3:
        t.write("나의 승리", False,"center", (" ", 20, "normal"))
    if a=="바위"and computer==1:
        t.write("나의 승리", False,"center", (" ", 20, "normal"))
    if a=="보"and computer==2:
        t.write("나의 승리", False,"center", (" ", 20, "normal")) # 사용자 승리 결과 출력

