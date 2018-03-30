from api_gen import api_gen
from news_crawler import news_crawler
from data_collection import data_collection
import json

print ""
print "***Welcome to Edu Bias News Crawler***"
print ""

# API Key Selection
apiKeys = api_gen()
apiKeys.printAllKeys()
print ""
currentAPIKey = apiKeys.getKey(str(raw_input("Select an API Key: ")))


# Data Collection Module
inputPrompt = "\nRun Data Collection Module (y/n):"
if(str(raw_input(inputPrompt)) == 'y'):
    data = data_collection()
    article_batches = int(raw_input("\tNumber of Article Batches: "))
    data_export = data.collect_articles(article_batches, currentAPIKey)
    json.dump(data_export, open("data_collection.txt", 'w'))
else:
    print "Loading Cached Datafile (data_collection.txt)"
    data_export = json.load(open("data_collection.txt"))

# Crawler Module
inputPrompt = "\nRun Crawler Module (y/n):"
if(str(raw_input(inputPrompt)) == 'y'):
    crawler = news_crawler()
    crawler_export = crawler.crawl_articles(data_export)
    json.dump(crawler_export, open("crawler_export.txt", 'w'))
else:
    print ""
