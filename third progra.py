                #normal use
marks1=94
marks2=25.1
marks3=85.2
marks4=45
marks5=63
print(marks1,marks2,marks3,marks4,marks5)

                 #list used python(mutable)
marks=[94,25.1,85.2,45,63]
print(marks)
print (type(marks))
                   #OR
student=["sahil",95.4,"hyderabad"]
print(student)

                  #list index 
stu= ["sahil",12,51.2,"hyderabad"]
print(stu[3])

                   #OR
student=["sahil",95.4,"hyderabad"]
print(student[0])
student[0]="mira"
print(student)

                 
                 #list slicing
str=["sahil", 12, 52.1,"hyderabad"]
str[0:len(str)]
print(str)
                 # list negative slicing
data=["sahil",12,3.0, "hyderabad","ashis taba"]
data[-3:-1]
print(data)


               #some list method(append) muted
list=[2,1,4]
list.append(9)
print(list)
                
                #some list method(sort)ascending
list=[2,1,4,3]
list.sort()
print(list)
                 #some list method(sort)descending
list=[100,85,125,132,21,87,146,78]
list.sort(reverse=True)
print(list)
                 #OR ascending of str
list=["sahil","papai","sharukh","dip","soumodip"]
list.sort()
print(list)
                #OR descending of str
list=["sahil","papai","sharukh","dip","soumodip"]
list.sort(reverse=True)
print(list)
                   #some list method(reverse)
list=['a','t','y','','k','l','n','b','s','e',]
list.reverse()
print(list)
                    #some list method(insert)
list =[2,5,4]
list.insert(0,8)#changed the before index 
print(list)
                    #some list method(remove)
list=[2,1,3,1]
list.remove(1)#remove the element same but at the first
print(list)
                     #some list method(pop)
list=[2,5,4,1,3,0]
list.pop(2)#remove only particular index
print(list)
                      



                      #tuple used in python (immutable)
tuple=(2,1,3,1)
print(type(tuple))

                       #tuple indexing
tuple=(2,1,3,1)
print(tuple[0])
                        #tuple slicing
tuple=(2,7,9,6)
print(tuple[0:3])
                          #tuple slicing negative slicing
tuple=(2,8,4,5,)
print(tuple[-4:-1])
                         #some methods of tuple(index) findout particular element
tuple=(2,1,7,4,5)
print(tuple.index(4)) 
                  #some methods of tuple(count) count how many times eeturn the element 
tuple=(2,5,2,6,8,8,5,6,1,1,8,4,8,9,8,7,1,8)
print(tuple.count(8))



#QN.1 write a program to ask the user to enter names of their 3 favorite movies &store them in a list

movies=[]
movies.append(input("enter first movie: "))
movies.append(input("enter second movie: "))
movies.append(input("enter third  movie: "))

print(movies) 

#QN.2  WAP to check if a list contains a palindrome of elements .(hint:use copy() method)
   # palindrome mean : when i look  the element first to last same orderd (1,2,3,2,1)

list1 = [1,2,3,2,1]
copy_list1=list1.copy()
copy_list1.reverse()

if(copy_list1==list1):
    print("palindrome")
else:
    ("not palindrome")


#QN.3  WAP to count the number of studentd with the "A"  grade in the following tuple.
#("C","D","A","B","B","A")

grade=["C","D","A","B","B","A"]
grade.sort()
print(grade)
