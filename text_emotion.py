from empath import Empath
emo = Empath()
import pandas as pd
import re
import matplotlib.pyplot as pyplot

   
def cleanTweet(tweet):
        
     return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) | (\w +:\ / \ / \S +)", " ", tweet).split())


data=["I felt tired out for no good reason some of the times"]
for i in range(len(data)):
    data[i]=data[i].replace("\n"," ").strip().lower().replace(".","")
df={}    
for i in range(len(data)):
    data[i]=cleanTweet(data[i])
    d=emo.analyze(data[i],)
    
    for j in d:
        if(d[j]!=0.0):
            if(j not in df):
                df[j]=d[j]
            else:
                df[j]+=d[j]



print(df)

dff={}
for i in df:
    if(i in ['aggression','sadness','fear', 'nervousness', 'negative_emotions','fun', 'celebration']):
        dff[i]=df[i]
pyplot.pie([float(dff[v]) for v in dff], labels=[str(k) for k in dff],
          autopct=None)
pyplot.show()          




