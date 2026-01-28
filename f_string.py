person = "AShu"
coins = 3

print("\n" + person + " has " + str(coins) + " coins left")


message = "\n%s has %s coins left" % (person,coins)
print(message)

message = "\n{} has {} coins left".format(person,coins)
print(message)

message = "\n{1} has {0} coins left".format(coins,person)
print(message)

#######
# f-string
print(f"\n{person} has {coins} coins left")
print(f"\n{person.lower()} has {coins} coins left")
print(f"\n{person.upper()} has {2+3} coins left")
print(f"\n{person.title()} has {coins} coins left")

###################
# You can also use f-string to format numbers
num = 10
print(f"\n2.25 times {num} is {2.25 * num:.2f}")

for i in range(1,10):
    print(f"{i} X 2 = {i*2}")


