filee=open('file')
a=[]
b=[]
c=[]
d=[]
def func():
 count=0
 count1=0
 count2=0
 count3=0
 for line in filee:
  for i in line.split():
   #print(i)
   if 'ASSAULT' in i:
    count+=1
    #print(count)
    #print(word)
    a.append(i)
 #print(a)
   elif 'ROBBERY' in i:
    count1+=1
    b.append(i)
   elif 'BREAK' in i:
    count2+=1
    c.append(i)
   elif 'THEFT' in i:
    count3+=1
    d.append(i)
 print(a,count)
 print(b,count1)
 print(c,count2)
 print(d,count3)
func()



