class Calculator:
    def __init__(self, first, second):
        self.first = first 
        self.second = second 
    def setdata(self, first, second):
        self.first = first 
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def pow(self):
        result = self.first ** self.second
        return result
    
class UpgradeCal(Calculator):
    def div(self):
        if self.second == 0:
            return 'Infinity'
        else:
            return self.first / self.second

ar = {'+': 'add','-': 'sub','*': 'mul','/':'div','**':'pow'}

num = input('뛰어쓰기필수:')

count = len(num.split())

a = []
c = []

for i in range(0,count,2):
    a.append(int(num.split()[i]))

for i in range(1,count-1,2):
    c.append(num.split()[i])
test1 = UpgradeCal(a[0],a[1])
if count == 3:
    if c[0] == '+':
        print(test1.add())
    elif c[0] == '-':
        print(test1.sub())
    elif c[0] == '/':
        print(test1.div())
    elif c[0] == '*':
        print(test1.mul())
    elif c[0] == '**':
        print(test1.pow())
##else:
##    for i in range(0,len(a)-1):
##        test1 = UpgradeCal(a[i],a[i+1])
##        if c[i] == '+':
##            a[i+1]=test1.add()
##        elif c[i] == '-':
##            a[i+1]=test1.sub()
##        elif c[i] == '/':
##            a[i+1]=test1.div()
##        elif c[i] == '*':
##            a[i+1]=test1.mul()
##        elif c[i] == '**':
##            a[i+1]=test1.pow()
##    print(a[-1])
        