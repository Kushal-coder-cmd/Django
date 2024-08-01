class Calculator:
    def add(self, a, b):
        return a+b
    def sub(self, a, b):
        return a-b
    def div(self, a, b):
        return a/b
    def mul(self, a, b):
        return a*b
class Child(Calculator):
    pass

user=Child()
a=int(input('enter the numbber a: '))
b=int(input('enter the numbber b: '))
print('1.Add\n2.Subtract\n3.Mulitply\n4.Divide')
choice = int(input('Enter the choice: '))
if(choice==1):
    result= user.add(a,b)
    print(f'Answer= {result}')
if(choice==2):
    result= user.sub(a,b)
    print(f'Answer= {result}')
if(choice==3):
    result= user.mul(a,b)
    print(f'Answer= {result}')
if(choice==1):
    result= user.div(a,b)
    print(f'Answer= {result}')
