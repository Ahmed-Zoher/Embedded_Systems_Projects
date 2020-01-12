# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from firebase import firebase
import math
firebase = firebase.FirebaseApplication('https://coin-collector-7dd3f.firebaseio.com', None)
c1 = firebase.get('/Coin1', None)
c2 = firebase.get('/Coin2', None)
c3 = firebase.get('/Coin3', None)
c4 = firebase.get('/Coin4', None)
c5 = firebase.get('/Coin5', None)
c6 = firebase.get('/Coin6', None)
coinX=[1,1,1,1,1,1];
coinY=[1,1,1,1,1,1];
coins=[c1,c2,c3,c4,c5,c6]
def getMinNonZero(x):
    min=max(x);
    idx=-1;
    for i in range(len(x)):
        if (x[i]<=min and x[i]!=0):
            idx=i;
            min=x[i];
    return idx;        

for i in range(6):
    coinX[i]=math.floor(coins[i]/10)
    coinY[i]=coins[i]%10



w=4;
graph=[[0 for x in range(w)]for y in range(w)];
#coinX=[2,1,2,3,3,2];
#coinY=[1,2,2,3,2,3];
coin1=[1,2,3,4,5,6];
coin2=[1,2,3,4,5,6];
move1=[];
move2=[];

i1=0;
i2=0;
d1=[0 for x in range(len(coinX))];
d2=[0 for x in range(len(coinX))];
car1X=1;
car1Y=1;
car2X=4;
car2Y=1;
goalX=[car1X,car2X];
goalY=[car1Y,car2Y];
car1Xi=goalX[0];
car1Yi=goalY[0];
car2Xi=goalX[1];
car2Yi=goalY[1];
done=[0, 0, 0, 0, 0, 0];
d11=[200 for i in range(len(done))];
for i in range (len(coinX)):
    d1[i]=abs(car1X-coinX[i])+abs(car1Y-coinY[i]);
    d2[i]=abs(car2X-coinX[i])+abs(car2Y-coinY[i]);

for i in range (len(coinX)):
    for j in range (len(coinX)-1):
        if d1[j]>d1[j+1]:
            temp=d1[j];
            d1[j]=d1[j+1];
            d1[j+1]=temp;
            temp=coin1[j];
            coin1[j]=coin1[j+1];
            coin1[j+1]=temp;
        if d2[j]>d2[j+1]:
            temp=d2[j];
            d2[j]=d2[j+1];
            d2[j+1]=temp;
            temp=coin2[j];
            coin2[j]=coin2[j+1];
            coin2[j+1]=temp;

idx1=0;
idx2=0;
while sum(done)!=len(done):
    while(coin1[idx1]==coin2[idx2] or done[coin1[idx1]-1]==1 or done[coin2[idx2]-1]==1 ):
        if done[coin1[idx1]-1]==1:
            idx1+=1;
            continue;
        if done[coin2[idx2]-1]==1:
            idx2+=1;
            continue;
        if(coin1[idx1]==coin2[idx2]):
            if(idx1<idx2):
                idx1+=1;
            else:
                idx2+=1;
    while(car1Y!=coinY[coin1[idx1]-1]):
        if car1Y<coinY[coin1[idx1]-1]:
            car1Y+=1;
            move1.append(3);
        else:
            car1Y-=1;
            move1.append(4);
    while(car1X!=coinX[coin1[idx1]-1]):
        if car1X<coinX[coin1[idx1]-1]:
            car1X+=1;
            move1.append(1);
            
        else:
            car1X-=1;
            move1.append(2);
    move1.append('P');        
    while(car1X!=goalX[0]):
        if car1X<goalX[0]:
            car1X+=1;
            move1.append(1);
        else:
            car1X-=1;
            move1.append(2);
      
    while(car1Y!=goalY[0]):
        if car1Y<goalY[0]:
            car1Y+=1;
            move1.append(3);
        else:
            car1Y-=1;
            move1.append(4);        
    move1.append('D');
    done[coin1[idx1]-1]=1;  
    idx1+=1; 
    while(car2X!=coinX[coin2[idx2]-1]):
        if car2X<coinX[coin2[idx2]-1]:
            car2X+=1;
            move2.append(1);
        else:
            car2X-=1;
            move2.append(2);       
    while(car2Y!=coinY[coin2[idx2]-1]):
        if car2Y<coinY[coin2[idx2]-1]:
            car2Y+=1;
            move2.append(3);
        else:
            car2Y-=1;
            move2.append(4);
    move2.append('P');        
    while(car2Y!=goalY[1]):
        if car2Y<goalY[1]:
            car2Y+=1;
            move2.append(3);
        else:
            car2Y-=1;
            move2.append(4);
    while(car2X!=goalX[1]):
        if car2X<goalX[1]:
            car2X+=1;
            move2.append(1);
        else:
            car2X-=1;
            move2.append(2);        
    move2.append('D');
    done[coin2[idx2]-1]=1;
    idx2+=1;


