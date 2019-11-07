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

with open('wordlist') as f:
    wordlist = f.read().splitlines()

word = "world"
perm_set = [
    ['world'],
    ['w', 'orld']
]

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
    #print("iterating anagrams_list" + "\t"+str(lst))
    combine(lst,'')
    #print(combinations)






    
