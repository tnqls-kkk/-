#p31 중간점검
#1)"안녕하세요?" 출력하기
print("안녕하세요?")

#2)"programming에 입문하신 것을 축하드립니다."를 출력하여 보자
print("programming에 입문하신 것을 축하드립니다.")

#4)"생일축하!!"를 10번 출력하는 명령문을 만들어보자. 문자열 반복을 사용한다.
print("생일축하!!"*10)

#print("Hello)를 실행하면 오류가 발생한다. 원인을 알아보자
print("Hello") #큰따옴표 하나가 생략되어 문자열의 역할을 하지 못한다.

#p38 중간점검
#3단 구구단의 일부(*3까지)를 출력하는 프로그램 작성하기
#print함수만 사용
print("3*1=",3*1)
print("3*2=",3*2)
print("3*3=",3*3)

#range반복문 사용
for i in range(1,4):
    print("%d*%d=%d"%(3,i,3*i))

#p39 도전문제
    #*******************************
#print()를 사용한 예제입니다.
#내가 제일 좋아하는 숫자는 7입니다.
#*******************************
#라는 메시지를 출력하는 프로그램을 작성해보자
print('*'*31)
print('print()를 사용한 예제입니다.')
print('내가 제일 좋아하는 숫자는 7입니다.')
print('*'*31)

#줄바꿈 사용하기
print('*'*31,'print()를 사용한 예제입니다.','내가 제일 좋아하는 숫자는 7입니다.','*'*31,sep='\n')

#49 중간점검
#1)거북이를 움직여서 정삼각형을 그려보자. 회전하는 각도를 몇 도로 하여야 하는가?
import turtle as t
t.shape('turtle')

t.left(120) #180도에서 정삼각형의 한 각인 60도를 뺀 120도를 해야 한다
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)
t.done()

#range반복문 사용
for i in range(3):
    t.left(120)
    t.forward(100)
t.done()

#2)거북이를 움직여서 정사각형을 그려보자. 회전하는 각도를 몇 도로 하여야 하는가?
import turtle as t
t.shape('turtle')
for i in range(4):
    t.left(90) #90도로 회전해야 한다
    t.forward(100)
t.done()

#3)거북이를 움직여서 정6각형을 그려보자. 회전하는 각도를 몇 도로 하여야 하는가?
import turtle as t
t.shape('turtle')
for i in range(6):
    t.left(60) #60도를 회전해야 한다
    t.forward(100)
t.done()

#p55 Programming 1~5번
#1)"환영합니다.","파이썬의 세계에 오신 것을 환영합니다.","파이썬은 강력합니다."를 화면에 작성하시오. 스크립트 모드로 실행한다.
print('환영합니다.','파이썬의 세계에 오신 것을 환영합니다.','파이썬은 강력합니다.',sep='\n')

#2)다음과 같이 사각형 안에 이름을 출력하는 프로그램을 작성해보자
#줄바꿈 사용 안되더라
print('+'+'='*16+'+')
print(':'+'     '+'홍길동'+'     '+':')
print('+'+'='*16+'+')

#3)1~3의 합을 출력하는 프로그램을 반복문 사용하지 않고 작성해보자.
print(1+2+3)

#4)"1+2+3을 계산하면 6입니다."를 6은 1+2+3을 계산하여 출력하는 프로그램을 작성해보자
print('1+2+3을 계산하면 %d입니다.'%(1+2+3)) #%d에 1+2+3의 정수값을 계산하여 넣도록 함

#5)터틀 그래픽에서 거북이를 이동시켜서 다음과 같은 그림을 그려보자. forward(), right(), left() 함수만을 사용한다.
import turtle as t
t.shape('turtle')
t.forward(100)
t.left(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.left(90)
t.forward(100)
t.done()

#p56 Programming 6~9번
#6)거북이에게 몇 개의 명령문을 주어서 햄버거를 사오게 하자. 햄버거 가게는 (300,200)에 있다고 가정한다. 거북이는 (0,0) 위치에 있다고 하자.
import turtle as t
t.shape('turtle')
t.forward(300)
t.left(90)
t.forward(200)
#햄버거 위치 도달
t.left(90)
t.forward(300)
t.left(90)
t.forward(200)
t.done()

#7)터틀 그래픽에서 width() 함수를 호출하면 거북이가 그리는 선의 두께를 두껍게 한다. 거북이를 이동하여서 다음과 같이 두께가 10인 선을 그려보자
import turtle as t
t.shape('turtle')
t.width(10)
t.forward(100)
t.left(90)
t.forward(100)
t.done()

#8)터틀 그래픽에서 color()함수를 호출하면 거북이가 그리는 선의 색상을 변경할 수 있다. 색상을 파랑색으로 변경하여서 다음과 같이 길이가 100픽셀인 선을 그려보자
import turtle as t
t.shape('turtle')
t.color('blue')
t.forward(100)
t.done()

#9)터틀 그래픽에서는 거북이의 모양을 삼각형, 원, 사각형으로 변경할 수 있다. 다음과 같이 shape()함수를 사용하면 된다. 사각형으로 변경하고 100픽셀 길이의 직선을 그려보자
import turtle as t
t.shape('square')
t.forward(100)
t.done()

