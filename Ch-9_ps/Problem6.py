with open("logfile.txt", "r") as f:
    content = f.read()

if("python" in content):
    print("python is present in the file")

else:
    print("python is not present in the file")
    