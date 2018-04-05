import json
from api_gen import api_gen
from data_collection import data_collection
from news_crawler import news_crawler
from word_tools import word_tools

print ""
print "***Welcome to Edu Bias News Crawler***"
print ""

# API Key Selection
apiKeys = api_gen()
key_repeat = True
while key_repeat:
    try:
        apiKeys.printAllKeys()
        currentAPIKey = str(raw_input("\nSelect an API Key (KeyName|add): ") or "BenPSU")
        if currentAPIKey == 'add':
            print '\nAdd an API Key'
            title = raw_input('\tTitle: ')
            key = raw_input('\tKey: ')
            apiKeys.addKey(title, key)
            print "\n***API Key Added***\n"
        else:
            currentAPIKey = apiKeys.getKey(str(currentAPIKey))
            key_repeat = False
    except Exception as ke:
        print "\n***Invalid Selection***\n"


# Data Collection Module
inputPrompt = "\nRun Data Collection Module (y/n):"
if (str(raw_input(inputPrompt)) == 'y'):
    data = data_collection()
    article_batches = int(raw_input("\tNumber of Article Batches: "))
    data_export = data.collect_articles(article_batches, currentAPIKey)
    # Export Data to File
    print 'Exporting Articles to /data_collection.json'
    j = data_export
    f = open('data_collection.json', 'w')
    print >> f, j
    f.close()
    data_export = json.load(open("data_collection.json"))
else:
    print "Loading Cached Datafile (data_collection.json)"  # Imports Previous JSON Data
    data_export = json.load(open("data_collection.json"))

# Crawler Module
inputPrompt = "\nRun Crawler Module (y/n):"
if (str(raw_input(inputPrompt)) == 'y'):
    crawler = news_crawler()
    crawler_export = crawler.crawl_articles(data_export)
    #Export Data to File
    print 'Exporting Articles to /crawler_export.json'
    j = crawler_export
    f = open('crawler_export.json', 'w')
    print >> f, j
    f.close()
    crawler_export = json.load(open("crawler_export.json"))
else:
    print "Loading Cached Datafile (crawler_export.json)"  # Imports Previous JSON Data
    crawler_export = json.load(open("crawler_export.json"))

# Word Tools Module
inputPrompt = "\nRun Word Tools Module (y/n):"
if str(raw_input(inputPrompt)) == 'y':
    word_tools = word_tools()
    t = word_tools.textToWordCount(crawler_export)
    t = json.dumps(t, indent=4, sort_keys=True)
    print 'Exporting Articles to /word_count_export.json'
    j = t
    f = open('word_count_export.json', 'w')
    print >> f, j
    f.close()