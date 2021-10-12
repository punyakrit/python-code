
#if else code

num1=eval(input('Enter the First Number : '))
num2=eval(input('Enter the Second Number : '))
if num1<num2:
    print('First Number is smallest')
else:
    print('Second Number is smallest')

    


#    or for if-else



num1=int(input('Enter the First Number : '))
num2=int(input('Enter the Second Number : '))
if num1<num2:
    print('min =', num1 ) if num1<num2 else print('min=', num2)



#finding number of days in month
    



    month=int(input('enter the month (1-12): '))
if month in (1,3,5,7,8,10,12):
    print('no. of days is 31')
elif month in (4,6,9,11):
    print('no. of days is 30')
elif month ==2:
    year = int(input('enter the year:'))
    if year%4==0 and (not(year%100==0)) or year %400==0:
        print('no. of days is 29')
    else:
          print('no. of days is 28')
else:
    print('enter value in range (1-12)')







   #program to prompt a user to enter a day of the week.


day = int(input("Enter the day number: "))
if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")
else:
    print("Invalid input.")  
