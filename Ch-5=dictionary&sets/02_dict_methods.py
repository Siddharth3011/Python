marks = {
    "Siddharth" : 100, 
    54: "Subham",
    "Rohan"  : 23
}

print(marks.items())
print(marks.keys()) #left side wale keys hote hai
print(marks.values()) #right side wale values hote hai
marks.update({"Siddharth": 99, "renuka": 55})
print(marks)

print(marks.get("Siddharth2")) # it returns none
# print(marks["Siddharth2"]) # it give error

Rohan  = marks.pop('Rohan')
print(Rohan)
print(marks)

last_item = marks.popitem()
print(last_item)
print(marks)