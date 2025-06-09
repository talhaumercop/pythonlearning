# class myClass:
#     name='talha'
#     classes=[1,2,3,4,5,6]

# #constructor
#     def __init__(self,name,list):
#         print('hii')
#         self.name=name
#         self.classes=list

#     def get_info(self):
#         print(f'the list of the classes are {self.classes} and the name is {self.name} ')

#     @staticmethod
#     def good_morning():
#         print('good morning')
# class1=myClass('hitesh',[1,4,23,5,3])
# class1.get_info()
# class1.good_morning()
# # print(class1.name,class1.section)

# class programmer:
#     language=''
#     experience=''
#     salary=0
#     def __init__(self,language,experience,salary):
#         self.language=language
#         self.salary=salary
#         self.experience=experience
#         print(self.language)

# prog1=programmer('java','1year',10000)

# class Employee:
#     salary=100000
#     def __init__(self):
#         print(self.salary)
#     @classmethod
#     def show(self):
#         print(f' you class value for salary is {self.salary}')

# talha=Employee()
# talha.salary=10000000
# talha.show()

# class student:
#     number_of_stud=0
#     name='default'
#     email=''

#     def __init__(self,name,email):
#         self.name=name
#         self.email=email

#     def showDetails(self):
#         print(f'student name is {self.name} and email is {self.email} and total no. of students are {self.number_of_stud}')
    
#     @classmethod
#     def increase_count(cls):
#         cls.number_of_stud+=1
        
# student1=student('talha','talha@gmail.com')
# student1.increase_count()
# student2=student('talha','talha@gmail.com')
# student2.increase_count()
# student1.showDetails()

# class twoDvec:
#     def __init__(self,i,j):
#         self.i=i
#         self.j=j
        
#     def show(self):
#         print(self.i,self.j)

# class threeDvec(twoDvec):
#     def __init__(self,i,j,k):
#         super().__init__(i,j)
#         self.k=k
#     def show(self):
#         print(self.i,self.j,self.k)

# a=twoDvec(1,2).show()
# b=threeDvec(1,2,4).show()
import random

n = random.randint(1, 50)
inputt = -1
guesses = 0

while n != inputt:
    guesses += 1
    inputt = int(input('Guess a number: '))

    if n > inputt:
        print('Higher number please!')
    elif n < inputt:
        print('Lower number please!')

print(f'You guessed it right in {guesses} tries!')
