from urllib2 import urlopen as uReq
from bs4 import BeautifulSoup as soup
import html2text
import json


class news_crawler:
    def __init__(self):  # this method creates the class object.
        pass

    test = json.dumps({"articles": [{
        "url": "https://www.nytimes.com/2018/02/28/world/australia/school-tech-lumineer-academy-susan-wu.html",
        "source": "The New York Times",
        "title": "Why This Tech Executive Says Her Plan to Disrupt Education Is Different"
    },
        {
            "url": "https://www.bloomberg.com/news/articles/2018-03-15/urgent-pedestrian-bridge-collapses-at-university-injuries-unclear",
            "source": "Bloomberg",
            "title": "URGENT: Pedestrian Bridge Collapses At University; Injuries Unclear"
        }]})

    def crawl_articles(self, collectedData):

        # Convert string to json object
        articles = json.loads(collectedData)
        # Create "articles" dictionary
        data = {'articles': []}
        # Loop for each article in the collected data
        counter = 0
        status_file = open('crawler_status.txt', 'w')
        for x in articles['articles']:
            counter = counter + 1

            # set the url to read the article
            url = x['url']

            # Split the url into parts based on dots
            newsName = url.split('.')

            # Create lists to store the title and the article
            titleContainer = []
            articleContainer = []

            # Open a connection with the url
            try:
                uClient = uReq(url)


                # Load the HTML page of the targeted url in the page_html variable
                page_html = uClient.read()

                # Close the connection
                uClient.close()

                # Parse the html page in the soup to be able to read from it
                page_soup = soup(page_html, "html.parser")

                if (newsName[1] == 'washingtonpost'):
                    titleContainer = page_soup.findAll('title')
                    articleContainer = page_soup.findAll('article')

                elif (newsName[1] == 'nytimes'):
                    titleContainer = page_soup.findAll('h1', {'class': 'headline'})
                    articleContainer = page_soup.findAll('p', {'class': 'story-body-text story-content'})

                elif (newsName[0][7:] == 'abcnews'):  # Needs to fix the article
                    titleContainer = page_soup.article.div.header.h1
                    articleContainer = page_soup.findAll('div', {'class': 'article-body'})

                elif (newsName[1] == 'aljazeera'):
                    titleContainer = page_soup.findAll('h1', {'class', 'megaheadline post-title'})
                    articleContainer = page_soup.findAll('div', {'class': 'article-p-wrapper'})

                elif (newsName[1] == 'apnews'):
                    titleContainer = page_soup.article.div.h3
                    articleContainer = page_soup.findAll('div', {'class': 'articleBody'})

                elif (newsName[1] == 'bbc'):
                    titleContainer = page_soup.findAll('h1', {'class': 'story-body__h1'})
                    articleContainer = page_soup.findAll('div', {'class': 'story-body__inner'})

                elif (newsName[1] == 'bloomberg'):
                    titleContainer = page_soup.findAll('h1', {'class': 'lede-text-only__hed'})
                    articleContainer = page_soup.findAll('div', {'class': 'body-copy fence-body'})

                elif (newsName[1] == 'buzzfeed'):  # poor HTML pattern
                    titleContainer = page_soup.hgroup.h1
                    articleContainer = page_soup.findAll('div', {'id': 'mod-subbuzz-text-1'})

                elif (newsName[1] == 'cbsnews'):
                    titleContainer = page_soup.findAll('h1', {'class': 'title'})
                    articleContainer = page_soup.findAll('div', {'class': 'entry'})

                elif (newsName[1] == 'cnn'):
                    titleContainer = page_soup.findAll('h1', {'class': 'pg-headline'})
                    articleContainer = page_soup.findAll('div', {'class': 'zn-body__read-all'})

                elif (newsName[1] == 'cnbc'):  # Rejects the connection
                    titleContainer = page_soup.findAll('h1', {'class': 'title'})
                    articleContainer = page_soup.findAll('div', {'class': 'content'})

                elif (newsName[1] == 'nbcnews'):  # Rejects the connection
                    titleContainer = page_soup.findAll('div', {'class': 'article-hed'})
                    articleContainer = page_soup.findAll('div', {'class': 'article-body'})

                elif (newsName[1] == 'politico'):
                    titleContainer = page_soup.findAll('span', {'itemprop': 'headline'})
                    articleContainer = page_soup.findAll('p')

                elif (newsName[1] == 'economist'):
                    titleContainer = page_soup.findAll('span', {'class': 'flytitle-and-title__title'})
                    titleContainer = titleContainer[0]
                    articleContainer = page_soup.findAll('div', {'class': 'blog-post__text'})

                elif (newsName[1] == 'huffingtonpost'):
                    titleContainer = page_soup.findAll('h1', {'class': 'headline__title'})
                    articleContainer = page_soup.findAll('div',
                                                         {'class': 'entry__text js-entry-text bn-entry-text yr-entry-text'})

                elif (newsName[1] == 'wsj'):  # Needs payment
                    titleContainer = page_soup.findAll('h1', {'itemprop': 'headline'})
                    articleContainer = page_soup.findAll('div', {'div': 'wsj-article-body'})

                elif (newsName[1] == 'usatoday'):  # Rejects connection
                    titleContainer = page_soup.findAll('h1', {'class': 'asset-headline speakable-headline'})
                    articleContainer = page_soup.findAll('div', {'class': 'asset-double-wide double-wide p402_premium'})

                elif (newsName[0][7:] == 'time'):
                    titleContainer = page_soup.findAll('h1',
                                                       {'class': 'headline heading-content margin-8-top margin-16-bottom'})
                    articleContainer = page_soup.findAll('div', {'class': 'padded'})

                # Convert html to text and store it in the title variable
                title = str(html2text.html2text(str(titleContainer)))
                title = self.clean_text(title)

                # convert html to text and store the text in the article variable
                article = str(html2text.html2text(str(articleContainer)))
                article = self.clean_text(article)

                # New json object to strore the entire article and add it to "article_details"
                json_article = {'article': article}

                # Create a json object with the current article details
                article_details = {'source': x['source'], 'title': x['title'], 'article': json_article['article'],
                                   'url': x['url']}

                data['articles'].append(article_details)
                print counter, 'of', len(articles['articles']), 'SUCCESS'
                print >> status_file, counter, 'of', len(articles['articles']), 'SUCCESS\n'
            except Exception as a:
                print counter, 'of', len(articles['articles']), '***FAILURE***','\nReason Code:', a , '\n', str(
                    x['url']) , '\n'
                print >> status_file, counter, 'of', len(articles['articles']), '***FAILURE***', '\nReason Code:', a, '\n', str(
                    x['url']), '\n'

        json_data = json.dumps(data, sort_keys=True, indent=3)
        status_file.close()
        # return a json string
        return json_data

    def clean_text(self, str):
        str = str.replace('\n', ' ')
        str = str.replace('\\n', '')
        str = str.replace('\\u201', ' ')
        str = str.replace('#', '')
        str = str.replace(' d ', ' ')
        str = str.replace('  ', ' ')
        return str


