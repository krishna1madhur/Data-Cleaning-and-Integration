import sys
import re
import operator
filePath = sys.argv[1]

listOfProfessorNames = []
listOfProfessorCourses = [] 

with open(filePath, 'r') as file:
        for line in file:
            splitLine = line.split('-',1)
            listOfProfessorNames.append(splitLine[0])
            temporaryObject = splitLine[1]
            temporaryLength = len(temporaryObject) - 1
            listOfProfessorCourses.append(temporaryObject[1:temporaryLength])
#Code to open the cleaned.txt file and retrieve the data from the file into two lists.
def editDistance(a,b):
    length1 = len(a)
    length2 = len(b)
    indexI ,indexJ = 0,0
    opt = [ [ 0 for indexJ in range(length2) ] for indexI in range(length1) ]
    
    for indexI in range(0,length1):
        opt[indexI][0] = indexI
    for indexJ in range(0,length2):
        opt[0][indexJ] = indexJ
    
    for indexI in range(1,length1):
        for indexJ in range(1,length2):
            if (a[indexI] == b[indexJ]):
                cost = 0
            else:
                cost = 1
            m = cost + opt[indexI-1][indexJ-1]
            n = 1 + opt[indexI-1][indexJ]
            g = 1 + opt[indexI][indexJ-1]
            opt[indexI][indexJ] = min(m,n,g)            
    return opt[length1-1][length2-1]

def jaccard(string1,string2):
    total = len(string1.split()) + len(string2.split())
    l = 0
    if set(string1.split()).intersection(set(string2.split())):
        l = len(set(string1.split()).intersection(set(string2.split())))     
    return l/(total-l)


def distinctCourses(listofCourses):
    listOfCourses = []
    for row in listOfProfessorCourses:
        splitString = re.split(r'[|]\s*', row.title())
        for i in range(0,len(splitString)):
            listOfCourses.append(splitString[i])
    setOfCourses = set(listOfCourses)
    listCourse = list(setOfCourses)
    
    for i in range(0,len(listCourse)-1):
        for j in range(i+1,len(listCourse)):
            count1 = len(re.findall(r'\w+', listCourse[i]))
            count2 = len(re.findall(r'\w+', listCourse[j]))          
            if (count1 < 3 or count2 < 3):
                if (editDistance(listCourse[i], listCourse[j]) < 3):
                    listCourse[j] =listCourse[i]
                else:
                    continue
            else:
                if (editDistance(listCourse[i], listCourse[j]) < 3 and jaccard(listCourse[i], listCourse[j]) > 0.70):
                    listCourse[j] =listCourse[i]
                else:
                    continue
    setOfCourses = set(listCourse)
    print("q1: Number of distinct courses in the dataset: "+ str(setOfCourses.__len__()))

def mostAlignedInterest(listOfProfessorNames,listOfProfessorCourses):
    listOfIndexs = []
    max=0
    prof1=0
    prof2=0
    
    for i in range(0,len(listOfProfessorCourses)):
        if(len(re.findall(r'[|]\s*', listOfProfessorCourses[i])) >=5):
            listOfIndexs.append(i)
        
    for a in listOfIndexs:
        for b in listOfIndexs:
            if(a!=b):
                count=0
                splitString1 = re.split(r'[|]\s*',listOfProfessorCourses[a])
                splitString2 =re.split(r'[|]\s*',listOfProfessorCourses[b])
                for str1 in splitString1:
                    for str2 in splitString2:
                        if (jaccard(str1,str2) > 0.50):
                            count=count+1
                    if(count>max):
                        max=count
                        prof1=a
                        prof2=b
              
    print("q3: Professors having most aligned teaching interests: "+listOfProfessorNames[prof1]+" "+listOfProfessorNames[prof2])        
            
def coursesTaughtByTheys(listOfProfessorNames,listOfProfessorCourses):
    theysList = []
    theys = "theys"
    for item in range(0,len(listOfProfessorNames)):
        if(listOfProfessorNames[item].strip().lower() == theys.lower()):
            theysList = re.split(r'[|]\s*',listOfProfessorCourses[item])
            break
    print("q2: Mithell Theys:")
    for i in theysList:
        print(i+',', end="")
    print("")    
distinctCourses(listOfProfessorCourses)
#q1: Function calling distinct courses

coursesTaughtByTheys(listOfProfessorNames, listOfProfessorCourses) 
#q2: Function calling professor They's courses

mostAlignedInterest(listOfProfessorNames, listOfProfessorCourses)
#q3: Function for most aligned professors

