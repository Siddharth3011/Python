word = "Donkey"
with open("file.txt") as f:
    content = f.read()

newcontent = content.replace("Donkey", "#####")

with open("file.txt","w") as f:
    content = f.write(newcontent)
