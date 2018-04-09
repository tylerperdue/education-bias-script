import json
import requests


class data_collection:
    def __init__(self):  # this method creates the class object.
        self.verbose = 'n'
        self.keywords = ''
        pass

    def get_keywords(self):
        file = open('keywords.txt', 'rt')
        keyword_string = ""
        first = True
        for x in file:
            term = x.replace(" ", "%20")
            if first:
                keyword_string = keyword_string + term
                first = False
            else:
                keyword_string = keyword_string + '%20OR%20' + term
        self.keywords = keyword_string


    def select_sources(self):
        sources = ""
        print ""
        print "Select Sources"

        sourceList = ["abcnews", "al-jazeera-english", "associated-press", "bbc-news", "bloomberg", "cbs-news", "cnn",
                      "msnbc", "the-politico", "the-economist", "the-huffington-post", "the-new-york-times",
                      "the-washington-post"]
        for x in sourceList:
            curr_source = x
            inputPrompt = "\t" + curr_source + " (y/n): "
            if (str(raw_input(inputPrompt)) == 'y'):
                if (sources != ""):
                    sources = sources + "," + curr_source
                else:
                    sources = sources + curr_source

        return sources

    def collect_articles(self, numPages, apiKey):
        # Returns json data for articles matching bias keywords
        # Json data includes: source, title, and url
        sourceList = self.select_sources()

        print "Collecting Articles from News API.."
        # result is a list of json (dictionary) objects obtained through the News API requests
        result = []
        # counter is used to count the number of articles we are using for analysis
        # incremented every time a article is found in the responses
        counter = 0

        # News Sources: ABC News, Al Jazeera English, Associated Press, BBC News, Bloomberg, CBS News, CNN,
        # MSNBC, Politico, The Economist, The Huffington Post, The New York Times,
        # Time,The Washington Post.

        # page_number represents a page of results, we change the page in the request to get other articles
        page_number = 1
        # keywords are pulled and parsed from text file
        self.get_keywords()
        # outputed json file that will be added to as articles are parsed, each article will be a dictionary object containing source, title, and url
        data = {'articles': []}
        while page_number <= numPages:
            print "Page: " + str(page_number)
            # 100 Requests - Limited to 1000 Requests Per Day.
            # Returns a maximum of 100 articles per request using the pageSize=100 parameter.
            # Have to increment page number in order to gather all results, limited buffer size of 10,000
            # Max amount of articles we are able to retrieve is 10,000 unless we incrementally decrease pageSize
            # Change API key if needed in both URLs defined below
            if page_number == numPages:
                url = 'https://newsapi.org/v2/everything?sources=' + sourceList + '&pageSize=99&page=' + str(
                    page_number) + '&q=' + self.keywords + '&apiKey=' + apiKey
            else:
                url = 'https://newsapi.org/v2/everything?sources=' + sourceList + '&pageSize=100&page=' + str(
                    page_number) + '&q=' + self.keywords + '&q=&apiKey=' + apiKey
            response = requests.get(url)
            response = json.loads(response.text)
            # Add result of request to result list
            result.append(response)
            # Looping through each article to make sure we have access to the article information and to provide a
            # visual when running the script.
            try:
                for article in response['articles']:
                    counter = counter + 1
                    # Prints name of source and the titel of the article
                    if self.verbose == 'y':
                        print article['source']['name'], article['title']
                    # Add article to ouput
                    article = {'source': article['source']['name'], 'title': article['title'], 'url': article['url']}
                    data['articles'].append(article)
            except KeyError:
                print "Maximum amount of daily requests reached."
            page_number = page_number + 1
        json_data = json.dumps(data, indent=4, sort_keys=True)
        j = json_data
        f = open('web_sources.json', 'w')
        print >> f, j
        f.close()
        print "Finished Collecting Articles from News API."
        print str(counter) + " total articles collected."
        return json_data