car1Face='N';
car2Face='N';
rotate1=[];
rotate2=[];
p1x=car1Xi;
p1y=car1Yi;
p2x=car2Xi;
p2y=car2Yi;

i=0;
j=0;         
while(i<len(move1) and j<len(move2)):
        if(move1[i]=='P'):
            rotate1.append('P');
            i+=1;
        elif (move1[i]=='D'):
            rotate1.append('D');
            i+=1;
            if i==len(move1):
                break;
        if(move1[i]==1):
            p1x+=1;
            i+=1;
            if(car1Face=='N'):
                rotate1.append('R');
            elif (car1Face=='S'):
                rotate1.append('L');
            elif (car1Face=='W'):
                rotate1.append('L');
                rotate1.append('L');
            car1Face='E'    
        elif(move1[i]==2):
            p1x-=1;
            i+=1;
            if(car1Face=='N'):
                rotate1.append('L');
            elif (car1Face=='S'):
                rotate1.append('R');
            elif (car1Face=='E'):
                rotate1.append('L');
                rotate1.append('L');
            car1Face='W'
        elif(move1[i]==3):
            p1y+=1;
            i+=1;
            if(car1Face=='W'):
                rotate1.append('R');
            elif (car1Face=='E'):
                rotate1.append('L');
            elif (car1Face=='S'):
                rotate1.append('L');
                rotate1.append('L');
            car1Face='N'
        elif(move1[i]==4):
            p1y-=1;
            i+=1;
            if(car1Face=='E'):
                rotate1.append('R');
            elif (car1Face=='W'):
                rotate1.append('L');
            elif (car1Face=='N'):
                rotate1.append('L');
                rotate1.append('L');
            car1Face='S'
            
        if len(rotate1)>1 and rotate1[len(rotate1)-1]=='L' and rotate1[len(rotate1)-2]=='L' and len(rotate1)>=2:
            rotate1.pop();
            rotate1.pop();
            rotate1.append('B');
            if car1Face=='S':
                car1Face='N';
            elif car1Face=='E':
                car1Face='W';
            elif car1Face=='N':
                car1Face='S';
            elif car1Face=='W':
                car1Face='E';   
        else:   
            rotate1.append('F');     
        if(move2[j]=='P'):
            rotate2.append('P');
            j+=1;
        elif(move2[j]=='D'):
            rotate2.append('D');
            j+=1;
            if j==len(move2):
                break;
        if(move2[j]==1):
            p2x+=1;
            j+=1;
            if(car2Face=='N'):
                rotate2.append('R');
            elif (car2Face=='S'):
                rotate2.append('L');
            elif (car2Face=='W'):
                rotate2.append('L');
                rotate2.append('L');
            car2Face='E' 
        elif(move2[j]==2):
            p2x-=1;
            j+=1;
            if(car2Face=='N'):
                rotate2.append('L');
            elif (car2Face=='S'):
                rotate2.append('R');
            elif (car2Face=='E'):
                rotate2.append('L');
                rotate2.append('L');
            car2Face='W'
        elif(move2[j]==3):
            p2y+=1;
            j+=1;
            if(car2Face=='W'):
                rotate2.append('R');
            elif (car2Face=='E'):
                rotate2.append('L');
            elif (car2Face=='S'):
                rotate2.append('L');
                rotate2.append('L');
            car2Face='N'
        elif(move2[j]==4):
            p2y-=1;
            j+=1;
            if(car2Face=='E'):
                rotate2.append('R');
            elif (car2Face=='W'):
                rotate2.append('L');
            elif (car2Face=='N'):
                rotate2.append('L');
                rotate2.append('L');
            car2Face='S'
        if len(rotate2)>1 and rotate2[len(rotate2)-1]=='L' and rotate2[len(rotate2)-2]=='L' and len(rotate2)>=2:
            rotate2.pop();
            rotate2.pop();
            rotate2.append('B');
            if car2Face=='S':
                car2Face='N';
            elif car2Face=='E':
                car2Face='W';
            elif car2Face=='N':
                car2Face='S';
            elif car2Face=='W':
                car2Face='E';    
        else:   
            rotate2.append('F');    
        if(p1x==p2x and p1y==p2y):
            move2.insert(j+1,0);
            rotate2.insert(len(rotate2)-1,'S');
            j+=1;
        print(p1x,p1y,p2x,p2y);                      
