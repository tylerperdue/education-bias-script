import json
from api_gen import api_gen
from data_collection import data_collection
from news_crawler import news_crawler

print ""
print "***Welcome to Edu Bias News Crawler***"
print ""

# API Key Selection
apiKeys = api_gen()
key_repeat = True
while key_repeat:
    try:
        apiKeys.printAllKeys()
        currentAPIKey = raw_input("\nSelect an API Key (KeyName|add): ")
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
else:
    print ""

