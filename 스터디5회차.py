#프린트1
#1번) 출력되는 결과
#답: 1 2 4 5
i=0
while i<6:
   i+=1
   if i%3==0:
      continue
   print(i,end=' ')
#답: 합= 55
i=1
hap=0
while i<=10:
   hap+=i
   i+=1
print('합=',hap)

#2번) 출력결과, while문 변경
#답: 1
     12
     123
     1234
     12345
for i in range(1,6):
   for j in range(1,i+1):
      print(j,end=' ')
   print()
#while문 변경
i=0
while i<5:
   j=0
   while j<i+1:
      j+=1
      print(j,end=' ')
   print()
   i+=1
#답: *****...(10개)
     ****...(9개)
     ....
     *(1개)
for i in range(10):
   for j in range(i,10):
      print('*',end=' ')
   print()
#while문 변경
i=0
while i<10:
   j=i
   while j<10:
      j+=1
      print('*',end=' ')
   print()
   i+=1
print()
#사용자로부터 양의 정수 n을 입력받아 1부터 n까지의 제곱들의 합을 구하는 프로그램 작성
n=int(input(=숫자를 입력하세요:'))
i=0
hap=0
while i<n:
   i+=1
   hap+=i**2
print('합=',hap)

#과제) turtle 이용, while문 간략 작성
import turtle as t
i=1
while i<=6:
   t.circle(100)
   t.left(60)
   i+=1
t.dont()

#4번)소수 출력하는 프로그램
#for문으로
for i in range(2,101):
   for j in range(2,i+1):
      if i==j:
         print(i)
      elif i%j==0:
         break
#while문으로
i=2
while i<=100:
   j=2
   while j<=i:
      if j==i:
         print(i,end=' ')
      elif i%j==0:
         break
      j+=1
   i+=1


