import os

#ask user to give the file location
#(uncoment when code is ready)fname = raw_input("Give file location: ")
#outreach = raw_input("Give the outreach in m for that file: ")


#definitions for debuging only
fname = "BFV4_instance3_1000T.txt"#BFV4_instance1_0T.txt"
fname1 = "BFV4_instance3_1000T copy 2.txt"
fname2 = "BFV4_instance3_1000T copy 3.txt"
fname3 = ""#BFV4_instance3_1000T.txt"
fname4 = ""
fname5 = ""
fname6 = ""

outreach = 23.00
outreach1 = 15.10
outreach2 = 25.00
outreach3 = 0#15.10
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
noBlanks = []
joinedList = []
noDuplicates = []

def f7(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]

# read all the lines from a file and add them to a list
def ReadFileLines(fname):
    with open(fname) as f:
        content = f.readlines()
    return content



def splitFunction(var):
    out=[]
    for i in range(0,len(var)):
        out.append(var[i].split())
    return out

def removeBlansLists(var):
    out = []
    for i in range(0,len(var)):
        if var[i]!= []:
            out.append(var[i])
    return out

def joinList(var):
    out= []
    for i in range(0,len(var)):
        out.append(" ".join(var[i]))
    return out   

#write all the strings to the list from all the files
for i in range(0,len(filesNumber)):
    if filesNumber[i] != "":
        inputs = (ReadFileLines(filesNumber[i]))
        #print(inputs)
        noSpaces = splitFunction(inputs)
        #print(noSpaces)
        noBlanks = removeBlansLists(noSpaces)
        
        lengths.append(len(joinList(noBlanks)))
        
        joinedList.append(joinList(noBlanks))
        
        #step = reduce(lambda x,y: x+y,joinedList) second way
        flatList = sum(joinedList, [])
        
#print(len(flatList))
#print(lengths)
#print(len(joinedList))
#print(joinedList)

#append lines into the filtered list
for j in range(0,len(joinedList)): # first select the outreach of the each file,
    i=0
    #print(j)
    for i in range(i+flag,lengths[j]+flag): # then iterate through all the list items
        if flatList[i][:len(str("%.2f" % outreachList[j]))]==str("%.2f" % outreachList[j]):
            #print(joinedList[i])
            filtered.append(flatList[i])
            #print(filtered)
    flag = flag + lengths[j]
#print(len(ReadFileLines(filesNumber)[0]))

#remove duplicates
noDuplicates = f7(filtered)    
#print(noDuplicates)

#print ReadFileLines(fname)
with open(ofile, "w") as text_file:
    for i in range(0,len(noDuplicates)):
        text_file.write(noDuplicates[i])
        text_file.write('\n') # add new line every after line
        locations = os.getcwd() +'/'+ str(ofile)
        
print(" %s matches found! and copied to %s" % (str(len(noDuplicates)), locations))
text_file.close()
