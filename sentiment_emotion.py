from empath import Empath
emo = Empath()
import re
import matplotlib.pyplot as pyplot
import sys
from textblob import TextBlob
import matplotlib.pyplot as plt



def  emotion(t):
    data=t
    data=data.replace("\n"," ").strip().lower().replace(".","")
    def clean(text):
        
         return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) | (\w +:\ / \ / \S +)", " ", text).split())

    data=clean(data)
    d=emo.analyze(data)
    dff={}
    for i in d:
        if(i in ['aggression','sadness','fear', 'nervousness', 'negative_emotions','fun', 'celebration']):
            dff[i]=d[i]
    print(dff)        
    #pyplot.pie([float(dff[v]) for v in dff], labels=[str(k) for k in dff],autopct=None)
    #pyplot.show()          


dic_param={'polarity':0,'positive':0,'wpositive':0,'spositive':0,'negative':0,'wnegative':0,'snegative':0,'neutral':0}

def sentiment(t):
        analysis = TextBlob(t)
        dic_param['polarity'] += analysis.sentiment.polarity 

        if (analysis.sentiment.polarity == 0):  
                dic_param['neutral'] += 1
        elif (analysis.sentiment.polarity > 0 and analysis.sentiment.polarity <= 0.3):
                dic_param['wpositive'] += 1
        elif (analysis.sentiment.polarity > 0.3 and analysis.sentiment.polarity <= 0.6):
                dic_param['positive'] += 1
        elif (analysis.sentiment.polarity > 0.6 and analysis.sentiment.polarity <= 1):
                dic_param['spositive'] += 1
        elif (analysis.sentiment.polarity > -0.3 and analysis.sentiment.polarity <= 0):
                dic_param['wnegative'] += 1
        elif (analysis.sentiment.polarity > -0.6 and analysis.sentiment.polarity <= -0.3):
                dic_param['negative'] += 1
        elif (analysis.sentiment.polarity > -1 and analysis.sentiment.polarity <= -0.6):
                dic_param['snegative'] += 1
        print()
        

def final_report_dict():
    return dic_param

def report(dic_param):
        print("General Report: ")
        if (dic_param['polarity'] == 0):
            print("Neutral")
        elif (dic_param['polarity'] > 0 and dic_param['polarity'] <= 0.3):
            print("Weakly Positive")
        elif (dic_param['polarity'] > 0.3 and dic_param['polarity'] <= 0.6):
            print("Positive")
        elif (dic_param['polarity'] > 0.6 and dic_param['polarity'] <= 1):
            print("Strongly Positive")
        elif (dic_param['polarity'] > -0.3 and dic_param['polarity']<= 0):
            print("Weakly Negative")
        elif (dic_param['polarity'] > -0.6 and dic_param['polarity'] <= -0.3):
            print("Negative")
        elif (dic_param['polarity'] > -1 and dic_param['polarity'] <= -0.6):
            print("Strongly Negative")
        print()
        print("Detailed Report: ")
        print(str(dic_param['positive']) + "%  it was positive")
        print(str(dic_param['wpositive']) + "%  it was weakly positive")
        print(str(dic_param['spositive']) + "%  it was strongly positive")
        print(str(dic_param['negative']) + "%  it was negative")
        print(str(dic_param['wnegative']) + "% it was weakly negative")
        print(str(dic_param['snegative']) + "% it was strongly negative")
        print(str(dic_param['neutral']) + "% it was neutral")
     
  








