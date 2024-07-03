###a=input("세 수 입력").split(" ")
##a=input("첫번째수")
##b=input("두번째수")
##c=input("세번째수")
##print(a+b+c)
##print(a-b-c)
##print(a*b*c)
##print(a/b)
##print(a%b)


##
##a=int(input("돈의 액수 입력"))
##print("만원짜리", a//10000, "장")
##print("천원짜리", a//1000, "장")
##print("백원짜리", a//100, "장")
##print("십원짜리", a//10, "개")
### 보충할 점: 형식 계산자를 안썼다는거? 그래도 복습이니까)


##
##r=float(input("반지름의 길이 입력"))
##h=float(input("높이 입력"))
##v=3.141592*(r**2)*h
##print("원기둥의 부피는", round(v,2))
##print("원기둥의 부피는"+str(round(v,2)))
##print("원기둥의 부피는{:.2f}".format(v))
##print("원기둥의 부피는 %.2f" %(v))
##print(f"원기둥의 부피는 {v:.2f}")


##x=10
##y=10.0
##z='string'
##w= True
##print(x,type(x))
##print(y,type(y))
##print(z,type(z))
##print(w,type(w))


##print( 'she said "hi"')
##print( 'she said "hi"')
##print( 'she/'s a /"good/" student')
##print( )
##print( 'she said "hi"')
##       -> 보충해야해 어쩃든


####슬라이싱 연습
##s="Next time I fall in love"
####print(a[8:4:-1])
####print(a[-9:-13:-1])
##print(s[:9]) #start 생략시 처음부터
##print(s[10:len(s)]) #end 값을 문자열 길이 겂으로
##print(s[10:999]) #end 값을 엄청 큰 값으로
##print(s[:]) #문자열 전체
##print(s[8::-1])
##print(s[-1::-1]) #문자열 전체 거꾸로
##print(s[-4:]) #love 출력


### 소금의 양 물의 양 입력받도 소숫점1자리까지 나오도록
##a= int(input("소금의 양"))
##b=int(input("물의 양"))
##c=a/(a+b)*100
##print("소금물의 농도", round(c,1))
#####이거 왜 안되는지 잘 모르겠어요


##print("안녕하세요")
##name=input("이름")
##print("만나서 반갑습니다." +name+ "님")
##print(name+"님 이름의 길이는 다음와 같군요", end=" ")
##


##import turtle
##t=turtle.Turtle()
##t.shape("turtle")
##s=turtle.textprint(" ", "이름을 입력허세요")
##t.write(안녕하세요 +s+ "씨, 터틀 입사드립니다")
##
##t.lt(90)
##t.fd(100)
##
##t.lt(90)
##t.fd(100)
##
##t.lt(90)
##t.fd(100)
##
##t.lt(90)
##t.fd(100) #약간망한거 .. 아 졸려ㅓ ..ㅋㅋ



##import turtle
##t=turtle.Turtle()
##t.shape("turtle")
##s=turtle.textinput("문자열 입력", " 내용을 입력하세요.")
##t.up()
##t.goto(0,300)
##t.down()
##t.write(s, True, "left", (" ", 25, "bold"))
##t.up()
##t.goto(0,250)
##t.down()
##t.write(s, True, "center", (" ", 25, "normal"))
##t.up()
##t.goto(0,200)
##t.down()
##t.write(s, True, "right", (" ",25, "bold"))
##t.up()
##t.goto(0,150)
##t.down()
##t.write(s,False, "center", (" ", 25, "bold"))
### 이탈릭이 없는데 파이썬 다시 깔아야 하나?
##없는게 아니라 대소문자 구분 안해서 그런거임


##import turtle
##t=turtle.Turtle()
##t.shape("turtle")
##a=int(turtle.textinput(" ", "반지름입력"))
##t.up()
##t.goto(0.-a)
##t.down()
##t.circle(a)
##t.up()
##b= str(a)+"는 입력한 반지름값"
##t.write(fb, True, "center", (" " , 20, "bold"))
### 글자 쓰는거 필기를 보여달라고 말씀드리기



### 터틀 그래픽에서 좌표 입력받고 직선을 그리고 거북이 이동 없이 좌표값 출력하고 (0,250)에 직선길이 출력
##import turtle
##t=turtle.Turtle()
##a,b=turtle.textinput("첫번째 좌표", "x1, y1 입력").split(" ")
##c,d=turtle.textinput("두번째 좌표", "x2, y2 입력").split(" ")
##a, b, c, d= int(a), int(b),int(c), int(d)
##q=((c-a)**2 + (d-b)**2)**0.5
##t.up()
##t.goto(a,b)
##t.write(f"({a},{b})", False, "center", ( " ",10, "bold")) #f-string 이용
##t.down()
##t.goto(c,d)
##t.write(f"({c},{d})", False, "center", (" ", 10, "bold"))
##t.up()
##t.goto(0,250)
##t.write("두 점 사이의 거리는" +str(q)+"입니다", True, "center", (" ",20, "normal"))


##a=int(input("투입한 돈"))
##b=int(input("물건 가격"))
##c=a-b
##print("거스름돈 "+ str(c))
##print("500원"+ str(c//500)+ "개")
##c= c%500
##print("100원"+str(c//100)+"개")


money=int(input("투입한 돈"))
price=int(input("물건 가격"))

change=money-price
print("거스름돈", change)
coin500=change//500
change=change%500

coin100=change//100
print("500원",coin500)
print("100원",coin100)
