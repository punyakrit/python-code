#area pof circle
r=eval(input('Enter radius of circle: ' ))
pi=3.14
a= pi* r*r
print(a)







#total cost in gst
price=eval(input('enter the price'))
Gst= (18*price)//100
print ("tax is ", Gst)
print ("total price is ", price+Gst)






#marks of student
print("Enter the marks out of 100")
hindi = int(input("Enter marks in hindi: "))
math = int(input("Enter marks in hindi: "))
english = int(input("Enter marks in hindi: "))
science = int(input("Enter marks in hindi: "))
sst = int(input("Enter marks in hindi: "))
total = hindi+math+english+science+sst
percentage = total/5
print("Aggregate marks:", total)