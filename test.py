print('hello world')
def eat(a,b):
    a= a+b
    b= None
    list = [a,b]
    return list
ma = 10
mb = 20
test = {'a':1,'b':2,'c':3}
while True:
    ma = eat(ma,mb)[0]
    mb = eat(ma,mb)[1]
    if mb is None:break
word = input('choose: ')
p= 20
print(test[word])
print(p)