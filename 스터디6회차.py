#5장 LAB

#p213 피자의 면적

def main():
    print("20cm 피자 2개 면적:", get_area(20)+get_area(20))
    print("30cm 피자 1개 면적:", get_area(30))

def get_area(radius) :
    if radius > 0 :
        area = 3.14*radius**2
    else :
        area = 0
    return area

main()

#p221 반복출력

def display(msg, count=1) :
    for k in range(count) :
        print(msg)

display("환영합니다.", 5)


#p222 근 계산하기

def f(x):
    return (x**2-x-1)

def bisection_method(a, b, error) :
    if f(a)*f(b) > 0:
        print("구간에서 근을 찾을 수 없습니다.")
    else:
        while (b-a)/2.0 > error:
            midpoint = (a+b)/2.0
            if f(midpoint)==0:
                return(midpoint)
            elif f(a)*f(midpoint) < 0:
                b = midpoint
            else:
                a = midpoint
        return midpoint

answer = bisection_method(1, 2, 0.0001)
print("x**2-x-1의 근:", answer)

#p223 주급계산
def weeklyPay(rate, hour):
    money = 0
    if (hour>30):
        money = rate*30+1.5*rate*(hour-30)
    else:
        money=rate*hour
    return money

rate=eval(input("시급:"))
hour=eval(input("근무 시간:"))
print("주급은" + str(weeklyPay(rate, hour)))

#p227 여러 값 반환

def get_info():
    name=input("이름:")
    age=int(input("나이:"))
    return name, age

st_name, st_age = get_info()
print("이름은 ", st_name, "이고 나이는 ", st_age, "살입니다.")


#p231 사각혁 터틀 프로그램

import turtle as t
t.shape("turtle")

def square(length):
    t.down()
    for i in range(4):
        t.forward(length)
        t.left(90)
    t.up()

square(100)
t.forward(120)
square(100)
t.forward(120)
square(100)

t.done()

#p241 터틀 

import turtle as t
t.shape("turtle")
t.speed(0)

def f(x):
    return x**2+1

t.goto(200, 0)
t.goto(0, 0)
t.goto(200, 0)
t.goto(0, 0)

for x in range(150):
    t.goto((x, int(0.01*f(x)))

t.bye()
           
