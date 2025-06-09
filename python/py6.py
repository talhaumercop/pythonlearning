file=open('me.txt','w')
# data= file.read()
# data2= file.readline()
file.write('hi my name is talha')
file.close()
file= open('me.txt','r+')
file.write('yea')
file.close()
file=open('me.txt','r+')
data=file.read()
file.write('hahahaha')
print(data)
file.close()
with open('me.txt', 'r') as file:
    data=file.read()
    print(data)
    file.close()
with open('demo.js','w+') as file:
    file.write('function myName(){}')
    print(file.read())
import os
os.remove('demo.js')

file = open('practice.txt','w')
file.write('hi everyone \nwe are learning python \nusing java \ni dont like progrmaming')
file.close()

with open('practice.txt','r') as f:
   data=f.read()

with open('practice.txt','w') as f:
   new_data=data.replace('java','python')
   f.write(new_data)

with open('practice.txt','r') as f:
   data=f.read()
   if(data.find('learning') != -1):
      print('true')
   else:
      print('false')
    