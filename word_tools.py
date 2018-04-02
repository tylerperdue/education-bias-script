from collections import Counter
import re, string, json, collections

class word_tools:
    def __init__(self):  # this method creates the class object.
        self.verbose = 'n'
        self.keywords = ''
        pass

    def textToWordCount(self,inputDictionary):
        print inputDictionary
        dict = inputDictionary["articles"]
        print len(dict)
        print type(dict)

        counter = 0
        while counter < len(dict):
            a = dict[counter]
            b = a['article']
            frequency = {}

            #print a['article']
            match_pattern = re.findall(r'\b[a-z]{3,15}\b', b)

            print b

            for word in match_pattern:
                count = frequency.get(word, 0)
                frequency[word] = count + 1

            frequency_list = frequency.keys()

            for words in frequency_list:
                print words, frequency[words]

            b = b.split()
            a['wordFreq'] = frequency

            counter = counter + 1
        #   print dict[key]

            #text = pattern.match(text)
            #array = Counter(text.split())
            #key["wordCount"] = array


        dict = a
        print type(dict)
        return inputDictionary

