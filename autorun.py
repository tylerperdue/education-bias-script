import json
from api_gen import api_gen
from data_collection import data_collection
from news_crawler import news_crawler

print ""
print "***Welcome to Edu Bias News Crawler***"
print ""

# API Key Selection
apiKeys = api_gen()
apiKeys.printAllKeys()
key_repeat = True
while key_repeat:
    try:
        currentAPIKey = apiKeys.getKey(str(raw_input("\nSelect an API Key: ")))
        key_repeat = False
    except KeyError as ke:
        print "\n***Invalid Selection***\n"
        apiKeys.printAllKeys()

# Data Collection Module
inputPrompt = "\nRun Data Collection Module (y/n):"
if (str(raw_input(inputPrompt)) == 'y'):
    data = data_collection()
    article_batches = int(raw_input("\tNumber of Article Batches: "))
    data_export = data.collect_articles(article_batches, currentAPIKey)
    print 'Exporting Articles to /data_collection.json'
    json.dump(data_export, open("data_collection.json", 'wt'))
else:
    print "Loading Cached Datafile (data_collection.json)"  # Imports Previous JSON Data
    data_export = json.load(open("data_collection.json"))

# Crawler Module
inputPrompt = "\nRun Crawler Module (y/n):"
if (str(raw_input(inputPrompt)) == 'y'):
    crawler = news_crawler()
    crawler_export = crawler.crawl_articles(data_export)
    print 'Exporting Articles to /crawler_export.json'
    json.dump(crawler_export, open("crawler_export.json", 'w'))
else:
    print ""
