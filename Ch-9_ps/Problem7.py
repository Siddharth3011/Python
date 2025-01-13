with open("logfile.txt", "r") as f:
    lines = f.readlines()

lineno = 1
for line in lines:
    if("python" in line):
        print(f"python is present in the file, line no: {lineno}")
        break
    lineno += 1

else:
    print("python is not present in the file")
    