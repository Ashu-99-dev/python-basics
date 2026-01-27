# f = open("demo.txt","r")

# data = f.read()

# print(data)
# print(type(data))
# f.close()


# create a new file "practice.txt" using pyhton. Add the following data in it.

# with open("practice.txt","w") as f:
    # f.write("Hi everyone\nwe are learning File I/O\n" \
    # "using python.\nI like programming in python")

# WAF that replace all occurrences of "python" with "java" in above file.

# with open("practice.txt","r") as f:
#     data = f.read()

# new_data = data.replace("python","Java")
# print(new_data)

# with open("practice.txt","w") as f:
#     f.write(new_data)


# Search if the word "learning" exists in the file or not.
word = "learning"
with open("practice.txt","r") as f:
    data = f.read()
    if(data.find(word) != -1):
        print("Found")
    else:
        print("not found")