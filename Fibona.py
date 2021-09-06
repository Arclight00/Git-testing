# Write a Python program to get the Fibonacci series between 0 to 50.


#x,y=0,1

# while y<50:
#     print(y,end=" ")
#     x,y = y,x+y

first_num=0
second_num=1
emp=[]
for i in range(7):
    if i==1:
        emp.append(1)
    else:
        emp.append(second_num)
        first_num=second_num
        second_num=first_num+emp[i-1]

print(emp)
