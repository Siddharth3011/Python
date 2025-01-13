words = ["Donkey", "bad", "horror"]
with open("newfile.txt") as f:
    content = f.read()

for word in words:
    content = content.replace(word, "#"*len(word))

with open("newfile.txt","w") as f:
    content = f.write(content)
