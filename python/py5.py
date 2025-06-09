count=0
while count<=5:
    print('hii',count)
    count+=1

tuple=(1,2,4,6,35,64)
print(tuple)
i=1
while i<=len(tuple):
    if(i==tuple[2]):
        print('the position of number: ', i)
    i+=1
i=1
while i<=5:
    print(i)
    if(i==3):
        break
    i+=1
while i<=20: 
    if(i%2==0):
        i+=1
    print(i)
    i+=1
list=[1,3,4,5,6,7]
string='stromng'
for el in string:
    print(el)


seq=range(0,10,2)
for el in range(0,5):
    print(el)

for el in seq:
    print(el)

for el in range(100): print(el)
for el in range(100,0,-1): print(el)
n=2
for el in range(1,11):
    print(n*el) 
n=20
i=0
result=0
while i<=n:
    result += i
    print(result)
    
    i+=1 

def calculate_sum(a,b):{
    print(a+b)
}
calculate_sum(1,3)

def Print(a):{
    print(a)
}
Print('hello')
def fun(a=3,b=2):{
    print(a*b)
}
fun(1,5)

def list_length(a):
    print(len(a))
    for el in a:
        print(el, end=' ')

list=[1,2,3,4,5,56]
list_length(list)

# recursive function
def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)

show(5)

def factorial_num(n):
        if(n==0 or n==1):
            return 1
        else:
            return n * factorial_num(n-1)
        

factorial =factorial_num(6)
print(factorial)

def Print_List(list,i):
    
    print(list,i)

list=[1,324,5]
index=[]
for el in list:
    index.append(el)
Print_List(list,index)