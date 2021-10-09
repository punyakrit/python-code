#print a b c d with for loop


for i in range(65,91):
    print(chr(i),end=' ')









#larget number
    

num1=int(input('enter the number: '))
num2=int(input('enter the number: '))
num3=int(input('enter the number: '))
num4=int(input('enter the number: '))
sum=num1+num2+num3+num4
for i in range(sum):
    if i==num1 or i==num2 or i==num3 or i==num4:
        large=i
        
print('largest:',large)      

