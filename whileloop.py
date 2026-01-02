# count = 1
# while count <= 100000 :
#     print("hello", count)
#     count += 1


# print(count)

# Print number from 1 to 100
# i = 1 
# while i <= 100:
#     print(i)
#     i += 1

# Print number from 100 to 1
# i = 100
# while i > 0:
#     print(i)
#     i -= 1

# Print the multiplication table of a number n
# n = int(input("Enter the number: "))
# i = 1
# while i <= 10:
#     print(n ,"*", i ,"=", n*i)
#     i += 1

# Print the elements of the following list using a loop
# arr = []
# i = 1
# while i <= n:
#     arr.append(i*i)
#     i += 1
# print(arr)   

# num = int(input("Enter the no. which we want to search: "))
# i = 1
# while i < len(arr):
#     if(num == arr[i]): 
#         continue
#         print("Number is present in th list") 
#     # else : print("Number is not present in the list")
#     i += 1
# print("Number is not present in the list")

# i = 1
# while i <= 10:
#     if(i%2 == 0):
#         i+=1
#         continue
#     print(i)
#     i += 1

# Write a program to print numbers from 1 to 5 using a while loop.
i = 1
while i <=5:
    print(i)
    i += 1

# Find the sum of first n natural numbers using a while loop.
sum = 0 
n = int(input("Enter the number: "))
i = 1
while i <= n:
    sum += i
    i += 1

print(sum)

# Write a program to count the digits of a number.

digi = 1234567
cnt = 0
while digi > 0:
    cnt += 1
    digi //= 10

print(cnt)

# Reverse a number using a while loop.

num = 1234
revNum = 0
while num > 0:
    digi = num % 10
    revNum = revNum*10+digi
    num //= 10

print(revNum)