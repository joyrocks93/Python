'''Write a program to display only those numbers from a list that satisfy the following conditions

The number must be divisible by five
If the number is greater than 150, then skip it and move to the next number
If the number is greater than 500, then stop the loop
'''
a=int(input("Enter total numbers:"))
n=[]
for i in range(0,a):
    ele=int(input())
    n.append(ele)
print("Output:")
for i in range(0,a):
    if(n[i]<=150):
        if n[i]%5==0:
            print(n[i])
    elif n[i]>500:
        break;
