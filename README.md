# Trustpilot-code-challenge
This repository holds an algorithm which solves the [Trustpilot code challenge](https://followthewhiterabbit.trustpilot.com/cs/step2.html). The problem statement is as follows:

Unless you know the secret phrase, it will remain hidden.

Can you write the algorithm to find it?

Here is a couple of important hints to help you out:
- An anagram of the phrase is: "poultry outwits ants"
- There are three levels of difficulty to try your skills with
- The MD5 hash of the easiest secret phrase is "e4820b45d2277f3844eac66c903e84be"
- The MD5 hash of the more difficult secret phrase is "23170acc097c24edb98fc5488ab033fe"
- The MD5 hash of the hard secret phrase is "665e5bcb0c20062fe8abaaf4628bb154"

Additonally, a [list of english words](wordlist) is supplied.

# Algorithm
The implemented algorithm utilizes a [trie](https://en.wikipedia.org/wiki/Trie) to store the wordlist. In order to narrow the width and depth of the trie, only words which can be part of an anagram of the original phrase are stored.

The strategy is then to recursively traverse the trie and concatenate words until certain requirements are met. Then, the md5 of the candidate solution is computed and checked against the hashes of the problem statement.