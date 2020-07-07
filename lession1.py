print('你好')
name = 'nimenhao'
a=3
b=2
c=4
d=(a+c)/b
print(d)
print(bool([]))
print(1>0 and 1<2)

#打印1到100的和
a=1
b=0
while a<101:
    b=b+a
    a=a+1
print(b)

#斐波那契数列，后一个数是前两个数的和
i=0
j=1
while i<1000:
    print(i,end='\t')
    i,j=j,i+j
    