#프린트2
#1
def sum(v1,v2):
  result=v1+v2
  return result
print(sum(10,20))

#2
def func(v1,v2=0,v3=0):
  return v1+v2+v3
print(func())

#3
a=0
def func1():
  print(a)
def func2():
  a=111
  print(a)
func()
func()
#결과: 0 / 111

#4
def sub(a,b):
  return a+b,a-b
x,y=sub(10,20)
print(x,y)

#5
x=10   
def dec()
  glbal x  #외부변수
  x=x-1
dec()
print(x)
#결과: 9

#6
def square(n):
  return n**2
print('3의 제곱은:',square(3))
print('4의 제곱은:',square(4))

#7
import turtle as t
t.shape('turtle')
def draw_square(size):
  for i in range(4):
    t.fd(size)
    t.left(90)
    size+=5
for i in range(10):
  draw_sqaure(i*20)
t.done()
