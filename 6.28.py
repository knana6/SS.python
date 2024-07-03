##import turtle
##t=turtle.Turtle()
##t.shape("turtle")
##a=turtle.textinput("이름 입력", "이름을 \n입력하세요")
##t.up()
##t.goto(0,250)
##t.write(a+"님 안녕하세요 반갑습니다!", False, "center", (" ", 20, "bold"))
##t.goto(0,0)
##t.down()
##t.setheading(90)
##t.fd(100)
##t.left(90)
##t.fd(100)
##t.left(90)
##t.fd(100)
##t.left(90)
##t.fd(100)
##t.left(90)
##t.up()
##t.goto(-50,50)
##t.down()
##


##
##a=input("암호를 만들 문자를 입력하세요")
##al=a[-1::-1]
##al2=a[0]+a[-2:0:-1]+a[-1]
##print(al)
##print(al2)
###아 길이를 모르면 그냥 비우놔도 되는구나..그리고 문자는 문자니까 str 안해줘도됨


##
##import time
##now=time.time()
##thisYear=int(1970+now//(365*24*3600))
##print("올해는 %s 년 입니다."%(thisYear))
##age=int(input("당신의 나이를 입력하세요"))
##print("2050년에는 %s 살이시군요."%(age+2050-thisYear))


##score=int(input("당신의 점수는"))
##if score>=60:
##    print("축하합니다")
##    print("합격입니다")
##else:
##    print("다음 \n기회에 \n만났으면 \n좋겠습니다")
##print("수고하셨습니다")


##a=3.1415926535
##print("소숫점3자리" ,round(a,3))
##print("소숫점3자리 {:.3f}".format(a))
##print("소숫점3자리 %.3f" %(a))
##print(f"소숫점3자리 {a:.3f}")


##print("소숫점 2자리" ,round(a,2))
##print("소숫점 2자리 {:.2f}".format(a))
##print("소숫점 2자리 %2f" %(a))
##print(f"소숫점 2자리 {a,2f}")


##
##num=int(input("수 입력"))
##if num % 2 == 0:
##    print("짝수")
##else:
##    print(:홀수")


##a=float(input("당신의 학점은?"))
##b=int(input("당신의 학년은?"))
##if a<3.5 and b>=2:
##    print("이번 학기도 수고했어요")
##
##if product="참기름" and cnt!=0:
##if score>=210 and obj=="Pass":
##elif 60<=score<=90:
##else:
##if choice==1 or choice==3:
### if choice ==1 or 3 으로 작성하지 않도록 주의합시다


##a=float(input("당신의 성적은"))
##if 100>=a>=90:
##    print("A")
##elif 80<=a<90:
##    print("B")
##elif 70<=a<80:
##    print("C")
##elif 60<=a<70:
##    print("D")
##elif a<=59:
##    print("F")
##else: print("잘못 입력했습니다")

##
##num=int(input("정수 입력:"))
##if num>0:
##    print("양수입니다")
##else:
##    if num<0:
##        print("음수입니다:)
##    else:
##        print("0입니다")

##
##a,b,c=input("세 변의 길이 입력(a,b,c순서)").split(" ")
##a,b,c=int(a), int(b), int(c)
##if a**2+ b**2 == c**2:
##    print("직각삼각형)
##else:
##    print("직각삼각형이 아니다")


#터틀의 정수판별
##import turtle
##t=turtle.Turtle()
##t.shape("turtle")
##
##t.penup()
##t.goto(100,100)
##t.write(" 입력된 정수는 양의 정수")
##t.goto(100,0)
##t.write("입력된 정수는 0입니다")
##t.goto(100,-100)
##t.write("입력된 정수는 음의 정수입니다")
##
##t.goto(0,0)
##t.pendown()
##n=int(turtle.textinput(" ", "숫자를 입력하세요"))
##
##if n>0:
##    t.goto(100,100)
##if n==0:
##    t.goto(100,0)
##if n<0:
##    t.goto(100,-100)
#이걸 다시 해야 한닷



##import random
##print("주민등록번호의 성별 정보 번호를 생성합니다.")
####gender=random.randint(1,4)
####gender=random.randrange(1,5)
####gender=random.randrange(1,5,1)
##gender=random.randrange(4)+1
##print("생성번호 %s" %(gender))
##if gender ==1 or gender ==3:
##    print("남성")
##else:
##    print("여성")



