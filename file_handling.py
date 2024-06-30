# access modes
# read, write and append

# Method 1: READ
with open("demo.txt","r") as fp:
    print(fp.read())
    fp.close()
print()
    
# Method 2: READ
f = open("demo.txt","r")
print(f.read())
f.close()

print()

# Reading contents line by line
c = open("demo.txt","r")
for line in c:
    print(line.strip())

print()

with open("demo.txt","r") as x:
    print(x.readline().strip())

print()

# WRITING TO A FILE
with open("another.txt","a") as d:
    d.write("\nOverwrites existing data")
    