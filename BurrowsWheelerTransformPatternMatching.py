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

def BWMatching( firstColumn, lastColumn, Pattern, LastToFirst):
    top = 0
    bottom = len(lastColumn)-1
    while top <= bottom:
        if len(Pattern) != 0:
            symbol = Pattern[len(Pattern)-1]
            Pattern = Pattern[0:len(Pattern)-1] 
            topIndex = -1
            bottomIndex = -1
            for i in range(top,bottom+1):
                if lastColumn[i][0] == symbol and topIndex == -1:
                    topIndex = i
                    bottomIndex = i
                if lastColumn[i][0] == symbol and topIndex != -1:    
                    bottomIndex = i
            if topIndex == -1 and bottomIndex == -1:
                return 0
            top = LastToFirst[topIndex]
            bottom = LastToFirst[bottomIndex]
        else:
            return bottom - top + 1

fileName = "rosalind_ba9l.txt"
dataFile = open(fileName)
text = dataFile.readline().strip()
patternLine = dataFile.readline().strip()
patterns = patternLine.split(" ")
firstAndlast = makeInfo(text)
lastToFirstMap = lastToFirstMap(text)
out = ""
for pattern in patterns:
    out = out + " " + str(BWMatching( firstAndlast[0], firstAndlast[1], pattern, lastToFirstMap))
print out