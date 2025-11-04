#simple calculator by sahil
print ("=====calculator =====")
num1 = float (input("enter fir st number: "))
operator = input("enter operator(+,-,*,/): ")
num2 = float (input("enter second number : "))
if operator  == "+":
    print ("result:", num1+num2)
elif operator =="-":
   print ("result:", num1-num2)
elif operator =="*":
   print ("result:", num1*num2)
elif operator =="/":
 print ("result:", num1/num2)
 print ("invalid operator")

