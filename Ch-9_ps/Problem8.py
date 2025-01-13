with open("this.txt") as f:
    content = f.read()

with open("copy_this.txt","w") as f:
    f.write(content)