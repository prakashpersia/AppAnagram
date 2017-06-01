import time
import itertools
global string
global f,lines
global answer
f = open('wordsEn.txt', 'r')
lines = f.read()

def Display(answer,string,lines):
    a=list()
    b=list()
    for i in range (len(string)):
             a.append(lines[answer+i])
             
    res = " ".join(a)
    
    print(res)

def List_Create(Min_Len,items):
    try:
        start_time = time.time()
        a=list()
        for i in range(len(items)+1):
            for combination in itertools.combinations(items, i):
                a.append(combination)
        res = [''.join(p) for p in a]
        res.sort()
        res.reverse()
        mylist=set(res)
        res=list(mylist)
        res=[i for i in res if len(i) > Min_Len]
        print("--- %s seconds ---" % (time.time() - start_time))
        return res
                
    except KeyboardInterrupt:
        raise()  
                    
def File_Check(Result_Word):
    
    try:
#        f = open('wordsEn.txt', 'r')
#        lines = f.read()
        string= '\n'+str(Result_Word)+'\n'
        answer = lines.find(string)
        if answer == -1:
            pass
        else :
            Display(answer,string,lines)

    except KeyboardInterrupt:
           raise()

try:
    start_time=time.time()
    Result_List = List_Create(4,"omprakashdubey")
    for i in range(len(Result_List)):
        File_Check(Result_List[i])
    print (time.time() - start_time)
#    print " Found %d words in %s seconds " %(,(time.time() - start_time))	

except KeyboardInterrupt:
       raise()                    


         
     
