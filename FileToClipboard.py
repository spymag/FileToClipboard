import inspect, os

#ask user to give the file location
#(uncoment when code is ready)fname = raw_input("Give file location: ")
#outreach = raw_input("Give the outreach in m for that file: ")


#definitions for debuging only
fname = "FileToParse.txt"
ofile = "Output.txt"
outreach = 15.1
filtered = []
noSpaces = []
inputs = []



# read all the lines from a file and add them to a list
def ReadFileLines(fname):
    with open(fname) as f:
        content = f.readlines()
    return content

#write all the strings to the list
inputs = ReadFileLines(fname)

#remove spaces from the list
for i in range(0,len(inputs)):
    noSpaces.append(inputs[i].split())
#print(noSpaces[1][0][0:3])


#append lines into the filtered list
for i in range(0,len(noSpaces)):

    #if the first figure of the line is equal to the selected outreach...
    if noSpaces[i][0][0:(len(str(outreach)))] == str(outreach):
        #print(noSpaces[i])
        filtered.append(noSpaces[i])
#print(len(filtered[0]))

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





