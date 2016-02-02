import os

#ask user to give the file location
#(uncoment when code is ready)fname = raw_input("Give file location: ")
#outreach = raw_input("Give the outreach in m for that file: ")


#definitions for debuging only
fname = "FileToParse.txt"
fname1 = "FileToParse1.txt"
fname2 = "FileToParse2.txt"
fname3 = ""
fname4 = ""
fname5 = ""
fname6 = ""

outreach = 15.1
outreach1 = 30
outreach2 = 25
outreach3 = 0
outreach4 = 0
outreach5 = 0
outreach6 = 0

ofile = "Output.txt"
filtered = []
noSpaces = []
inputs = []
filesNumber = [fname,fname1,fname2,fname3,fname4,fname5,fname6]
outreachList = [outreach,outreach1,outreach2,outreach3,outreach4,outreach5,outreach6]
flag = 0
lengths = []



# read all the lines from a file and add them to a list
def ReadFileLines(fname):
    with open(fname) as f:
        content = f.readlines()
    return content

#print(len(filesNumber))
#print(len(ReadFileLines(filesNumber[1])))



#create a list with the lengths of each file filtering out the blank lines
for i in range(0,len(filesNumber)):
    if filesNumber[i] != "":
        temp = ReadFileLines(filesNumber[i])
        #print(temp)
        lengthunit = 0
        for i in range(0,len(temp)):           
            if temp[i] != "\n":
                lengthunit =lengthunit + 1
        lengths.append(lengthunit)
        #print(ReadFileLines(filesNumber[i]))
    
#print(lengths)    

#print len(ReadFileLines(filesNumber[0]))

#write all the strings to the list from all the files
for i in range(0,len(filesNumber)):
    if filesNumber[i] != "":
        #inputs = ReadFileLines(filesNumber[i])
        inputs.extend(ReadFileLines(filesNumber[i]))

#print(inputs)
#remove spaces from the list
for i in range(0,len(inputs)):
    noSpaces.append(inputs[i].split())
#print(noSpaces)
#print ((lengths[0])+12)

#remove empty strings from the list
noBlanks = filter(None, noSpaces)
#print(noBlanks)

#append lines into the filtered list
for j in range(0,len(lengths)): # first select the outreach of the each file,
    i=0
    for i in range(i+flag,lengths[j]+flag): # then iterate through all the list items

        #if the first figure of the line is equal to the selected outreach...
        if noBlanks[i][0][0:(len(str(outreachList[j])))] == str(outreachList[j]):
            #print(noBlanks[i])
            filtered.append(noBlanks[i])
    flag = flag + lengths[j]
#print(len(ReadFileLines(filesNumber)[0]))

#print(filtered)
a
#print ReadFileLines(fname)
with open(ofile, "w") as text_file:
    for i in range(0,len(filtered)):
        for j in range(0,len(filtered[i])):
            text_file.write(filtered[i][j])
            text_file.write(' ')# add space for each list item
        text_file.write('\n') # add new line every after line
        locations = os.getcwd() +'/'+ str(ofile)
        
print(" %s matches found! and copied to %s" % (str(len(filtered)), locations))
text_file.close()
