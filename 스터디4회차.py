#p244 exercise
#chapter5 exercise
#1번 빈칸 채우기(더 큰 수 출력하기)
def max(a,b):
    if a>b:
        result=a
    else:
        result=b
    return result

#2번 출력하기
#답: 10
def main():
    print(mistery(10,20))  #main() 이라는 함수=mistery(a,b)에 10,20을 넣은 것을 print한 함수임

def mistery(a,b):
    result=a   #임의로 result값은 a임(지역변수 너낌. 딱히 말이 없으면 무조건 a임)
    if b<result:   #b가 result값인 a보다 작을 때->result는 (a가 아닌)b로 저장됨
        result=b
    return result  #이 mistery 함수를 출력했을 때 결과는 result값이 출력돼야함 
main()   #main함수, 즉 mistery 함수에 10,20을 넣은 값(result값)을 출력함
       
#3번 함수 호출 중 올바른 것
#답: sub(1,2,3,d=4)

#4번 실행 결과와 그 이유
#답: 0
def mistery(a,b,min):
    min=a    #지역변수
    if b<min:
        min=b   #'a값을 부여받은 min이 b보다 크면->min은 b값으로 저장됨'이라고 정의만 해놓음
  mistery함수를 출력하려면, return으로 반환하거나, print로 출력한다는 정의가 필요함
min=0   #전역변수아님
mistery(20,10,min)   #mistery()함수는 정의만 하고 출력되는 값이 없는 함수임. 
print(min) #mistery함수의 min을 출력시킬 return이나 print가 함수 정의 내용에 없기 때문에->min=0이라는 내용을 고대로 적용

5번 실행 결과와 그 이유
답: 9
x=10  #모든 부분에 통용하는 전역변수
def dec(): 
    global x  #x가 전역변수라는 뜻임
    x-=1  #x에서 1을 빼야

dec()
print(x)

#6번 코드에서 잘못된 것은?
#답: 거짓인 경우(x가 양수,0인 경우)값이 없음
x=int(input('정수:'))
if x<0:
    y=10
print(y)

#7번 실행 결과
#답: 2 3 / 10 3 / 5 6 / 2 10
def sub(a=2,b=3):
    print(a,b)

sub()   #기본적으로 a=2,b=3 인데,
sub(a=10)   #따로
sub(5,6)        #이렇게 정해줄 경우,
sub(b=10)          #정해준 값은 정해준 대로, 안정해준 값은 기본값으로 출력

#8번 실행 결과
#답: 30 -10
def sub(a,b):
    return a+b,a-b   #반환할 때 a+b값과 a-b값이 결과임

x,y=sub(10,20)   #x,y의 값에 sub함수(10,20을 넣은)를 넣었으니, 결과로 10+20, 10-20값으로 각각 반환됨
print(x,y)   

#9번 오류 발생 이유
global=0
def sub():
    local=1
    print(global)
    print(local)

sub()
print(global)
print(local)

#p246 programming
#1번 원의 둘레
def get_peri(r=5.0) :
    p=2.0*3.141692*r
    return p

print('get_peri()=',get_peri())
print('get_peri(4.0)=',get_peri(4.0))

#2번 함수 작성, 테스트
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multi(a,b):
    return a*b
def divide(a,b):
    return a/b

a=int(input('첫 번째 정수를 입력하시오:'))
b=int(input('두 번째 정수를 입력하시오:'))
print('(10+20)=',add(a,b))
print('(10-20)=',sub(a,b))
print('(10*20)=',multi(a,b))
print('(10/20)=',divide(a,b))

#3번 수정하기
def calc(a, b) :
    return a+b, a-b, a*b, a/b

i=int(input("첫번째 정수를 입력하시오: "))
j=int(input("두번째 정수를 입력하시오: "))
a, b, c, d = calc(i, j)
print(a, b, c, d, "이 반환되었습니다.")


#4번 성적 함수 getGrade(score)를 작성하고 테스트
#????
def getGrade(score):
    if score>=90:
        print('A')
    elif score>=80:
        print('B')
    elif score>=70:
        print('C')
    elif score>=60:
        print('D')
    else:
        print('F')

score=int(input('점수를 입력하세요:'))
getGrade(score)   


#6번 함수 작성과 테스트
def add(a,b):
    return a+b

a=int(input('첫 번째 정수를 입력하시오:'))
b=int(input('두 번째 정수를 입력하시오:'))
i=add(a,b)
print('정수 %d+%d의 합은?'%(a,b))

#9번 최대 공약수를 찾는 함수
def gcd(a,b):
    if a%b==0:
        return b
    else:
        return a%b #요기 잘 모르겠음

a=int(input('첫 번째 정수;'))
b=int(input('두 번째 정수:'))
print(gcd(a,b))

#10번
#이거 모르겠음;;
def testPrime(n):
    n=2
    for i in range(n+1):
        if i%1==0:
            print(i)
        else:
            print()
        i+=1
n=100
print(testPrime(n))

#16번
import turtle
turtle.shape('turtle')

def draw_line():
    turtle.forward(100)
    turtle.backward(100)

for i in range(12):
    draw_line()
    turtle.left(30)
