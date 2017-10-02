filee=open('file')
a=[]
def func():
 count=0
 for i in filee:
  for word in i.split():
  #if i=='ASSAULT':
   if 'ASSAULT' in word:
    count+=1
    print(count)
    a.append(word)
  print(a)
  #count=count+1 
  #print(count)
func()