while(j<len(move2)):
   
    if(move2[j]=='P'):
        rotate2.append('P');
        j+=1;
    elif(move2[j]=='D'):
        rotate2.append('D');
        j+=1;
        if j==len(move2):
            break;
    if(move2[j]==1):
        p2x+=1;
        j+=1;
        if(car2Face=='N'):
            rotate2.append('R');
        elif (car2Face=='S'):
            rotate2.append('L');
        elif (car2Face=='W'):
            rotate2.append('L');
            rotate2.append('L');
        car2Face='E' 
    elif(move2[j]==2):
        p2x-=1;
        j+=1;
        if(car2Face=='N'):
            rotate2.append('L');
        elif (car2Face=='S'):
            rotate2.append('R');
        elif (car2Face=='E'):
            rotate2.append('L');
            rotate2.append('L');
        car2Face='W'
    elif(move2[j]==3):
        p2y+=1;
        j+=1;
        if(car2Face=='W'):
            rotate2.append('R');
        elif (car2Face=='E'):
            rotate2.append('L');
        elif (car2Face=='S'):
            rotate2.append('L');
            rotate2.append('L');
        car2Face='N'
    elif(move2[j]==4):
        p2y-=1;
        j+=1;
        if(car2Face=='E'):
            rotate2.append('R');
        elif (car2Face=='W'):
            rotate2.append('L');
        elif (car2Face=='N'):
            rotate2.append('L');
            rotate2.append('L');
        car2Face='S'
    if rotate2[len(rotate2)-1]=='L' and rotate2[len(rotate2)-2]=='L' and len(rotate2)>=2:
        rotate2.pop();
        rotate2.pop();
        rotate2.append('B');
        if car2Face=='S':
            car2Face='N';
        elif car2Face=='E':
            car2Face='W';
        elif car2Face=='N':
            car2Face='S';
        elif car2Face=='W':
            car2Face='E';    
    else:   
        rotate2.append('F');
while(i<len(move1)):
    if(move1[i]=='P'):
        rotate1.append('P');
        i+=1;
    elif (move1[i]=='D'):
        rotate1.append('D');
        i+=1;
        if i==len(move1):
            break;
    if(move1[i]==1):
        p1x+=1;
        i+=1;
        if(car1Face=='N'):
            rotate1.append('R');
        elif (car1Face=='S'):
            rotate1.append('L');
        elif (car1Face=='W'):
            rotate1.append('L');
            rotate1.append('L');
        car1Face='E'    
    elif(move1[i]==2):
        p1x-=1;
        i+=1;
        if(car1Face=='N'):
            rotate1.append('L');
        elif (car1Face=='S'):
            rotate1.append('R');
        elif (car1Face=='E'):
            rotate1.append('L');
            rotate1.append('L');
        car1Face='W'
    elif(move1[i]==3):
        p1y+=1;
        i+=1;
        if(car1Face=='W'):
            rotate1.append('R');
        elif (car1Face=='E'):
            rotate1.append('L');
        elif (car1Face=='S'):
            rotate1.append('L');
            rotate1.append('L');
        car1Face='N'
    elif(move1[i]==4):
        p1y-=1;
        i+=1;
        if(car1Face=='E'):
            rotate1.append('R');
        elif (car1Face=='W'):
            rotate1.append('L');
        elif (car1Face=='N'):
            rotate1.append('L');
            rotate1.append('L');
        car1Face='S'
    if rotate1[len(rotate1)-1]=='L' and rotate1[len(rotate1)-2]=='L' and len(rotate1)>=2:
        rotate1.pop();
        rotate1.pop();
        rotate1.append('B');
        if car1Face=='S':
            car1Face='N';
        elif car1Face=='E':
            car1Face='W';
        elif car1Face=='N':
            car1Face='S';
        elif car1Face=='W':
            car1Face='E';   
    else:   
        rotate1.append('F');    
print(rotate1);
print(rotate2);                   
firebase.put('',"rotate1size",len(rotate1))
firebase.put('',"rotate2size",len(rotate2))

         
firebase.put('',"rotate1",rotate1)     
firebase.put('',"rotate2",rotate2)   