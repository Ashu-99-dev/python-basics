# info = {
#     "key" : "value",
#     "name" : "Ashutosh",
#     "learning": "pyhton",
#     "from" : "Apna College",
#     "languages" : ["Python","C++","Java","Javascript"],
#     "tuple" : ("Rahul","Aagam"),
#     "is_Adult": True,
#     "marks" : 99
# }

# print(info)

student = {
    "name" : "Ashutosh Tiwari",
    "subject" : {
        "phy" : 98,
        "maths" : 95,
        "chem" : 98,
        "eng" : 90,
        "it" : 93
    }
}

print(student["subject"]["eng"])
print(student.keys())
print(student.items())

# print(student["name2"]) # error
print(student.get("name2"))  # none

student.update({"city" :"Morena"})
print(student)


collection = {} 
print(type(collection))   # it gives us output dictionary

# to create an empty set 
collection = set()
print(type(collection))


# store following word meaning in a python dictionary:

thing = {
    "table": ["a piece of furniture","list of facts & figure"],
    "cat" : "a small animal"
}

print(thing)

# you are given a list of subjects for students. Assume one classroom is required for 1 subject.
# how many classroom are needed by all students.

classroom = {"python", "java" , "C++" , "python" , "javascript","java", "python" ,"C++" , "C"}
print(classroom)
print(len(classroom))