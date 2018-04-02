import re


class word_tools:
    def __init__(self):  # this method creates the class object.
        self.verbose = 'n'
        self.keywords = ''
        pass

    def textToWordCount(self, inputDictionary):
        # print inputDictionary
        inner_dictionary = inputDictionary["articles"]
        # print len(inner_dictionary)
        # print type(inner_dictionary)
        counter = 0
        while counter < len(inner_dictionary):
            a = inner_dictionary[counter]
            b = a['article']
            frequency = {}
            match_pattern = re.findall(r'\b[a-z]{3,15}\b', b)
            # print b
            for word in match_pattern:
                count = frequency.get(word, 0)
                frequency[word] = count + 1
            b = b.split()
            a['wordFreq'] = frequency
            counter = counter + 1
        # print type(a)
        return inputDictionary
