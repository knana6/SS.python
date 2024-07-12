s1={10,20,30,40,70,60,50}
s1.discard(80) # 해당 원소가 없어도 에러가 나지 않음
s1.discard(30)
print(s1)
if 80 in s1: # 해당 원소가 없으면 에러가 나기 떄문에  if  와 같이 사용
    s1.remove(80)
s1.remove(40)#해당 원소가 있기 때문에 에러안남
print(s1)
s1.clear()#전체 원소 삭제
print(s1)#공집합set() 출력


#가위바위보게임+ 잘못 입력 판단+ 비겼으면 다시. 내코드
def match(c,m):
    while True:
        if c==m:
            return "비겼습니다, 다시 입력해주세요"
            mine=input("가위 바위 보 중 하나 다시 입력")
##            continue
        elif match_table[c]==m:
            return "졌습니다"
            break
        else:
            return "이겼습니다"
            break
        

## main part ##
import random
rps_dic={1:"가위",2:"바위",3:"보"}
match_table={"가위":"보","바위":"가위","보":"바위"} #컴이 이겼을때의 경우들
com=rps_dic[random.randint(1,3)] #킷값을 랜덤으로 결정, 랜덤으로 결정된 킷값에 해당되는 value 값을 com에 입력
mine=input("가위 바위 보 중 하나")
result=match(com,mine)

if mine not in rps_dic:
    mine=input("가위 바위 보 중 하나 다시 입력")
    result=match(com,mine)

        
print(result)


#교답(보)

#힘수는 그대로
#main part#
import random
rps_dic={1:"가위",2:"바위",3:"보"}
match_table={"가위":"보","바위":"가위","보":"바위"}
whlle True:
    com=rps_dic[random.randiant(1,3)]
    print(com) #확인용
    qhile True:
        mine=input("가위 바위 보 중 하나 입력")
        if mine in rps_dic.values(): #가바보중에 있는지 확인
            break #안쪽 무한루프 탈출
        else:
            print("잘못입력")
    result=match(com,mine)
    print(result)
    if result=="비겼습니다":
        print("다시합니다")
    else:
        break #바깥 무한루프 탈출



