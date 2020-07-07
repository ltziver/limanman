
list=[5,8,6,9,3,4,8,9,5,1,4,2]        
list_len = len(list)    #定义一个变量list_len，赋值是list列表的长度,即为12
#print(list_len)

#倒叙排列
l_len=list_len//2     #定义一个变量l_len，赋值为list_len除以2取得整数，即为6
#print(l_len)
for i in range(l_len):         #i分别遍历0、1、2、3、4、5的for循环
    list[i],list[list_len-1-i]=list[list_len-1-i],list[i]   #当i=0时，list[0]=list[5],list[5]=list[0]同时进行，即互相交换值
print(list)

#冒泡排序
for i in range(list_len-1):
    for j in range(i,list_len):
        if list[i]>list[j]:
            list[i],list[j]=list[j],list[i]
print(list)
m=range(6)
print(m)