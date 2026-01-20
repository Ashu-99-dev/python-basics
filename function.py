# WAF to convert USD to INR 

def usdToInr(value):
    print(value, "USD =",value*89, "INR")
    # return value*90

# usdToInr(10)

# WAF to find factorial of n

def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    return fact


# print(factorial(5))

# WAF to check wheather a num is even or odd

def evenOrOdd(num):
    if(num%2 == 0):
        print("Even")
    else:
        print("Odd")

# evenOrOdd(10)
# evenOrOdd(3)

def sum(a,b):
    sum =  a+b
    print(sum)
    return sum

# sum(4,5)
# sum(12,34)
# sum(100,200)

def cal_prod(a,b=3):  # b is default parameter
    # defalut values are always comes after non defalut values
    prod = a*b
    print(prod)
    return prod

# cal_prod(4)
# cal_prod(12,34)
# cal_prod(100)


# WAF to print the length of a list without using len() function

list = [1,2,3,4,5,6,7,8,9,10]
cities = ["Delhi", "Mumbai", "Kolkata", "Chennai", "Bangalore"]
heros = ["Ironman", "Thor", "Hulk", "Spiderman", "Captain America"]

def print_length(list):
    print(len(list))

# print_length(list)
# print_length(cities)
# print_length(heros)

# WAF to print the list element in the same line

def print_list(list):
    for i in list:
        print(i,end=" ")
    print("\n")

# print_list(list)
# print_list(cities)
# print_list(heros)