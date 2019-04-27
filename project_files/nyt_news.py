from config import api_key
import datetime
import requests
import pandas as pd

def getNews():
    '''
    '''
    snippet = []
    pubDate = []
    leadPara= []
    headline_main = []
    headline_print = []
    headline_seo = []

    for i in range(0,1):

        #url_target = "https://newsapi.org/v2/top-headlines?"

        today = str(datetime.datetime.today().date())
        today = today.replace('-', '')
        print(today)

        url_target = 'https://api.nytimes.com/svc/search/v2/'
        #query_url = f"{url_target}articlesearch.json?fq=news_desk:('Sports')&page=0&begin_date={today}&end_date={today}&api-key={api_key}"
        query_url = f"{url_target}articlesearch.json?fq=market&page={i}&begin_date={today}&end_date={today}&api-key={api_key}"
        print(query_url)

        news = requests.get(query_url).json()

        lenNews = len(news['response']['docs'])
        print(lenNews)


        for lnews in range(lenNews):
            try:
                pub_date = news['response']['docs'][lnews]['pub_date']
                snip = news['response']['docs'][lnews]['snippet']
                leadpara = news['response']['docs'][lnews]['lead_paragraph']
                hmain = news['response']['docs'][lnews]['headline']['main']
                hprint = news['response']['docs'][lnews]['headline']['print_headline']
                hseo = news['response']['docs'][lnews]['headline']['seo']

                snippet.append(snip)
                pubDate.append(pub_date)
                leadPara.append(leadpara)
                headline_main.append(hmain)
                headline_print.append(hprint)
                headline_seo.append(hseo)

                print(f'Published Date: {pub_date}')
                print(f"Snippet: {snip}")
                print(f"Lead Paragraph: {leadpara}")
                print(f"Main Headline: {hmain}")
                print(f"Print Headline: {hprint}")
                print(f"Seo Headline: {hseo}")
                print("-------------------------------------------------------------------------------------------------")
            except Exception:
                print(f"Error on Snippet: {snip}")

        

        #https://api.nytimes.com/svc/search/v2/articlesearch.json?fq=market&begin_date=20120101&end_date=20120101&api-key=BoeyEHviGTCHP36FZIuyYDvMXS79QG5j
    print(len(snippet))
    nyt_news_df = pd.DataFrame({
    "Published" : pubDate,
    "Snippet"  : snippet,
    "Lead Paragraph" : leadPara,
    "Main Headline"  : headline_main,
    "Print Headline" : headline_print,
    "Seo Headline"   : headline_seo
    })

    nyt_news_df.to_csv('resources/news/market_news.csv', index=False)