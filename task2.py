filee=open('file')
a=[]
a1=[]
b=[]
c=[]
d=[]
d1=[]
def func():
 count=0
 count1=0
 count2=0
 count3=0
 count4=0
 count5=0
 for line in filee:
  for i in line.split():
   #print(i)
   if 'ASSAULT' and '1430' in i:
    #print()
    count+=1
    #print(count)
    #print(word)
    a.append(i)
   if 'ASSAULT' and '1420' in i:
    #print()
    count1+=1
    #print(count)
    #print(word)
    a1.append(i)
 #print(a)
   elif 'ROBBERY' and '1610' in i:
    count2+=1
    b.append(i)
   elif 'BREAK' and '2120' in i:
    count3+=1
    c.append(i)
   elif 'THEFT' and '2135' in i:
    count4+=1
    d.append(i)
   elif 'THEFT' and '2142' in i:
    count5+=1
    d1.append(i)

 print('CrimeType','ASSULT',"CrimeID 1430",'Crime Count',count)
 print('CrimeType','ASSULT',"CrimeID 1420",'Crime Count',count1)
 print('CrimeType','ROBBERY',"CrimeID 1610",'Crime Count',count2)
 print('CrimeType','BREAK',"CrimeID 1430",'Crime Count',count3)
 print('CrimeType','THEFT OF VEHICLE',"CrimeID 2135",'Crime Count',count4)
 print('CrimeType','THEFT FROM VEHICLE',"CrimeID 2142",'Crime Count',count5)

func()



