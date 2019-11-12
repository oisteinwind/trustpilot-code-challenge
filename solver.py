import hashlib
from random import shuffle

class TrieNode(object):
    '''
    A TrieNode is an object consisting of a specific character, a list of children (of TrieNode objects), and a flag stating whether the node represents the end of a word.
    '''
    def __init__(self, char: str):
        self.char = char
        self.children = []
        self.word_finished = False

class AnagramProblemSet(object):
    def __init__(self, trie:TrieNode, original_phrase:str, md5_solutions:[]):
        self.trie = trie
        self.original_phrase = original_phrase
        self.md5_solutions = md5_solutions

def add_word_to_trie(root: TrieNode, word: str):
    '''
    This method adds a specific word to the trie.
    '''
    node = root
    for char in word:
        found_in_child = False
        # Search for the character in the children of the present `node`
        for child in node.children:
            if child.char == char:
                # And point the node to the child that contains this char
                node = child
                found_in_child = True
                break
        # We did not find it so add a new chlid
        if not found_in_child:
            new_node = TrieNode(char)
            node.children.append(new_node)
            # And then point node to the new child
            node = new_node
    # Everything finished. Mark it as the end of a word.
    node.word_finished = True

def keep_word(original_phrase, word):
    '''
    This method determines whether or not we should add the word to the trie.
    '''
    if not word:
        return False    
    # If the word is longer than the entire original phrase, it cannot be an anagram of it.
    if len(word) > len(original_phrase):
        return False
    # Each character in the word has to be found in the original phrase, otherwise it cannot be an anagram of it.
    for character in word:
        if character not in original_phrase:
            return False
    return True

def traverse_trie(trie_node, candidate_solution, remaining_letters, current_word_count, word_count, problemSet:AnagramProblemSet):
    '''
    Traverse the trie and look for solutions.
    '''
    if trie_node.word_finished:
        # If there are no remaining letters, we should either:
        # 1) check if the md5 is matching solution or
        # 2) return if the current node does not represent a full word
        if remaining_letters == "":
            if trie_node.word_finished:
                md5_candidate_solution =  hashlib.md5(candidate_solution.encode()).hexdigest()
                if current_word_count == word_count and md5_candidate_solution in problemSet.md5_solutions:
                    print('solution:\t'+candidate_solution)
                    print('md5:\t'+str(md5_candidate_solution))
            return
        # At this point, there must be remaining letters, so we add new words by traversing the root trie once again
        if current_word_count < word_count:
            traverse_trie(problemSet.trie, candidate_solution + " ", remaining_letters, current_word_count + 1, word_count, problemSet)

    # Else we traverse the children of the current node until we are at the end of a word
    for child_node in trie_node.children:
        # The current node has to have a character in the remaining_letters, otherwise it cannot be an anagram
        if child_node.char in remaining_letters:
            # Pick out the character from the current node and remove this character in the remaining_letters
            index = remaining_letters.index(child_node.char)
            updated_remaining_letters = remaining_letters[0:index]+remaining_letters[index+1:]
            # Traverse the node with the updated remaining letters
            traverse_trie(child_node, candidate_solution + child_node.char, updated_remaining_letters, current_word_count, word_count, problemSet)

def solve_phrases(word_count:int, problemSet:AnagramProblemSet):
    '''
    Traverse trie and establish increasingly more complex words (in terms of word count)
    A combination of words is a candidate solution if its length  (without spaces) is equal to the length of the original phrase.
    '''
    # Initiate the recursion by looking for single words matching the solutions
    print("---------------------------------\n"+"Solving for phrases of word_count:\t"+str(word_count))
    traverse_trie(problemSet.trie, "", problemSet.original_phrase, 1, word_count, problemSet)

    # Increase the number of words we're looking for by 1
    solve_phrases(word_count + 1, problemSet)

def main():
    '''
    Initialize a trie and solve for matching phrases.
    '''
    # Set up trie tree for words which are 
    # 1) of length less than or equal to length of the original phrase
    # 2) have all characters included in the original phrase
    original_phrase = "poultry outwits ants".replace(" ","")
    root_trie = TrieNode("")
    with open('wordlist') as f:
        wordlist = f.read().splitlines()
        # We randomize the wordlist to enable parallelization
        shuffle(wordlist)
    for word in wordlist:
        if keep_word(original_phrase, word):
            add_word_to_trie(root_trie, word)

    # MD5 checksums: Easy, medium, hard
    md5_solutions = ["e4820b45d2277f3844eac66c903e84be","23170acc097c24edb98fc5488ab033fe","665e5bcb0c20062fe8abaaf4628bb154"]
    problemSet = AnagramProblemSet(root_trie, original_phrase, md5_solutions)

    # Start solving for correct phrases by considering a single word initially
    solve_phrases(1, problemSet)

if __name__ == "__main__":
    main()