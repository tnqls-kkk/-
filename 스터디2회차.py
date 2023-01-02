#p174, 176 중간점검 구구단, p177 도전문제
#p174 while문으로 1~n까지의 합계 구하기

n=int(input('숫자를 입력하시오'))
i,hap=1,0
while i<=n:
   hap+=i
   i+=1
print('합은:',hap)

#p176 중간점검 1번 if문과 while문을 비교하여 조건식이 같다면 어떻게 동작하는가

if문은 조건이 참일 경우 한 번 출력하지만, while문은 조건이 참일 경우 반복횟수가 없다면 무한대로 출력한다

#p176 구구단 출력
#for문으로
dan=int(input('단을 입력하시오:'))
for i in range(1,dan+1):
   print('%d*%d=%d'%(dan,i,dan*1))
#while문으로
dan=int(input('단을 입력하시오:'))
i=0 
while i<dan:  #어차피 
   i+=1
   print('%d*%d=%d'%(dan,i,dan*1))

#p177 도전문제 for문으로 바꾸고 while과 for 중 더 편한 것은?
#for문을 먼저 배우고 오래 써서 더 편하다고 생각함
for i in range(1,10)
   print('%d*%d=%d'%(dan,i,dan*1))

#p184,185 도전문제,189 중간점검
#p184 주사위 2개의 합이 n인 경우

n=int(input('주사위의 합:'))
for i in range(1,n+1):    #미지수가 두 개니까 i,j
   for j in range(1,n+1):
      if i+j==n:    #두 미지수(주사위)의 합이 n이 되야하니까
         print(i,',',j)

#p185 도전문제 조합 출력

person=['Kim','Park','Lee','Choi']
restaurants=['Korean','American','French','Chinese']
locations=['서울','부산','대전']
for i in person:
    for j in locations:
        for z in restaurants:
            print(i+'이',j+'의',z+'식당을 방문')

#p189 중간점검 1,2번

#1번: break
#2번: (세로로) 1 2
for i in range(1,10,1):
    if i%3==0: break  #3에서 빠져나가니까, 조건에 해당하는 3부터는 출력 안됨
    print(i)