행성까지의 여행 시간
planet_dict={"수성":91700000,"금성":4140000,"화성":78400000,"목성":628700000,"토성":1277400000,"천왕성":275400000,"해왕성":4347400000}
planet=input("행성 이름")
speed=int(input("이동 속도"))
distance=planet_dict[planrt]
time=distance/speed
year=int(time)//(365*24)
month=int(time-(year*365*24)//(30*24))
day=int(time-(year*365*24)-(month*30*24)-(day*24))
hour=int(time-(year*365*24)-(month*30*24)-(day*24))
print(time)
print(year)
        


멘델의 유전법칙 시뮬레이션
def make_descendant():
    h1=random.randrange(0.2)
    h2= #보보보


def count_descendant(d):
    d_dict={}
    for n in d:
        if n in d_dict:
            d_dict[n]+=1
        else:
            d_dict[n]=1 #n은 'RR;, ;Rr','rR','rr'증 하자. 1은 value
    print(d_dict)
    cal_rate(d_dict)

def cal_rate(d):
    rate=(d['RR']+d['Rr']+d['rR']}/d['rr']
    print(rate,":1")

#main part#\
import random
descendant=[]
for n in range(100):
    make_descendant()
count_descendant(descendant)
    
                    


#튜링상 수상자
awards=[]
awards.append({'이름':'팀 버너스리','수상년도':2016,'국적':'영국','대표업적':'월드 와이드 웹의 하이퍼텍스트 시스템을 고안하여 개발'})

awards.append({'이름':'리처드 해밍','수상년도':1968,'국적':'미국','대표업적':'오류 검출 부호 및 오류 정정 부호'})

awards.append({'이름':'에츠허르 데이크스트라','수상년도':1972,'국적':'네덜란드','대표업적':'프로그래밍 언어 연구.데이크스트라 알고리즘'})

awards.append({'이름':'데니스 라키','수상년도':1983,'국적':'미국','대표업적':'유닉스 운영 체제 개발. c언어 개발'})

for award in awards:#전체출력
    print(award) #딕셔너리

print("==수상자 명단==")
for award in awards: #award는 딕셔너리
    print(award['이름'])#'이름'키에 해당하는 value 출력

print()
print("==수상자 명단과 수상년도==")
for award in awards: 
    if award['수상년도']<=1990: #'수상년도'키에 해당하는 value<=1990년
        print(award['이름'],award['수상년도'])

print()
print("==수상자 국가==")
nationality=set() #공집합 생성
for award in awards:
    nationality.add(award['국적']) #같은 값이 있어도 중복은 제거(집합이므로)

print(nationality)



문제) 학생들의 어떤 과목 점수를 딕셔너리로 저장. 학생 20명, key로 학번(std1~std20) 사용, value로는 과목 점수(랜덤 0~100) 저장
{"std1':75,"std2";97,...}
 점수가 70점 이상인 학생의 학번과 점수 출력, 70점 이상의 학생 몇명인지 출력. 전체 평균 소숫점 2자리까지 출력

import random
s=[]

for i in range(20):
    n=random.randint(0,100)
    s.append(f"std{i+1}:{n}",) #이케 해도 되는지 질문-> 문자열 표현 방법은 4가지 모두 가능하다, 콤마 표기법은 print()에서만 되구


#교답
import random
jdic={}
for i in range (1,21):
    jdic[f"str{i}"]=random.randint(0.100)
print(jdic)
cnt, sum1=0.0\fot i,f in jdic.items(): #i에는 키값(학번). j에는 value 값(점수)
    sum1+=j
    if j>=70:
        print(f"{i};{j}") #i는 학번
        cnt+=1
print(cnt)
print(sum1/len(jdic) #보보
print(s)




#문제) {'세제','비누','락스','칫솔','샴푸','치약','린스','로션'} 집합 이용
#핀매실적 42ㅓㅁ 이상 제품은 비누 칫솔 샴푸 치약 로션
#고객평가 4범이상 샴푸 린스 치약

#둘다 4점 이상-우수 제품
# 둘다 4점 미안

pro={'세제','비누','락스','칫솔','샴푸','치약','린스','로션'}
a={'비누','칫솔','샴푸','치약','로션'}
b={'샴푸','린스','치약'}
good=set()

##내답 집합 연산을 안씀
##if n in a and n in b:
##    good.add(n)
##print(good)

교답 집합 연산자 씀
good= a&b #교집합을 구하면 둘 다 4점 이상, 우수제품
#good=sale.intersection(b)
print("우수제품", good)
ssale=pro-(a | b) #4점이상 합집합 구하고 전체에서 뺴줌(차집합)
#ssale=pro.difference(a.union(b))
print("판매중지 예정 제품", ssale)


문제 학생수 34명, 국영수 시험 봄
 아이디 stud1,...,stud34
과목별 점수 0~100 랜덤값 저장
key는 아이디어, value는 [국어 영어 수학]
이걸 딕셔너리로 만든다
영어점수중 최고점을 구해서 풀력
 학생 점수의 평균이 가장 높은 학생의 아이디와 평균값(정수) 출력


내답: ㅇ ㅏ ㄹㅇ..ㅋㅋ
import random
s=[]

for i in range(34):
    s[std[i+1],]="random.randint(0,100)" #딕셔너리 추가하는 방법. 왜안될까 ㄹㅇ
print(s)


#교답 : 왜 내가 한 딕셔너리는 모양이 이상한지 생각.. 
import random
classdic={}
for i in range(34):
    classdic[f"stud{i+1}"]=[random.randint(0.100) for i in range(3)] #여기서 f스트링 쓰는이유?
print(classdic)

ejumsu=[] #영어 점수만 저장할 리스트
for i, j, k in classdic.values(): #i는 국어, j는 영어, k는 수학 점수
    ejumsu.append(j) #영어 점수만 리스트에 저장
print(f"영어 점수 최고점:{max(ejumsu)}")

avglist=[]
for k,e,m in classdic.values():
    avg=(k+e+m)//3
    avglist.append(avg) #평균값을 리스트에 저장(학생수만큼)

for i, j in classdic.items():
    sum1=0
    for k in j:
        sum1+=k
    if sum1//len(j)==max(avglist):
        print(f"아이디:{i}, 평균:{sum1//len(j)}") #같으면 출력


사고자 할 물품 5개 입력받아 리스트에 저장. 이미 있는 품목이면 다시 입력,
구매한 품목 3개 저장(key는 번호 (0,1,2),value는 입력값)
사고자 하는 품목 리스트와 구매한 품목 딕셔너리를 이용해 아직 구매하지 않은 품목 출력

#내답,딕셔너리와 하루만에 친해지기 ㄱㄱ
buy=[]
while len(buy)<6:
    a=input("구매할 물건 입력")
    buy.append(a)
    if a in buy():
        continue
bought={}
bought.i


#교답
buylist=[]
n=0
while n<5:
    buyitem=input("사고자 하는 품목 입력")
    if buyitem not in buylist:
        buylist.append(buyitem)
        n+=1
    else:
        print("이미 있는  품목입니다")
print(buylist)

buydic={}
n=0
while n<3:
    buyitem=input("구매한 품목 입력")
    if buyitem not in buydic.values():
        buydic[n]=buyitem
        n+=1
    else:
        print("이미 구매 내역에 있습니다")
print(buydic)

print("아직 구매하지 않은 품목")
buyitems=set(buylist)-set(buydic.values()) #차집합 이용,  list를 집합으로 바꾼 다음에 집합과 관련된 연산자 사용
print(buyitems) 


