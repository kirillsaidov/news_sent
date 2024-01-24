# module classify_news
import os
import pandas as pd
from datetime import datetime, timedelta
from collections import Counter
from NewsSentiment import TargetSentimentClassifier


def count_sentiments(df: pd.DataFrame, date: str = datetime.now().strftime("%Y-%m-%d")):
    """Generate sentiments report

    Args:
        df (pd.DataFrame): dataframe with sentiments inferred
        date (str, optional): date. If None, all data is used. Defaults to datetime.now().strftime("%Y-%m-%d").

    Returns:
        dict: counts of sentiments
    """
    dfd = df if date is None else df.loc[df['date'] == date]
    sentiments = dfd['category'].values
    counts = Counter(sentiments)
        
    # calculate
    counts_ = {'date': date if date else 'ALL'}
    for key, value in counts.items():
        counts_.update({
            key: (value, value/len(sentiments)),
        })
    
    return counts_


if __name__ == '__main__':
    # load data
    data_folder = './cache/webscrapping'
    df = pd.read_csv(os.path.join(data_folder, f'{datetime.now().strftime("%Y-%m-%d")}.csv'))
    # df.date = pd.to_datetime(df.date) # converts automatically upon loading

    # preprocess
    data = list(df.title.values)
    data = list(map(lambda x: ('', x, ''), data))

    # model
    tsc = TargetSentimentClassifier()

    # infer and extract label names
    sentiments = tsc.infer(targets=data)
    sentiments = list(map(lambda x: x[0]['class_label'], sentiments))
    
    # append category to df
    df['category'] = sentiments

    # count sentiments
    counts = [
        count_sentiments(df, date=datetime.now().strftime("%Y-%m-%d")),
        count_sentiments(df, date=(datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")),
        count_sentiments(df, date=None),
    ]

    # report
    print('------------------------------')
    for counts_ in counts:
        print(f'REPORT: {counts_["date"]}')
        for key, value in counts_.items():
            if key == 'date': 
                continue
            print(f' - [ {value[0]:3d} | {value[1]:.2f}% ] {key}')                    
    print('------------------------------')
    for label in ['negative', 'positive', 'neutral']:
        print(f'NEWS DUMP: {label}')
        print(df.loc[df['category'] == label][['title', 'snippet', 'source', 'category', 'date']].sort_values(by='date', ascending=False).reset_index(drop=True), end='\n\n')
    print('------------------------------')

