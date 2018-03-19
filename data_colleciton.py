import json
import requests

def collect_articles():
    # Returns json data for articles matching bias keywords
    # Json data includes: source, title, and url
    
    print "Collecting Articles from News API.."
    # result is a list of json (dictionary) objects obtained through the News API requests
    result = []
    # counter is used to count the number of articles we are using for analysis
    # incremented everytime a article is found in the responses
    counter = 0

    # News Sources: ABC News, Al Jazeera English, Associated Press, BBC News, Bloomberg, Buzzfeed, CBS News, CNN, 
    # MSNBC, NBC News, Politico, The Economist, The Huffington Post, The New York Times, 
    # The Wall Street Journal, Time,The Washington Post, USA Today.

    # page_number represents a page of results, we change the page in the request to get other articles
    page_number = 1
    # outputed json file that will be added to as articles are parsed, each article will be a dictionary object containing source, title, and url
    data = {'articles' : []}
    while page_number <= 100:
        print "Page: " + str(page_number)
        # 100 Requests - Limited to 1000 Requests Per Day.
        # Returns a maximum of 100 articles per request using the pageSize=100 parameter. 
        # Have to increment page number in order to gather all results, limited buffer size of 10,000
        # Max amount of articles we are able to retrieve is 10,000 unless we incremently decrease pageSize
        # Change API key if needed in both URLs defined below
        if page_number == 100:
            url = 'https://newsapi.org/v2/everything?sources=abc-news,al-jazeera-english,associated-press,bbc-news,bloomberg,buzzfeed,cbs-news,cnn,msnbc,nbc-news,the-politico,the-economist,the-huffington-post,the-new-york-times,the-wall-street-journal,the-washtington-post,usa-today&pageSize=100&page=' + str(page_number) + '&q=bias%20OR%20education%20OR%20learning%20OR%20college%20OR%20university%20OR%20%22technology%20education%22%20OR%20%22career%20choice%22%20OR%20gap%20OR%20%22entrance%20exam%22%20OR%20%22standardized%20testing%22&apiKey=f13ccf0bfb6443538be289855787b9f4'
        else:
            url = 'https://newsapi.org/v2/everything?sources=abc-news,al-jazeera-english,associated-press,bbc-news,bloomberg,buzzfeed,cbs-news,cnn,msnbc,nbc-news,the-politico,the-economist,the-huffington-post,the-new-york-times,the-wall-street-journal,the-washtington-post,usa-today&pageSize=100&page=' + str(page_number) + '&q=bias%20OR%20education%20OR%20learning%20OR%20college%20OR%20university%20OR%20%22technology%20education%22%20OR%20%22career%20choice%22%20OR%20gap%20OR%20%22entrance%20exam%22%20OR%20%22standardized%20testing%22&apiKey=f13ccf0bfb6443538be289855787b9f4'
        response = json.loads(response.text)
        # Add result of request to result list
        result.append(response)
        # Looping through each article to make sure we have access to the article information and to provide a 
        # visual when running the script.
        try:
            for article in response['articles']:
                counter = counter + 1
                # Prints name of source and the titel of the article
                print article['source']['name'], article['title']
                # Add article to ouput
                article = {'source': article['source']['name'], 'title': article['title'], 'url': article['url']}
                data['articles'].append(article)
        except KeyError:
            print "Maximum amount of daily requests reached."
        page_number = page_number + 1
    json_data = json.dumps(data)
    print "Finished Collecting Articles from News API."
    return json_data

collect_articles()




