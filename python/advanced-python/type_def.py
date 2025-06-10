from typing import List,Tuple,Union

my_list:List[int]=[1,2,3,4,5]
my_list2:List[int]=[1,2323]
my_tuple:Tuple[str,int]=('talha',2)
union:Union[int,str]='talha'
union=123   #also valid bcz it can have both vals
a:int=1
name:str='talha'
email:str='talha@gmail.com'
b:float=0.4
c:bool=True

def add(num1:int,num2:int) -> int:
    print(num1+num2)

add(1,2)