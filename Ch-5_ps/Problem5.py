a = {}

name1 = input("Enter your name1: ")
lang1 = input("Enter your language1: ")
a.update({name1: lang1})

name2 = input("Enter your name2: ")
lang2 = input("Enter your language2: ")
a.update({name2: lang2})

name3 = input("Enter your name3: ")
lang3 = input("Enter your language3: ")
a.update({name3: lang3})

print(a)
print(a.keys())
print(a.values())