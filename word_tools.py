import re, json
from word_tools_wordcloud import word_tools_wordcloud as wc
import random


class word_tools:
    def __init__(self):  # this method creates the class object.
        self.verbose = 'n'
        self.keywords = ''
        pass

    def grey_color_func(word, font_size, position, orientation, random_state=None,
                        **kwargs):
        return "hsl(0, 0%%, %d%%)" % random.randint(60, 100)

    def textToWordCount(self, inputDictionary):
        # print inputDictionary
        inner_dictionary = inputDictionary["articles"]
        # print len(inner_dictionary)
        # print type(inner_dictionary)
        counter = 0
        exitDictionary = {}
        master_frequency = {}
        while counter < len(inner_dictionary):
            a = inner_dictionary[counter]
            b = a['article']
            frequency = {}
            match_pattern = re.findall(r'\b[a-z]{3,15}\b', b)
            # print b
            for word in match_pattern:
                count = frequency.get(word, 0)
                frequency[word] = count + 1
                master_count = master_frequency.get(word, 0)
                master_frequency[word] = master_count + 1
            b = b.split()
            a['wordFreq'] = frequency
            keyTag = str(counter)
            exitDictionary[keyTag] = frequency
            counter = counter + 1

        t = json.dumps(exitDictionary, indent=4, sort_keys=True)
        j = t
        f = open('single_word_count_export.json', 'w')
        print >> f, j
        f.close()

        outDict = {}
        try:
            print "Attempting to import stopWords.txt"
            stopWords = [line.rstrip('\n') for line in open('stopWords.txt')]
        except Exception as ke:
            print "Warning: stopWords.txt was not found - Using Default Stopwords"
            stopWords = ["com", "not", "http", "https", "said", "news", "bbc", "www", "a", "about", "above", "after",
                         "again", "against", "all", "am", "an", "and", "any", "are", "as", "at", "be", "because",
                         "been", "before", "being", "below", "between", "both", "but", "by", "could", "did", "do",
                         "does", "doing", "down", "during", "each", "few", "for", "from", "further", "had", "has",
                         "have", "having", "he", "he'd", "he'll", "he's", "her", "here", "here's", "hers", "herself",
                         "him", "himself", "his", "how", "how's", "i", "i'd", "i'll", "i'm", "i've", "if", "in",
                         "into", "is", "it", "it's", "its", "itself", "let's", "me", "more", "most", "my", "myself",
                         "nor", "of", "on", "once", "only", "or", "other", "ought", "our", "ours", "ourselves", "out",
                         "over", "own", "same", "she", "she'd", "she'll", "she's", "should", "so", "some", "such",
                         "than", "that", "that's", "the", "their", "theirs", "them", "themselves", "then", "there",
                         "there's", "these", "they", "they'd", "they'll", "they're", "they've", "this", "those",
                         "through", "to", "too", "under", "until", "up", "very", "was", "we", "we'd", "we'll", "we're",
                         "we've", "were", "what", "what's", "when", "when's", "where", "where's", "which", "while",
                         "who", "who's", "whom", "why", "why's", "with", "would", "you", "you'd", "you'll", "you're",
                         "you've", "your", "yours", "yourself", "yourselves"]
        minimumTermCount = int(raw_input("Minimum Term Frequency to Count in JSON (Default: 15): ") or "15")
        for key in master_frequency:
            if master_frequency[key] > minimumTermCount and key not in stopWords:
                outDict[key] = master_frequency[key]

        t = json.dumps(outDict, indent=4, sort_keys=True)
        j = t
        f = open('master_freq.json', 'w')
        print >> f, j
        f.close()

        inputPrompt = "\nCreate Standard WordCloud? (y/n):"
        if (str(raw_input(inputPrompt)) == 'y'):
            wt = wc()
            print 'Exporting WordCloud to /Visualizations/WordCloud.jpg'
            ot = wt.make_wordcloud(outDict, 'Visualizations/WordCloud.jpg')

        inputPrompt = "\nCreate WordCloud From Image? (y/n):"
        if (str(raw_input(inputPrompt)) == 'y'):
            print "Directory for Input Images: InputImages/"
            inputPrompt = "\tJPG Filename (Default: stencil.jpg): "
            filename_in = str(raw_input(inputPrompt) or "stencil.jpg")
            filename = str("InputImages/" + filename_in)
            wt = wc()
            print 'Exporting WordCloud to /Visualizations/WordCloud_IMG_' + filename_in
            file_out = 'Visualizations/WordCloud_Img_' + filename_in
            ot = wt.make_wordcloud_img(outDict, filename, file_out)

        return inputDictionary
