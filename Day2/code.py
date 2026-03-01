list1=[1,2,3,4,5]


list2=[1,1.2,3.4+56.45j,True,'Hello']
print(list1)
print(list2)
print(type(list1))
print(list())

list1.append(10)

print(list1.append(7))
list1.insert(2,0)
print(list1)


help(list.append)
help(list.insert)

l1=[1,2,3]
l1.insert(4,3)
print(l1)

l1.insert(100,4)
print(l1)

l1.insert(-1,1000)


print(l1)

l1.insert(-7, 0)

print(l1)

help(list.extend)

l1.extend(list1)

print(l1)

l1.extend(list1)

print(l1)

l1=[1,2,3]
l2=[3,4,5]
l1.extend([i for i in range(0,100)]) 
print(l1)

l3=[1,2,3]
l3.extend((1,1))
l3.extend([(0,0,0)])
l3.extend([1.1,1.1])
print(l3)

l5=[1,1,1]
l6=l5
print(id(l5))
print(id(l6))

l7=l5+l6
print(l7)
print(id(l7))

l7.pop()

print(list1)
list1.pop(2)

print(list1)



list1.remove(7)
print(list1)


my_list=[100,23.5334,424+67j,'HELLO',[1,2,3]]
my_list[len(my_list)-1][len(my_list[len(my_list)-1])-1]


my_list[-2][-2]

tpl1=(1,2,3) 
tpl2=(1,2,'a',1.1)
tpl=1,2,3,41,44,6 
print(tpl)

s={1,False,0,True}
print(s)

s={1,2,3,3,4,5,6,6,6,"HELLO",5456.8585,696-4j}
print(s)

s.add(100)
print(s)

d1={'a':45,4:'jk'}
print(d1)

user_info={
    'userid':'Bhavishya',
    'password':'*****',
    'location':'Jaipur'
}

user_info

user_info['userid']


user_info['is_logged_in']=True

user_info

user_info['is_logged_in']=False

d1={
    1:'first value',
    1:'second value'
}
print(d1)

list1=[1,2,3]
print(id(list1))
list1[0]=10
print(list1)
print(id(list1))


list1.insert(0,10)
print(id(list1))

n1=250
print(id(n1))
n2=50
n1=n1+n2
print(n1)
print(id(n1))

print(id(n1))
print(id(10101))

s="PYTHON"
s[-1]
s[-1]='n'

t1=(1,2,3)
t1[2]=0


s='hello python'
print(s[:5:])
print(s[4::-1])

print(s[:1:])
print(s[::])

s2=s[::-1]
print(s2)
if s==s2:
  print ("Yes")
else:
  print("Not palindrome")

l10=[i for i in range(0,6)]
print(l10)
l10[-5:-3:1]

l10[-5::]

print(l10[-2:0:-1])
print(l10[::2])

print(10+5.5)


a=float(10)
print(a)
b=10
print(complex(b))
print(bool(b))
print(str(b))

a=100
b=a
print(id(a))
print(id(b))

l1=[1,2,3,4,5]
l2=l1
print(id(l1))
print(id(l2))
l1.append(6)
print(l1)
print(l2)

l3=[1,2,3]
l4=l3.copy()
print(id(l3))
print(id(l4))
l3.pop()
print(l3)
print(l4)

l1=[10,20,[30,40]]
l2=l1.copy()
l1[-1].pop()
print(l1)
print(l2)

import copy
l1=[1,2,3,[4,5]]
l2=copy.deepcopy(l1)
l1[-1].pop()
print(l1)
print(l2)
print(id(l1[-1]))
print(id(l2[-1]))
print(id(l1))
print(id(l2))
l1[-1].append(100)
print(l1)
print(l2)

123 in {1:123}

a=30
b=a
print(a is b)
print(20 is 20)
c=2.2
print(c is 2.2)


s1="HELLO"
s2=s1
print(s1 is s2)
print(s1 is not s2)