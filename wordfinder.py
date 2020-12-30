"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    ...
    
    
    
    def __init__(self, path):
        self.words = open(path, "r")
        print(f"{self.words_read()} words read")
    
    def words_read(self):
        count = 0
        for line in self.words:
            count +=1 
        return count
    
    def random(self):
        word_list = []
        self.words.seek(0)
        for line in self.words:
            word_list.append(line)
        return random.choice(word_list).strip('\n')
    
class SpecialWordfinder(WordFinder):

    def __init__(self, path):
        super().__init__(path)
    
    def random(self):
        word_list = []
        self.words.seek(0)
        for line in self.words:
            if "#" not in line and len(line) > 2 :
                word_list.append(line)
        return random.choice(word_list).strip('\n')
