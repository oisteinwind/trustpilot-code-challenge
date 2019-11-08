def find_anagrams(str):
    anagrams = []
    for word in wordlist:
        if is_anagram(str,word):
            anagrams.append(word)
    return anagrams

def is_anagram(str1,str2):
    return sorted(str1) == sorted(str2)

def combine(terms, accum):
    last = (len(terms) == 1)
    n = len(terms[0])
    for i in range(n):
        item = accum + terms[0][i]
        if last:
            combinations.append(item)
        else:
            combine(terms[1:], item)

def perms(s):        
    if(len(s)==1): return [s]
    result=[]
    for i,v in enumerate(s):
        result += [v+p for p in perms(s[:i]+s[i+1:])]
    return result

def Permute(string):
    if len(string) == 0:
        return ['']
    prevList = Permute(string[1:len(string)])
    nextList = []
    for i in range(0,len(prevList)):
        for j in range(0,len(string)):
            newString = prevList[i][0:j]+string[0]+prevList[i][j:len(string)-1]
            if newString not in nextList:
                nextList.append(newString)
    return nextList

with open('wordlist') as f:
    wordlist_original = f.read().splitlines()

word = "world"

wordlist = [s for s in wordlist_original if len(s) <= len(word)]
perm_set = Permute(word)
print(perm_set)
anagrams_list = []
for perms in perm_set:
    #print("Permutation:\t"+str(perms))
    #['world'] or ['W', 'orld']
    temp_anagrams_list = []
    keep_permutation = True
    i=0
    while i<len(perms):
        #'world' or 'orld' or 'w'
        word = perms[i]
        anagrams = find_anagrams(word)
        #print("word:\t"+word+"\tAnagrams:\t"+str(anagrams)+"\titeration\t"+str(i))
        if (len(anagrams)) == 0:
            keep_permutation = False
            break
        if len(temp_anagrams_list)<i+1:
            temp_anagrams = anagrams
            temp_anagrams_list.append(temp_anagrams)
        else:
            temp_anagrams = temp_anagrams_list[i]
            temp_anagrams.append(anagrams)
            temp_anagrams_list[i] = temp_anagrams
        i+=1
    if keep_permutation:
        anagrams_list.append(temp_anagrams_list)

combinations = []
for lst in anagrams_list:
    combine(lst,'')
print(anagrams_list)