##x=100
##y=200
##sum1=x+y
##print(sum1)
##
##num=1
##num="1"
##num=1.0
##

###출력연습
##x,y= 100,200
##sum1= x+y
##print(x,"과", y, "의 합은", sum1, "입니다.")
##print("{}과 {}의 합은 {}입니다.", format(x,y,sum1))
##print("%s과 %s의 합은 %s 입니다. "(x,y,sum1))
##print(str(x)+"과 "+str(y)+"의 합은 "+str(sum1)+"입니다.")
##      

##name=input("이름을 입력하세요.")
##print(name, "씨, 안녕하세요.")
##print("파이썬에 호신 것을 환영합니다.")

##num1=input("수1을 입력:")
##num2=input("수2를 입력:")
##print(num1+num2)

##x=int(input("정수1입력"))
##y=int(input("정수2입력"))
##print(x,"+",y,"=",x+y)
###format 형식 뺄셈
##print("{} - {} = {}".format(x,y,x-y))
### % 형태의 곱셈
##print("%s * %s = %s" %(x,y,x*y))
### f-string 나눗셈
##print(f"{x} / {y} = {x/y}")


#이건 꼭 복습해야 한다아아
##year=1
##name=kim
##major='computer'
##grade=4.3
##avg=3.7
##print("학년:", year, "이름:", name))
##print(" 학년{}, 이름:,{}".format(year, name))
##print("학년: {0}, 이름:{1}".format(year,name))
##print("이름:{1}, 학년:{0}".format(year.name))

a=10
b=30
c=int(input("숫자를 입력하세요"))
d=a+b+c

print(a, "+", b, "+", c,"=", d)
print("{} + {} + {} = {}".format(a,b,c,d))
print("%s + %s + %s = %s" %(a,b,c,d))
print(f"{a} + {b} + {c} = {d}")
print(str(a)+" + "+str(b)+"+"+str(c)+'='+str(d))
