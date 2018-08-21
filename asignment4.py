#ques 1
lst=[1,2,3,4,5]
lst.reverse()
print(lst)

#ques 2
strt=input("enter the string")
null=" "
for i in strt:
    if i.isupper():
        null=null+i+','
print(null)

#ques 3
lst=[]
lst1=[]
p=input()
lst=p.split(',')
for i in range (len(lst)):
    lst1.append(int(lst[i]))
print(type(lst1[0]))
print(lst1)

#ques 4
number=(input('enter no'))
temp=number
rev=number[::-1]
if(temp==rev):
    print("pallindrome")
else:
    print("not a pallindrome")

#ques 5
#shallow copy
import copy as c
list1=[1,2,[3,4],5]
list2=c.copy(list1)
list1[2][0]='sam'
print(list1)
print(list2)

#ques 6
#deep copy
import copy as c
list1=[1,2,[3,4],5]
list2=c.deepcopy(list1)
list1[2][1]='sam'
print(list1)
print(list2)
