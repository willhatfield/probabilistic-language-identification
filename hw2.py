import string
import sys
import math

letter_file = sys.argv[1]
probEng = float(sys.argv[2])
probSpan = float(sys.argv[3])

def get_parameter_vectors():
    '''
    This function parses e.txt and s.txt to get the  26-dimensional multinomial
    parameter vector (characters probabilities of English and Spanish) as
    described in section 1.2 of the writeup

    Returns: tuple of vectors e and s
    '''
    #Implementing vectors e,s as lists (arrays) of length 26
    #with p[0] being the probability of 'A' and so on
    e=[0]*26
    s=[0]*26

    with open('e.txt',encoding='utf-8') as f:
        for line in f:
            #strip: removes the newline character
            #split: split the string on space character
            char,prob=line.strip().split(" ")
            #ord('E') gives the ASCII (integer) value of character 'E'
            #we then subtract it from 'A' to give array index
            #This way 'A' gets index 0 and 'Z' gets index 25.
            e[ord(char)-ord('A')]=float(prob)
    f.close()

    with open('s.txt',encoding='utf-8') as f:
        for line in f:
            char,prob=line.strip().split(" ")
            s[ord(char)-ord('A')]=float(prob)
    f.close()

    return (e,s)
    
def shred(filename):
    '''
    This function parses a .txt file into a dict of character counts, where
    the input file may contain any printable ASCII characters and can be short 
    (e.g. a single word) or long (e.g. an article). Ignores case, i.e. merges 
    'A' and 'a' counts together, and so on (this is known as case-folding). 
    Only counts characters A to Z (after case-folding), ignoring all other 
    characters such as space, punctuations, etc.

    Sample Input/Output functionality:
    Input: "Hi! I'll go :-)"
    Output: {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0,
             'G': 1, 'H': 1, 'I': 2, 'J': 0, 'K': 0, 'L': 2,
             'M': 0, 'N': 0, 'O': 1, 'P': 0, 'Q': 0, 'R': 0,
             'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0,
             'Y': 0, 'Z': 0}

    Returns: dict of character counts
    '''

    boc=dict()
    with open (filename,encoding='utf-8') as f:
        corpus=f.read()
    f.close()
    #convert all lowercase alphabets to uppercase
    corpus=corpus.upper()
    #initialize X
    for a in string.ascii_uppercase:
        boc[a]=0
    for c in corpus:
        if c in string.ascii_uppercase:
            boc[c]+=1
    return boc

def safe_log(p: float) -> float:
    """Natural log with a fallback for p==0 (debug only)."""
    if p <= 0.0:
        return -1e8
    return math.log(p)



def logUnNormPostProb(counts, probs, prior):
    logPrior = safe_log(prior)

    logSumCountProb = 0
    for Xi, Pi in zip(counts, probs):
        if Xi == 0:
            continue

        logPi = safe_log(Pi)
        
        logSumCountProb += Xi * logPi
    
    return logPrior + logSumCountProb
    
def desiredConProb(lang):
    FEng = logUnNormPostProb(counts, e, probEng)
    FSpan = logUnNormPostProb(counts, s, probSpan)

    if lang == "eng":
        diff = FSpan - FEng
    else:
        diff = FEng - FSpan
    
    if diff >= 100:
        return 0
    elif diff <= -100:
        return 1
    else:
        return 1 / (1 + math.exp(diff))



e, s = get_parameter_vectors()
boc = shred(letter_file)

counts = 26 *[0]
for key, value in boc.items():
    counts[ord(key) - ord('A')] = value

def question1():
    print("Q1")

    X1 = counts[0]

    xloge = 0.0 if X1 == 0 else X1 * safe_log(e[0])
    xlogs = 0.0 if X1 == 0 else X1 * safe_log(s[0])

    print(f"{xloge:.4f}")
    print(f"{xlogs:.4f}")

def question2():
    print("Q2")

    totalLogProbE = logUnNormPostProb(counts, e, probEng)
    totalLogProbS = logUnNormPostProb(counts, s, probSpan)

    print(f"{totalLogProbE:.4f}")
    print(f"{totalLogProbS:.4f}")

def question3():
    print("Q3")

    probE = desiredConProb("eng")

    print(f"{probE:.4f}")

question1()
question2()
question3()