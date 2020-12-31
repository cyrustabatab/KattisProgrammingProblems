


class Trie:
    END_SYMBOL = '*'
    def __init__(self):
        self.root = {}


    def add(self,word):
        current = self.root
        for c in word:
            if c not in current:
                current[c] = {}

            current = current[c]


        current[Trie.END_SYMBOL] = True
    

    def __contains__(self,word):

        current = self.root

        for c in word:
            if c not in current:
                return False
            current = current[c]


        return Trie.END_SYMBOL in current
    

    def delete(self,word):
        current = self.root

        for c in word:
            if c not in current:
                return

            current = current[c]















