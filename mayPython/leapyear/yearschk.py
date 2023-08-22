fread = open("C:\\Users\\Little Raj\\PycharmProjects\\mayPython\\leapyear\\data.txt","r")
fwrite =open("C:\\Users\\Little Raj\\PycharmProjects\\mayPython\\leapyear\\leapyears.txt","w")
for line in fread:
    year= int(line.rstrip("\n"))  #line = "1890\n"
if (year %100==0 and year%400==0):
    f.write(str(year)+"\n")
elif(year%100 !=0 and year %4==0):
        f.write(str(year) +"\n")