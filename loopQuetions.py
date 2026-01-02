# Write a program to print numbers from 1 to 10 using a for loop.
for i in range(11): print(i)

# Write a program to print even numbers between 1 and 20.
for i in range(1,21):
    if(i%2 == 0): print(i)

# Print the multiplication table of a given number.
n = int(input("Enter the number: "))
for i in range(1,11): print(n ,"*" ,i ,"=" ,n*i)

# Write a program to print all numbers in reverse order from n to 1.
n = 14
for i in range(n,0,-1): print(i)

# Use a loop to print each character of a string.

str = "AshutoshTIwari"
for i in str:
    print(i)