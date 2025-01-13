f = open("file.txt")

# readlines ek baar mei heen sari lines read kr sakta hai 
# lines = f.readlines()

# print(lines, type(lines))

# readline ek baar mein ek heen line read krega 
# line1 = f.readline()
# print(line1, type(line1))

# line2 = f.readline()
# print(line2, type(line2))

# line3 = f.readline()
# print(line3, type(line3))

# isi cheez ko ham while loop se bhi likh sakte hain
line =f.readline()
while(line != ""):
    print(line)
    line = f.readline()

f.close()