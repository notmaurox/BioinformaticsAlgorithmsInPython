def makeInfo( text ):
               #A,C,T,G
    counters = [1,1,1,1]
    sortedText = []
    editText = []
    for i in range(len(text)):
        if text[i] ==  'A':
            sortedText.append( (text[i], counters[0]) )
            editText.append( (text[i], counters[0]) )
            counters[0] = counters[0] + 1
        if text[i] ==  'C':
            sortedText.append( (text[i], counters[1]) )
            editText.append( (text[i], counters[1]) )
            counters[1] = counters[1] + 1
        if text[i] ==  'T':
            sortedText.append( (text[i], counters[2]) )
            editText.append( (text[i], counters[2]) )
            counters[2] = counters[2] + 1
        if text[i] ==  'G':
            sortedText.append( (text[i], counters[3]) )
            editText.append( (text[i], counters[3]) )
            counters[3] = counters[3] + 1
        if text[i] == "$":
            sortedText.append( (text[i], 1) )
            editText.append( (text[i], 1) )
    sortedText.sort()
    return (sortedText,editText)
def lastToFirstMap( text ):
               #A,C,T,G
    counters = [1,1,1,1]
    sortedText = []
    editText = []
    for i in range(len(text)):
        if text[i] ==  'A':
            sortedText.append( (text[i], counters[0]) )
            editText.append( (text[i], counters[0]) )
            counters[0] = counters[0] + 1
        if text[i] ==  'C':
            sortedText.append( (text[i], counters[1]) )
            editText.append( (text[i], counters[1]) )
            counters[1] = counters[1] + 1
        if text[i] ==  'T':
            sortedText.append( (text[i], counters[2]) )
            editText.append( (text[i], counters[2]) )
            counters[2] = counters[2] + 1
        if text[i] ==  'G':
            sortedText.append( (text[i], counters[3]) )
            editText.append( (text[i], counters[3]) )
            counters[3] = counters[3] + 1
        if text[i] == "$":
            sortedText.append( (text[i], 1) )
            editText.append( (text[i], 1) )
    sortedText.sort()
    #print editText
    #print sortedText
    lastToFirstMap = []
    for i in range(len(editText)):
        match = editText[i]
        for j in range(len(sortedText)):
            if sortedText[j] == match:
                lastToFirstMap.append(j)
    return lastToFirstMap
def makeFirstOccurance( firstColumn ):
          # $, A, C, T, G
    occ = [-1,-1,-1,-1,-1]
    for i in range(len(firstColumn)):
        if firstColumn[i][0] == "$" and occ[0] == -1:
            occ[0] = i
        if firstColumn[i][0] == "A" and occ[1] == -1:
            occ[1] = i
        if firstColumn[i][0] == "C" and occ[2] == -1:
            occ[2] = i
        if firstColumn[i][0] == "T" and occ[3] == -1:
            occ[3] = i
        if firstColumn[i][0] == "G" and occ[4] == -1:
            occ[4] = i
    return occ
def makeCountMatrix( text ):
    count  = []
          #$ A C T G
    row = [0,0,0,0,0]
    count.append(row)
    for i in range(1,len(text)+1):
        prevRow = []
        #print text[i-1][0]
        for element in count[i-1]:
            prevRow.append(element)
        if text[i-1][0] == "$":
            prevRow[0] = prevRow[0] + 1
        if text[i-1][0] == "A":
            prevRow[1] = prevRow[1] + 1
        if text[i-1][0] == "C":
            prevRow[2] = prevRow[2] + 1
        if text[i-1][0] == "T":
            prevRow[3] = prevRow[3] + 1
        if text[i-1][0] == "G":
            prevRow[4] = prevRow[4] + 1
        count.append( prevRow )
    #print len(count)
    return count
def betterBWMatching( firstOccur, lastColumn, Pattern, count):
    top = 0
    bottom = len(lastColumn)-1
    while top <= bottom:
        if len(Pattern) != 0:
            symbol = Pattern[len(Pattern)-1]
            Pattern = Pattern[0:len(Pattern)-1] 
            key = -1
            if symbol == '$':
                key = 0
            if symbol == 'A':
                key = 1
            if symbol == 'C':
                key = 2
            if symbol == 'T':
                key = 3
            if symbol == 'G':
                key = 4
            top = firstOccur[key] + count[top][key]
            bottom = firstOccur[key] + count[bottom+1][key] - 1
        else:
            return bottom - top + 1
    return 
fileName = "rosalind_ba9m.txt"
dataFile = open(fileName)
text = dataFile.readline().strip()
#print text
#print len(text)
patternLine = dataFile.readline().strip()
patterns = patternLine.split(" ")
firstAndlast = makeInfo(text)
#print firstAndlast[0]
firstOcc = makeFirstOccurance(firstAndlast[0])
#print firstOcc
#print firstAndlast[1]
countMatrix = makeCountMatrix(firstAndlast[1])
#print countMatrix

out = ""
for pattern in patterns:
    out = out + " " + str(betterBWMatching( firstOcc, firstAndlast[1], pattern, countMatrix))
print out