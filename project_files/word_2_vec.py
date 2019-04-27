import pandas as pd
import gensim
import numpy as np
import xgboost as xgb
# import cufflinks as cf
import pprint
import json


from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

def WTV():
    main_data = pd.read_csv('../business_news.csv')
    main_data = main_data.head()
    main_data = main_data.sort_values(by = "Published")

    news_data = main_data[["Snippet", "Lead Paragraph", "Main Headline"]]
    news_data.apply(str)

    def list_prep(rows_to_list):
        news_list = rows_to_list.values.tolist()
        return(news_list)
        
    list_of_lists = list_prep(news_data)
    print(list_of_lists)
    def word_prep(list_lists):
        big_string = ""

        for title in list_lists:
        #     Splitting titles into list of words
            variable = title.split(" ")
        #     print(variable)

        #     v = words
        #     variable = list of words
            for v in variable:
                big_string = big_string + " " + v

        #     big_title_string = ' '.join((str(v) for v in variable))

        tokens = word_tokenize(big_string)

        # Remove non-alphabetic tokens, such as punctuation
        words = [word.lower() for word in tokens if word.isalpha()]

        # Filter out stopwords
        stop_words = set(stopwords.words('english'))

        words = [word for word in words if not word in stop_words]

        # Print first 10 words
        return(words)


        # print(tokens)
    word_list = []
    for list1 in list_of_lists:
        words = word_prep(list1)
        word_list.append(words)

    # Load word2vec model (trained on an enormous Google corpus)
    model = gensim.models.KeyedVectors.\
    load_word2vec_format('../resources/model/GoogleNews-vectors-negative300.bin', binary = True) 

    # Check dimension of word vectors
    model.vector_size
    
    def word_2_vec(words):
        vector_list = []
        words_filtered = []
        # Filter the list of vectors to include only those that Word2Vec has a vector for
        vector_list.extend([model[word] for word in words if word in model.vocab])
    #     return(vector_list)
        # Create a list of the words corresponding to these vectors
        words_filtered.extend([word for word in words if word in model.vocab])
    #     return(words_filtered)
        # Zip the words together with their vector representations
        word_vec_zip = zip(words_filtered, vector_list)
        
        # Cast to a dict so we can turn it into a dataframe
        word_vec_dict = dict(word_vec_zip)
        return(word_vec_dict)

    # dataframe_dict_list = []
    # for list in word_list:
    #     df = word_2_vec(list)
    #     dataframe_dict_list.append(df)

    # dataframe_list = []
    # for dataframe in range(len(dataframe_dict_list)):
    #     df = pd.DataFrame.from_dict(dataframe_dict_list[dataframe])
    #     dataframe_list.append(df)
    

    # def row_summation(dataframe_list):
    #     summation_list = []
    #     for dataframe in dataframe_list:
    #     #     print(dataframe)
    #         total_columns = len(dataframe.columns)
    #     #     print(total_columns)
    #         sums = dataframe.sum(axis = 1, skipna = True)
    #     #     print(sums)
    #         summation = sums/total_columns
    #         summation_list.append(summation)
    #     return summation_list

        
    # summation_series = row_summation(dataframe_list)

    return list_of_lists

