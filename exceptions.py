x = 10
try:
    #print(x/1)
    if not type(x) is str:
        raise Exception("x is not a string")
except NameError:
    print("name error means something is not defined")
except ZeroDivisionError:
    print("zero division error means you are trying to divide a number by zero")
except Exception as e:
    print(e)
else:
    print("no error")
finally:
    print("finally block will always execute")