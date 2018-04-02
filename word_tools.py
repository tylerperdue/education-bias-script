import re


class word_tools:
    def __init__(self):  # this method creates the class object.
        self.verbose = 'n'
        self.keywords = ''
        pass

    def textToWordCount(self, inputDictionary):
        #print inputDictionary
        dict = inputDictionary["articles"]
        #print len(dict)
        #print type(dict)
        counter = 0
        while counter < len(dict):
            a = dict[counter]
            b = a['article']
            frequency = {}
            match_pattern = re.findall(r'\b[a-z]{3,15}\b', b)
            #print b
            for word in match_pattern:
                count = frequency.get(word, 0)
                frequency[word] = count + 1
            frequency_list = frequency.keys()
            b = b.split()
            a['wordFreq'] = frequency
            counter = counter + 1
        #print type(a)
        return inputDictionary
