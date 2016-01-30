#ask user to give the file location
#(uncoment when code is ready)fname = raw_input("Give file location: ")
#outreach = raw_input("Give the outreach in m for that file: ")


#definitions for debuging only
fname = "FileToParse.txt"
outreach = 15.1
filtered = []
noSpaces = []


# read all the lines from a file and add them to a list
def ReadFileLines(fname):
    with open(fname) as f:
        content = f.readlines()
    return content

#print ReadFileLines(fname)[7]
#print len(str(outreach))

#remove spaces
for i in range(0,len(ReadFileLines(fname))):
    
   noSpaces.append(ReadFileLines(fname)) 


#append lines into the filtered list
for i in range(0,len(ReadFileLines(fname))):

    #if the first figure of the line is equal to the selected outreach...
    if ReadFileLines(fname)[i][0:(len(str(outreach)))] == str(outreach):
        #print(ReadFileLines(fname)[i])
        filtered.append(ReadFileLines(fname)[i])

#print ReadFileLines(fname)
with open("Output.txt", "w") as text_file:
    for i in range(0,len(filtered)):
        text_file.write(filtered[i])
print(filtered)
