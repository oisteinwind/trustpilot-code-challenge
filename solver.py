import hashlib
# Inspiration from https://towardsdatascience.com/implementing-a-trie-data-structure-in-python-in-less-than-100-lines-of-code-a877ea23c1a1
class TrieNode(object):
    def __init__(self, char: str):
        self.char = char
        self.children = []
        self.word_finished = False

def add_word_to_trie(root: TrieNode, word: str):
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

def keep_word(word: str):
    if len(word) > len(original_phrase):
        return False
    for character in word:
        if character not in original_phrase:
            return False
    return True



def solve_phrases(trie, phrase, word_count):
    '''
    Traverse trie and establish increasingly more complex words (in terms of word count)
    A combination of words is a candidate solution if its length  (without spaces) is equal to the length of the original phrase.
    '''
    def traverse_trie(node:TrieNode, candidate_solution, remaining_letters, current_word_count):
        # print("candidate_solution:\t"+candidate_solution)
        # print("remaining_letters:\t"+remaining_letters)
        # print("current_word_count:\t"+str(current_word_count))
        # print("word_count:\t\t"+str(word_count))
        # input("Press Enter to continue...")
        # If there are no remaining letters, we should either:
        # 1) check if the md5 is matching solution or
        # 2) return if the current node does not represent a full word
        if remaining_letters == "":
            if node.word_finished:
                md5_candidate_solution =  hashlib.md5(candidate_solution.encode()).hexdigest()
                if current_word_count == word_count and md5_candidate_solution in md5_solutions:
                    print('solution:\t'+candidate_solution)
                    print('md5:\t'+str(md5_candidate_solution))
            return
        
        # Else we traverse the children of the current node until we are at the end of a word
        for child_node in node.children:
            # The current node has to have a character in the remaining_letters, otherwise it can not be an anagram
            if child_node.char in remaining_letters:
                # Pick out the character from the current node and remove this character in the remaining_letters
                index = remaining_letters.index(child_node.char)
                updated_remaining_letters = remaining_letters[0:index]+remaining_letters[index+1:]
                # Traverse the trie with the updated remaining letters
                traverse_trie(child_node, candidate_solution + child_node.char, updated_remaining_letters, current_word_count)
        # If we are at the end of a word, there must be remaining letters, so we add new words by traversing the trie once again
        if node.word_finished and current_word_count < word_count:
            traverse_trie(root_trie, candidate_solution + " ", remaining_letters, current_word_count + 1)
    # Initiate the recursion by looking for single words matching the solutions
    traverse_trie(trie, "", phrase, 0)
    # Increase the number of words we're looking for by 1
    solve_phrases(trie, phrase, word_count + 1)

# Set up trie tree for words which are 
# 1) of length less than or equal to length of the original phrase
# 2) have all characters included in the original phrase
original_phrase = "poultry outwits ants".replace(" ","")
root_trie = TrieNode("")
with open('wordlist') as f:
    wordlist = f.read().splitlines()
for word in wordlist:
    if keep_word(word):
        add_word_to_trie(root_trie, word)

# MD5 checksums: Easy, medium, hard
md5_solutions = ["e4820b45d2277f3844eac66c903e84be","23170acc097c24edb98fc5488ab033fe","665e5bcb0c20062fe8abaaf4628bb154"]

solve_phrases(root_trie, original_phrase, 0)