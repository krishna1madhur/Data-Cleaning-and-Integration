import sys
import operator
filePath = sys.argv[1]

listOfProfessorNames = []
listOfProfessorCourses = []
listOfProfessorLastNames = []
 
with open(filePath, 'r') as file:
    for line in file:
        splitLine = line.split('-',1)
        listOfProfessorNames.append(splitLine[0])    
        temporaryObject = splitLine[1]
        temporaryLength = len(temporaryObject) - 1
        listOfProfessorCourses.append(temporaryObject[1:temporaryLength])

listOfProfessorNames = [fullName.replace('.', ' ') for fullName in listOfProfessorNames]
#===============================================================================
# Replace all dots with whitespace characters
#==============================================================================

for name in listOfProfessorNames:
    temporaryName = []
    if ',' in name:
        name= name.title()
        temporaryName = name.split(',')
        
        listOfProfessorLastNames.append(temporaryName[0])
    else:
        name = name.title()
        temporaryName = name.split()
        totalCountOfNames = temporaryName.__len__()
        listOfProfessorLastNames.append(temporaryName[totalCountOfNames - 1])
#===============================================================================
# Code below is for finding the edit distance between two strings a and b
#===============================================================================
def editDistance(a,b):
    len1 = len(a)
    len2 = len(b)
    i ,j = 0,0
    opt = [ [ 0 for j in range(len2) ] for i in range(len1) ]
    
    for i in range(0,len1):
        opt[i][0] = i
    for j in range(0,len2):
        opt[0][j] = j
    
    for i in range(1,len1):
        for j in range(1,len2):
            if (a[i] == b[j]):
                cost = 0
            else:
                cost = 1
            m = cost + opt[i-1][j-1]
            n = 1 + opt[i-1][j]
            g = 1 + opt[i][j-1]
            opt[i][j] = min(m,n,g)
            
    return opt[len1-1][len2-1]      
#===============================================================================
# Code above is for finding the edit distance between two strings a and b
#===============================================================================

#===============================================================================
# Code in the below block obtained for autocorrect library of spelling from http://norvig.com/spell-correct.html
#===============================================================================
import re, collections

def words(text): return re.findall('[a-z]+', text.lower())
text_file = open("wordlist.txt",'r')

def train(features):
    model = collections.defaultdict(lambda: 1)
    for f in features:
        model[f] += 1
    return model
NWORDS = train(words(text_file.read()))
alphabet = 'abcdefghijklmnopqrstuvwxyz'
def edits1(word):
    splits     = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes    = [a + b[1:] for a, b in splits if b]
    transposes = [a + b[1] + b[0] + b[2:] for a, b in splits if len(b)>1]
    replaces   = [a + c + b[1:] for a, b in splits for c in alphabet if b]
    inserts    = [a + c + b     for a, b in splits for c in alphabet]
    return set(deletes + transposes + replaces + inserts)

def known_edits2(word):
    return set(e2 for e1 in edits1(word) for e2 in edits1(e1) if e2 in NWORDS)

def known(words): return set(w for w in words if w in NWORDS)

def correct(word):
    candidates = known([word]) or known(edits1(word)) or known_edits2(word) or [word]
    return max(candidates, key=NWORDS.get)

#===============================================================================
# Code in the above block obtained for autocorrect library of spelling from http://norvig.com/spell-correct.html
#===============================================================================

listOfCourses = []
for row in listOfProfessorCourses:
    if '&' in row:
        row = row.replace('&','And')
    splitString = re.split(r'[|]\s*', row.title())
    listOfCourses.append(splitString)
#Divide into tokens, replace & with And and capitalizing first letters

dictionary = dict(zip(listOfProfessorLastNames , listOfProfessorCourses))

for eachProfessor in dictionary.keys():
    sameProfessorCourseList = []
    for j in range(0,len(listOfProfessorLastNames)):
        if(eachProfessor == listOfProfessorLastNames[j]):
            sameProfessorCourseList.append(j)
    for k in sameProfessorCourseList:
            if(dictionary[eachProfessor]!=listOfProfessorCourses[k]):
                dictionary[eachProfessor] = dictionary[eachProfessor] +'|'+ listOfProfessorCourses[k]

for eachProfessor in dictionary.keys():
    sampleCoursesList = []
    coursesString = ''
    courseSet = dictionary[eachProfessor]
    coursesStringList = []
    if '&' in courseSet:
        courseSet = courseSet.replace('&','And')
    if '-' in courseSet:
        courseSet = courseSet.replace('-',' ')
    sampleCoursesList = re.split(r'[|]\s*', courseSet.lower())
    for course in sampleCoursesList:
        tokenList = []
        mergedString = ""
        tokenList = re.split(r'[:;,|.\s]\s*', course.lower())
        for token in tokenList:
            if(len(token)>2):
                processed_text= correct(token)
            else:
                processed_text = token        
            if(token =="ii"):
                token = "II"
            elif(token == 'i'):
                token = 'I'
            if(token == "Introduction"):
                token = "Intro "
            elif(token == "Intro."):
                token = "Intro "
            elif(token == "intro "):
                token = "Intro "
            mergedString = mergedString +' '+processed_text
            mergedString = mergedString.lstrip() 
        coursesStringList.append(mergedString)   
    coursesStringList.sort()
    for course in coursesStringList:
        if (coursesString == ""):
            coursesString = course.title()
        elif course.title() in coursesString: 
            continue  
        else:        
            coursesString = coursesString + '|' + course
            coursesString = coursesString.title()
                
    dictionary[eachProfessor] =coursesString    


sorted_x = sorted(dictionary.items(), key=operator.itemgetter(0))

output_file = open("cleaned.txt", "w")
output_file.writelines(["%s  - %s\n" % item  for item in sorted_x])
text_file.close()

