sums = lambda x, y : x + y
def add(x, y): return x + y
print(sums(5, 10))
print(add(5, 10))

addTwo = lambda x : x + 2
print(addTwo(5))

multiply = lambda x, y,z : x * y * z
print(multiply(5, 10, 2))

def funBuilder(x):
    return lambda num : num + x

addTen = funBuilder(10)
addTwenty = funBuilder(20)

print(addTen(5))
print(addTwenty(5))


#################################################################
# high order functions

#lambda num : num * num
number = [1,2,3,4,5,6,7,8,9,10]

squared_number = list(map(lambda num : num * num, number))
print(squared_number)


#################################################################
# filter

number = [1,2,3,4,5,6,7,8,9,10]

even_number = list(filter(lambda num : num % 2 == 0, number))
print(even_number)


#################################################################
# reduce

from functools import reduce

number = [1,2,3,4,5,6,7,8,9,10]

sum_number = reduce(lambda x, y : x + y, number)
print(sum_number)

print(sum(number))

names = ["Ashutosh", "Ashish", "Ashish", "Ashish", "Ashish", "Ashish", "Ashish", "Ashish", "Ashish", "Ashish"]

print(list(map(lambda name : name.upper(), names)))

print(list(filter(lambda name : name.startswith("A"), names)))

print(reduce(lambda x, y : x + len(y), names, 0))