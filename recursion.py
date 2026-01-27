
# Print number n to 1 using recursion

def revcount(n):
    if(n == 0):
        return
    print(n,end=" ")
    revcount(n-1)

# revcount(7)
# print()

# WAF to calculate the sum of first n natural numbers

def sum(n):
    if(n == 1):
        return 1
    return n + sum(n-1)

# print(sum(5))

cities = ["agar","morena","gwalior","jhansi","bhind","delhi","noida"]

# length = len(cities)

def print_elements(list,ind):
    if(ind == len(list)):
        return 
    print(list[ind],end=" ")
    print_elements(list,ind+1)

print_elements(cities,0) 