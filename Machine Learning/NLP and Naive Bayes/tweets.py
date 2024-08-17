import pickle as pkl
import pandas as pd
from nltk.stem import PorterStemmer
import speech_recognition as sr 

def listen():

    r=  sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source,0,6)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio,language="en-in")
        print(f"you Said : {query}")

    except:
        return ""

    query = str(query)
    return query.lower()

herry_porter = PorterStemmer()

def set_tweet_content(text):
    text = text.split()
    temp = []
    for word in text:
        if '@' in word:
            continue
        else:
            for symbol in symbols:
                if symbol in word:
                    word = word.replace(symbol,'')
            temp.append(word)
    return temp

def stem_words(text):
    temp = []
    for word in text:
        temp.append(herry_porter.stem(word))
    return ' '.join(temp)

naive_model = pkl.load(open('Naive_model.pkl','rb'))
tfidf_model = pkl.load(open('Text_to_vector_model.pkl','rb'))

text = 'Today i am very happy because i completed my course.'

symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', 
           '[', ']', '{', '}', '|', '\\', ';', ':', '\'', '"', ',', '.', '/', '<', '>', '?', '`', '~']

text_in_list = set_tweet_content(text)

text = stem_words(text_in_list)

text = pd.Series(text)

text_vector = tfidf_model.transform(text).toarray()

prediction = naive_model.predict(text_vector)

print()
print('Your Emotion of Text is : ',prediction[0])