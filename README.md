# news_sent
The purpose of this project is to provided sentiment analysis over news collected from Google. 

### download_google_news.py
Downloads latest news for the past 2 days. Displays a tiny report of the collected news data.
```
------------------------------
REPORT:
 - [ 235 ] news found
 - [ 117 ] published today
 - [ 118 ] published yesterday
------------------------------
```

### classify_news.py
Runs news sentiment classification model from `NewsSentiment` pip package and generates a detailed report of the news. It splits the report into 2 sections. The first section displays short sentiment analytics, and the second section lists all news grouped together. 
```
------------------------------
REPORT: 2024-01-24
 - [  50 | 0.50% ] neutral
 - [  31 | 0.31% ] negative
 - [  19 | 0.19% ] positive
REPORT: 2024-01-23
 - [  69 | 0.51% ] neutral
 - [  17 | 0.13% ] positive
 - [  49 | 0.36% ] negative
REPORT: ALL
 - [ 119 | 0.51% ] neutral
 - [  80 | 0.34% ] negative
 - [  36 | 0.15% ] positive
------------------------------
NEWS DUMP: negative
                                                title                                            snippet           source  category        date
0   Coinbase Falls After JPMorgan Downgrades Stock...  The bitcoin ETF catalyst that pushed the ecosy...         CoinDesk  negative  2024-01-23
1   Solana, Avalanche Tokens Slide as Bitcoin Trad...  Over half of the profits accumulated by short-...         CoinDesk  negative  2024-01-23
..                                                ...                                                ...              ...       ...         ...
78  Bitcoin set for supply shock as ETF buys surge...  The upcoming halving and a surge in demand fue...  Crypto Briefing  negative  2024-01-24
79  Bitcoin's Wall Street takeover frustrates cryp...  The price of bitcoin soared to its highest lev...  Financial Times  negative  2024-01-24

[80 rows x 5 columns]

NEWS DUMP: positive
                                                title                                            snippet                     source  category        date
0   Michael Howell Predicts Continued Surge in Glo...  Crossborder Capital's Michael Howell gives evi...           Bitcoin.com News  positive  2024-01-23
1   Bitcoin Adoption In Pakistan Continues To Rise...  Regulation is not a necessary prerequisite for...           Bitcoin Magazine  positive  2024-01-23
..                                                ...                                                ...                        ...       ...         ...
34  How To Buy Bitcoin: 5 Ways To Add The Popular ...  Bitcoin ATMs. Another option is to buy bitcoin...                   Bankrate  positive  2024-01-24
35  Futures: Microsoft Leads 5 Buys; Bitcoin Up On...  Dow Jones futures: Microsoft flashed a buy sig...  Investor's Business Daily  positive  2024-01-24

NEWS DUMP: neutral
                                                 title                                            snippet           source category        date
0       First Mover Americas: Bitcoin Slips Below $39K  The latest price moves in crypto markets in co...         CoinDesk  neutral  2024-01-23
1    Analysts Predict Bitcoin Price to Hit $60000 i...  Bitcoin's potential to reach $60,000 in 2024 i...       BeInCrypto  neutral  2024-01-23
..                                                 ...                                                ...              ...      ...         ...
116  BlackRock's and three other Bitcoin ETFs billi...  A new dashboard keeps track of the Bitcoin (BT...  Crypto Briefing  neutral  2024-01-24
118  These Are All the Bitcoin ETFs That Are Now Tr...  These Are All the Bitcoin ETFs That Are Now Tr...          Decrypt  neutral  2024-01-24

[119 rows x 5 columns]

------------------------------
```

## LICENSE
Project is licensed under the MIT license.

