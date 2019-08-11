fp = open('py11/test11.txt')
ln3 = set()
for line in fp.readlines():
    fd = ""
    min = 0
    max = len(line)
    for i in range (min,max,1):
        if line[i].isdigit():
           fd = fd.strip() + line[i]   
        elif fd != "":
            ln3.add(fd.strip())
            fd = ""
           
    if fd != "":
        ln3.add(fd.strip())
print(ln3)
    
fp.close()
