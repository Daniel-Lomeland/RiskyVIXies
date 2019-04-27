#!pip install google.cloud
# export GOOGLE_APPLICATION_CREDENTIALS="/Users/daniellomeland/1_projects/Final_Project/Class_Project-key.json"

# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
import pandas as pd

# client = Client.from_service_account_json('/Users/daniellomeland/1_projects/Final_Project/Class_Project-key.json')



def get_sentiment():
    df = pd.read_csv("resources/news/market_news.csv")

    Snippet = df["Snippet"].tolist()
    Lead_Paragraph = df["Lead Paragraph"].tolist()
    Main_Headline = df["Main Headline"].tolist()
    Print_Headline = df["Print Headline"].tolist()

    Snippet_s= []
    Lead_Paragraph_s= []
    Main_Headline_s = []
    Snippet_m = []
    Lead_Paragraph_m= []
    Main_Headline_m = []


    for item in Snippet:
        try: 
            text = item    
            client = language.LanguageServiceClient()
            document = types.Document(
                    content=text,
                    type=enums.Document.Type.PLAIN_TEXT)
            sentiment = client.analyze_sentiment(document).document_sentiment
            print('Score: {}'.format(sentiment.score))
            Snippet_s.append(sentiment.score)
            Snippet_m.append(sentiment.magnitude)
        except TypeError:
            print("bad text")


    for item in Lead_Paragraph:
        text = item    
        client = language.LanguageServiceClient()
        document = types.Document(
                content=text,
                type=enums.Document.Type.PLAIN_TEXT)
        sentiment = client.analyze_sentiment(document).document_sentiment
        print('Score: {}'.format(sentiment.score))
        Lead_Paragraph_s.append(sentiment.score)
        Lead_Paragraph_m.append(sentiment.magnitude)


    for item in Main_Headline:
        text = item    
        client = language.LanguageServiceClient()
        document = types.Document(
                content=text,
                type=enums.Document.Type.PLAIN_TEXT)
        sentiment = client.analyze_sentiment(document).document_sentiment
        print('Score: {}'.format(sentiment.score))
        Main_Headline_s.append(sentiment.score)
        Main_Headline_m.append(sentiment.magnitude)

    # for item in Print_Headline:
    #     text = item    
    #     client = language.LanguageServiceClient()
    #     document = types.Document(
    #             content=text,
    #             type=enums.Document.Type.PLAIN_TEXT)
    #     sentiment = client.analyze_sentiment(document).document_sentiment
    #     print('Score: {}'.format(sentiment.score))
    #     Print_Headline_s.append(sentiment.score)



    df1 = pd.DataFrame({'Snippet_s':Snippet_s})
    df2 = pd.DataFrame({'Lead_Paragraph_s':Lead_Paragraph_s})
    df3 = pd.DataFrame({'Main_Headline_s':Main_Headline_s})
    # df4 = pd.DataFrame({'Print_Headline_s':Print_Headline_s})

    result = pd.concat([df,df1,df2,df3], axis=1, sort=False)


    df = result
    df2= df[['Snippet_s','Lead_Paragraph_s','Main_Headline_s']].apply(pd.DataFrame.describe, axis=1)
    df2= df2[['mean', 'std', 'min', '25%', '50%', '75%', 'max']]
    df["Published"] = pd.to_datetime(df.Published).dt.date
    df3= df["Published"]
    df5= df[['Snippet_s','Lead_Paragraph_s','Main_Headline_s']]
    df4 = pd.concat([df3,df5,df2], axis=1)
    df6= df4.groupby(df4['Published'],as_index=False).mean()
    df7= df6[['Snippet_s', 'Lead_Paragraph_s', 'Main_Headline_s', 'mean', 'std',
        'min', '25%', '50%', '75%', 'max']]
        
    # to DF
    print(df7)
    return df7.values.tolist()

