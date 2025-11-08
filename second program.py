                             #escape sequence charecter \n
str1="sahil hossain\ni am studying from cse branch ."
print (str1)

                             #escape sequence charecter \t
line1 = "fardi hossain \t i am  maried person \ti am work now it tech as a developer  "
print(line1)

                             #string operation (concatenation)
str1= "sahil hosain." 
""
str2= "fardi hossain"
final_str= (str1+str2)
print(final_str)

                             #string operation (indexing)
str1="sahil hossain"
index=str1[9]
print (index)

                             #string operation (slicing)
str2="sahil hossain"
slice=str2[4:9]
print(slice)

                             #string operation (negative slicing)
str3="sahil hossain"
slice=str3[-5:-1]
print(slice)

                             # string function length (len)
line="fardi hossain"
len1= len(line)
print (len1)

line1="fardi"
len2=len(line1)
print(len2)

line2="hossain"
len3=len(line2)
print(len3)

final_str=(line1+line2)
print (final_str)
print(len(final_str))

                           #string function endswith(true/false)
variable1="i am studying from apna college"
variable2=variable1.endswith("ege")
print (variable2)
          #OR
variable3=variable1.endswith("age")
print (variable3)

                            #string function (capitalize)
variable4="i am studying python "
variable4= variable4.capitalize()
print(variable4)

                           #string function (replace)
str1="i am studying python from apna collaege"
str = str1.replace("o","a")
print (str)
           #OR
str2=str1.replace("python","javascript")
print (str2)


                           #string function (find)
str1="i am sahil study on iit from rukre "
str1=str1.find("s")
print (str1)

                            #string function (count / occurence)
str2="i am sahil from west bengal  studied at  iit from rukre"
str2=str2.count("from")
print (str2)

#QN.1   write a program to input user's first name and print its length

name = str(input("enter you : "))
print("length of you", len(name ))

          #OR
name1= str(input("enter your qualification:"))
print("length of this:-",len(name1))



#QN.2  write a program to find the occurence of '$' in a string 

school="hi, $i passed out $ from lakhuria high $ school"
school=school.count("$")
print(school)

                       #conditional statement (if/elif/else)syntax


light ="green"

if(light=="red"):
    print("stop")
elif(light=="green"):
    print("go")
elif(light=="yellow"):
    print("look")

       #OR
age = 20

if(age >= 18):
    print ("i can vote")
elif(age <= 18):
    print("i cant vote")
else:
    print("i make voter card")

             # grade student based on  marks

marks=int(input("enter student marks:-"))

if(marks>=90):
    grade="A"
elif(marks>=80 and marks<90):
    grade="B"
elif(marks>=70 and marks< 80):
    grade="C"
else:
    grade="D"
print("grade of the student ->", grade)



                #nesting mean (writing one stement inside another statement)

age = 95

if(age>=18):
    if(age>=80):
        print("cant drive")
    else:
        print ("can drive")

else:
    print("cant drive")

#QN.1  write a program to check if a number entered by the user is odd or even

num=int(input("enter your number:-"))
if(num%2==0):
    print("EVEN")
else:
    print("ODD")
 
 #QN.2 write a program to find the greatest of 3 numbers entered by the users 

num1=int(input("enter your first number:-"))
num2=int(input("enter your second number:-"))
num3= int (input("enter your third number:-"))


if(num1>=num2 and num1>= num3):
    print ("first number is largest",num1)
elif(num2>=num3):
    print("second number is largest",num2)
else:
    print ("third  number is largest",num3)
              #OR

a=int(input("enter the first number "))
b=int (input ("enter the second number"))
c=int (input("enter the third number"))
if(a>=b):
    print ("first number is largesrt",a)
elif (b>=c):
    print ("second number is the largest",b)
elif (c>=a):
    print ("third number is the largest ",c)

#QN.3 write a programe to check if a number is a multiple 7 or not

a=int(input("enter the number :-"))

if(a % 7==0):
    print("multiple of 7")
else:
    print ("not multiple of 7")


