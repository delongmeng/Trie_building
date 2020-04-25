




# Problem 5: Building a Trie in Python
# Before we start let us reiterate the key components of a Trie or Prefix Tree. 
# A trie is a tree-like data structure that stores a dynamic set of strings. 
# Tries are commonly used to facilitate operations like predictive text or 
# autocomplete features on mobile phones or web search.


## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie        
        self.is_word = False
        self.children = {}
    
    def insert(self, char):
        ## Add a child node in this Trie   
        if char in self.children:  
            return None
        
        self.children[char] = TrieNode()
        
        
## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)        
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie        
        current_node = self.root
        
        for char in word:
            if char not in current_node.children:
                current_node.insert(char)     
            current_node = current_node.children[char]
        
        current_node.is_word= True 

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        current_node = self.root
        
        for char in prefix:
            if char not in current_node.children:
                return None
            current_node = current_node.children[char]
        
        return current_node



# Finding Suffixes
# Now that we have a functioning Trie, we need to add the ability to list 
# suffixes to implement our autocomplete feature. 
class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie        
        self.is_word = False
        self.children = {}
    
    def insert(self, char):
        ## Add a child node in this Trie   
        if char in self.children:  
            return None
        
        self.children[char] = TrieNode()            
    
    def suffixes1(self):
        # returns suffixes that have suffixes themselves
        # for example for 'f', this returns 'un', but not 'unction', 'actory'
        suffix = []
            
        if (not self.children) or (not self.is_word):  # this block returns ['un']
            for char, node in self.children.items():    
                for string in node.suffixes1():
                    suffix.append(char + string)                                        
        else:
            suffix.append('')                               
          
        return suffix
    
    
    def suffixes2(self):
        # returns the longest possible suffixes
        # for example for 'f', this returns 'unction', 'actory', but not 'un'
        suffix = []
     
        if self.children:  
            for char, node in self.children.items():    
                for string in node.suffixes2():
                    suffix.append(char + string)                                        
        else:
            suffix.append('')        
        
        return suffix        
        

    def suffixes(self):   
        ## Recursive function that collects the suffix for 
        ## all complete words below this point           
        # combine results of suffixes1 and suffixes2
        return self.suffixes1() + self.suffixes2()


        
        
# Test        
        
MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)        



prefixNode = MyTrie.find('f')

prefixNode.suffixes1()
# ['un']

prefixNode.suffixes2()
# ['unction', 'actory']

prefixNode.suffixes()
# ['un', 'unction', 'actory']

print('\n'.join(prefixNode.suffixes()))
# output:
# un
# unction
# actory



prefixNode = MyTrie.find('a')

prefixNode.suffixes1()
# ['nt']

prefixNode.suffixes2()
# ['nthology', 'ntagonist', 'ntonym']

prefixNode.suffixes()
# ['nt', 'nthology', 'ntagonist', 'ntonym']

print('\n'.join(prefixNode.suffixes()))
# output:
# nt
# nthology
# ntagonist
# ntonym





prefixNode = MyTrie.find('t')

prefixNode.suffixes1()
# []

prefixNode.suffixes2()
# ['rie', 'rigger', 'rigonometry', 'ripod']

prefixNode.suffixes()
# ['rie', 'rigger', 'rigonometry', 'ripod']

print('\n'.join(prefixNode.suffixes()))
# output:
# rie
# rigger
# rigonometry
# ripod





prefixNode = MyTrie.find('trig')

prefixNode.suffixes()
# ['ger', 'onometry']

print('\n'.join(prefixNode.suffixes()))
# output:
# ger
# onometry



