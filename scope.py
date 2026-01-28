name = "ashu"  # global scope
count = 1

def another():
    global count  # declare we're using the global variable
    color = "blue"
    global name # we can't modify global variable in a function
    name += "as"
    print(name)
    count += 1
    print(count)
    def greet(name):
        print(color)
        print(name)
    greet("ashu")
    
another()

