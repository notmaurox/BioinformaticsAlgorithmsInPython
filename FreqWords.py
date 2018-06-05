def Symbol2Number( char ):
    if char == "A":
        return 0
    if char == "C":
        return 1
    if char == "G":
        return 2
    if char == "T":
        return 3
        
def Number2Symbol( num ):
    if num == 0:
        return "A"
    if num == 1:
        return "C"
    if num == 2:
        return "G"
    if num == 3:
        return "T"  

def Pattern2Number( Pattern ):
    if Pattern == "":
        return 0
    lastSymbol = Pattern[len(Pattern)-1]
    prefix = Pattern[0:len(Pattern)-1]
    return (4 * Pattern2Number(prefix)) + Symbol2Number(lastSymbol)
    
def Number2Pattern( index, k ):
    #k used to keep track of k mer we are converting. Each call on k-1 mer
    if k == 1:
        #base case, 1 mer, A = 0, C = 1...
        return Number2Symbol(index)
    prefix = index // 4 #find position of k - 1 mer
    remainder = index % 4 # Find index contribution of last character
    symbol = Number2Symbol(remainder) # use index to determine character
    PrefixPattern = Number2Pattern( prefix, k-1)
    return PrefixPattern + symbol

def hamDist( s1, s2):
    dist = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            dist = dist + 1
    return dist
    
def approxPatternCount( text, pattern, d):
    matches = 0
    for i in range(len(text)-len(pattern)+1):
        dist = hamDist(pattern, text[i:i+len(pattern)])
        if dist <= int(d):
            matches = matches + 1
    return matches
    
def Neighbors( pattern, d):
    if d == 0:
        return ['pattern']
    if len(pattern) == 1:
        return ['A','C','G','T']
    neighborhood = []
    suffixNeighbors = Neighbors(pattern[1:len(pattern)],d)
    for i in range(len(suffixNeighbors)):
        if hamDist(pattern[1:len(pattern)], suffixNeighbors[i]) < d:
            neighborhood.append("A" + suffixNeighbors[i])
            neighborhood.append("C" + suffixNeighbors[i])
            neighborhood.append("T" + suffixNeighbors[i])
            neighborhood.append("G" + suffixNeighbors[i])
        else:
            neighborhood.append(pattern[0] + suffixNeighbors[i])
    return neighborhood
    
def freqWordsWithMismatches( text, k, d):
    freqPatterns = []
    freqWords = ""
    close = [0] * (4**k)
    freqArray = [0] * (4**k)
    for i in range(0,len(text)-k+1):
        hood = Neighbors(text[i:i+k],d)
        for i in range(len(hood)):
            close[Pattern2Number(hood[i])] = 1
    for i in range(len(close)):
        if close[i] == 1:
            freqArray[i] = approxPatternCount(text,Number2Pattern(i,k),d)
    maxCount = max(freqArray)
    for i in range(len(freqArray)):
        if freqArray[i] == maxCount:
            freqPatterns.append(Number2Pattern(i,k))
            freqWords = freqWords + " " + Number2Pattern(i,k)
    return freqWords
    
fileName = "inputA.txt"
dataFile = open(fileName)
text = dataFile.readline().strip()
Param = dataFile.readline().strip().split(" ")
k = int(Param[0])
d = int(Param[1])


print freqWordsWithMismatches( text, k, d)

