# print the element of the following list using a loop
# nums = [1,4,9,16,25,36,49,64,81,100]
# for val in nums:
#     print(val)

# search for a number x in this tuple using loop
val = (1,4,9,16,25,36,49,64,81,100)
# x = int(input("Enter the number: "))
# for num in vals:
#     if(num == x) : 
#         print("Entered number found")
#         break
# else: print("Entered number not found")

# for i in range(1,len(val),2):
#     print(val[i])

# for i(this is iterator) in range(start point,end point , step size)

# for i in range(101): print(i)
# for i in range(100,0,-1): print(i)

# WAP to find the sum of first n numbers(usin while)

num = int(input("Enter the number: "))
i = 1
sum = 0
while i <= num:
    sum += i
    i += 1
print(sum)   

# WAP to find the factorial of first n numbers.

n = int(input("Enter the number: "))
fact = 1
for i in range(1,n+1): fact *= i
print(fact)
