# module classify_news

import os
import pandas as pd
from datetime import datetime
from collections import Counter
from NewsSentiment import TargetSentimentClassifier

# load data
data_folder = './cache/webscrapping'
df = pd.read_csv(os.path.join(data_folder, f'{datetime.now().strftime("%Y-%m-%d")}.csv'))

# preprocess
data = list(df.title.values)
data = list(map(lambda x: ('', x, ''), data))

# model
tsc = TargetSentimentClassifier()

# infer
sentiments = tsc.infer(targets=data)

# extract output labels names
sentiments = list(map(lambda x: x[0]['class_label'], sentiments))
counts = Counter(sentiments)

# append category to df
df['Category'] = sentiments

# report
print('------------------------------')
print('REPORT: positive-neutral-negative')
print(f' - [ {counts["positive"]:3d} | {counts["positive"]/len(sentiments):.2f}% ] positive')
print(f' - [ {counts["neutral"]:3d} | {counts["neutral"]/len(sentiments):.2f}% ] neutral')
print(f' - [ {counts["negative"]:3d} | {counts["negative"]/len(sentiments):.2f}% ] negative')
print('------------------------------')
print('NEWS DUMP: negative')
print(df.loc[df['Category'] == 'negative'])
print('NEWS DUMP: positive')
print(df.loc[df['Category'] == 'positive'])
print('NEWS DUMP: neutral')
print(df.loc[df['Category'] == 'neutral'])
print('------------------------------')

