students = {
    "ritik" : 90,
    "prince" : 99,
    "leena" : 89,
    "sakshit" :87,
    "ram" : 100
}

name = input("Enter student name : ")

try:
    marks = students[name]   # try to get marks
    print(f"{name}'s marks: {marks}")
except KeyError:
    print(f" Student '{name}' not found in the records.")
        