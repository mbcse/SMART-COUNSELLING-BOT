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
    
    print(d)

    dff={}
    for i in d:
        if(i in ['aggression','sadness','fear', 'nervousness', 'negative_emotions','fun', 'celebration']):
            dff[i]=d[i]
    print(dff)        
    #pyplot.pie([float(dff[v]) for v in dff], labels=[str(k) for k in dff],
          #autopct=None)
    #pyplot.show()          


def sentiment(t,neutral,wpositive,positive,spositive,wnegative,negative,snegative,NoOfTerms,polarity):
        
        
        analysis = TextBlob(t)
            
        polarity = analysis.sentiment.polarity 

        polarity += analysis.sentiment.polarity

        if (analysis.sentiment.polarity == 0):  
                neutral+= 1
        elif (analysis.sentiment.polarity > 0 and analysis.sentiment.polarity <= 0.3):
                wpositive+= 1
        elif (analysis.sentiment.polarity > 0.3 and analysis.sentiment.polarity <= 0.6):
                positive+= 1
        elif (analysis.sentiment.polarity > 0.6 and analysis.sentiment.polarity <= 1):
                spositive+= 1
        elif (analysis.sentiment.polarity > -0.3 and analysis.sentiment.polarity <= 0):
                wnegative+= 1
        elif (analysis.sentiment.polarity > -0.6 and analysis.sentiment.polarity <= -0.3):
                negative+= 1
        elif (analysis.sentiment.polarity > -1 and analysis.sentiment.polarity <= -0.6):
                snegative+= 1


def percentage( part, whole):
        temp = 100 * float(part) / float(whole)
        return format(temp, '.2f')        

 

def report(neutral,wpositive,positive,spositive,wnegative,negative,snegative,NoOfTerms,polarity):

        
        positive =percentage(positive, NoOfTerms)
        wpositive =percentage(wpositive, NoOfTerms)
        spositive =percentage(spositive, NoOfTerms)
        negative = percentage(negative, NoOfTerms)
        wnegative = percentage(wnegative, NoOfTerms)
        snegative = percentage(snegative, NoOfTerms)
        neutral = percentage(neutral, NoOfTerms)

       
        polarity = polarity / NoOfTerms    

        print()
        print("General Report: ")

       
        if (polarity == 0):
            print("Neutral")
        elif (polarity > 0 and polarity <= 0.3):
            print("Weakly Positive")
        elif (polarity > 0.3 and polarity <= 0.6):
            print("Positive")
        elif (polarity > 0.6 and polarity <= 1):
            print("Strongly Positive")
        elif (polarity > -0.3 and polarity <= 0):
            print("Weakly Negative")
        elif (polarity > -0.6 and polarity <= -0.3):
            print("Negative")
        elif (polarity > -1 and polarity <= -0.6):
            print("Strongly Negative")

        print()
        print("Detailed Report: ")
        print(str(positive) + "% people thought it was positive")
        print(str(wpositive) + "% people thought it was weakly positive")
        print(str(spositive) + "% people thought it was strongly positive")
        print(str(negative) + "% people thought it was negative")
        print(str(wnegative) + "% people thought it was weakly negative")
        print(str(snegative) + "% people thought it was strongly negative")
        print(str(neutral) + "% people thought it was neutral")
     
  








