#p196 exercise
#2번 while문으로 변경

i=0
while i<=8:    
   print(i)
   i+=2   #print 이후에 i+=2를 해야, 출력되는 i전체 중에 시작(0)을 기준으로 2씩 더한 값이 나옴

#3번 while문으로 변경

i=-2
while i>=-5:
   print(i,end=' ')
   i-=1  #모든 i 중 첨(-2)부터 -1씩 하는 수만 나열

#4번

i=1
hap=0
while i<100:
   hap+=1
   i+=1
print(hap)
   
#5번 몇 번이나 출력되는 가
총 6번
for i in range(10):
   if i>5: continue
   if i>8: break
   print('Hello World!')

#6번
i가 10부터 flase임을 나타내는 i+=1이 없어서 아무것도 출력되지 않음
i=0
while i<10:
   print(i)
   i+=1

#p197
#7번
총 11번. 0~10까지니까
i=0
while i<=10:
   print('Hi!')
   i+=1

#8번 실행 결과
답 100
i=0
while (i<100):
   i+=2  #print 전에 해서, i가 98+2까지 출력 한 것!
print(i)

#10번 실행결과
답 
10 TV
10 Phone
20 TV
20 Phone

nums=[10,20]
items=['TV','Phone']
for i in nums:
   for j in items:
      print(i,j)

#p198 prograaming
#1번 2~50 짝수 출력
#for문으로
for i in range(2,51):
    if i%2==0:
        print(i,end=' ')
#while문으로
i=1  
while i<=50:
    i+=1     #여기서 i를 1씩 더한 후, 짝수인 경우를 찾는 것=>1(i)에 1을 더한 2부터 시작하는 것임
    if i%2==0:
        print(i,end=' ')
        
#2번 리스트의 합
myList=[11,22,23,99,81,93,35]
hap=0
for문으로
for i in myList:
    hap+=i
print('정수들의 합은',hap)

#3번 3의 배수의 합
hap=0
for i in range(1,101):
   if i%3==0:
      hap+=i
print('1부터 100 사이의 모든 3의 배수의 합은 %d입니다'%hap)

#4번 정수의 모든 약수
n=int(input('정수를 입력하시오:'))
print('약수',end=' ')      #밑으로 가면 '약수'가 무제한으로 나오거나 모든 약수 뒤에 나옴
for i in range(1,n+1):
   if n%i==0:      
      print(i,end=' ')
      
#5번 for,while문 모두
#for문으로
n=int(input('정수를 입력하시오:'))
for i in range(1,n+1):
   for j in range(1,i+1):   
      print(j,end=' ')
   print()
      
#while문으로
n=int(input("정수를 입력하시오 : "))
i=1
while i<n+1 :
    j=1
    while j<i+1 :
        print(j, end=" ")
        j+=1
    i+=1
    print()
    
#10번  for,while문 모두
#for문으로
n=int(input('n의 값을 입력하시오:'))
hap=0
for i in range(1, n+1):
    hap+=i**2
print('계산값은 %d입니다.'%hap)

#while문으로
n=int(input('n의 값을 입력하시오:'))
i=1
hap=0
while i<=n :
    hap+=i**2
    i+=1
print('계산값은 %d입니다.'%hap)
