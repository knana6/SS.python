###딕셔너리1
##phone_book={'홍길동':'010-1234-5678','강감찬':'010-1111-2222','조용히':'010-2111-2111'}
##print(phone_book['조용히']) #딕셔너리는 반환 기능, 출력하려면 print() 사용
###리스트는 [], 딕셔너리는 {}

###딕2
##p={} #공백 딕셔너리
##p["김나나"]='010-2222-2222' #딕셔너리에 값을 추가하는 방법
##print(p)
###['key']->'value'
##
##d={'name':'kwn','age':'20','color':'lightpink','status':'palpitating'}
##print(d['status'])


###딕3
##go={'나는':'행복합니다','누나는':'치킨이먹고싶어요','오빠는':'배고파','동생은':'귀여워'}
##print(go.keys()) #>dict_keys(['나는','누나는','오빠는','동생은'])
##for key in sorted(go.keys()): #모든 킷값 key가 순회
##    print(key,go[key]) # key 와 value값 나란히 출력
##print(go.values()) #>dict_values(['행복합니다','치킨이먹고싶어요','배고파','귀여워'])
### ['key']=>'value'

###딕4:수정은 키를 통해
##go={'나는':'행복합니다','누나는':'치킨이먹고싶어요','오빠는':'배고파','동생은':'귀여워'}
##go['나는']='태연합니다' #냅다 지정하는게 바로 수정한다는 의미
##print(go['나는'])
###del go['오빠는']
###go.pop('오빠는') 둘다 삭제의 의미, 팝은 객체를 앞에 꼭서주고 소괄호다
##print(go.keys())
##go.clear() #모두 삭제하는 것!
##print(go.keys())

###추가
##list={'나는':'행복합니다','누나는':'치킨이먹고싶어요','오빠는':'배고파','동생은':'귀여워'}
##print(list.get('누나는')) #get('key') ->'value'
##print(list.get('쌩은','default')) #콤마 추가해서 디폴트값 설정 가능


###딕6 딕셔너리와 반복문의 궁합
##items={'커피':7,'펜':3,'종이':10,'우유':5,'콜라':4,'라면':11}
##for k in items:
##    print(k,end=" ")
##print()
##for s in items.keys():
##    print(s,end=" ")
##print()
##for v in items.values():
##    print(v,end=" ")
##print()
##for a in items.items(): #items는 튜플 자료형이기 때문에index 사용 가능
##    print(a,a[0],a[1]) #a는 ('key',value) a[0]은 key a[1]은 value
##print()
##for k,v in items.items():
##    print(k,",",v) #변수 2개 쓰면 key와 value를 각각 k,v에 저장


##items_list=list(items.values())
##print(items_list[3])
##items_list.append(33)
##print(items_list)
##items_tu=list(items.items())# dict.items()를 list로 변환시 ('key',value) 튜플 자료형으로 요소 구성
##print(items_tu)
##print(items_tu[0][1])



###추가
##list=[]
##tu=()
##dic={}
##s=set()
##print(list,type(list))
##print(tu,type(tu))
##print(dic,type(dic))
##print(s,type(s))


#멘델의 유전법칙 시뮬레이션
def make_descendant():
    h1=random.randrange(0,2)
    h2=random.randrange(0,2)

    if h1==0 and h2==0:
        h='RR'
    elif h1==0 and h2==1:
        h='Rr'
    elif h1==1 and h2==0:
        h='rR'
    else:
        h='rr'
    descendant.append(h)


def count_descendant(d):
    d_dict={}
    for n in d:
        if n in d_dict:
            d_dict[n]+=1 #key가 있다면 value값 +1
        else:
            d_dict[n]=1 #n은 'RR;, ;Rr','rR','rr'증 하자. 1은 value
    print(d_dict)
    cal_rate(d_dict)

def cal_rate(d):
    rate=(d['RR']+d['Rr']+d['rR'])/d['rr']
    print(rate,":1")

#main part#\
import random
descendant=[]
for n in range(100):
    make_descendant()
count_descendant(descendant)

