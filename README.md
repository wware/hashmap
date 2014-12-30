Algorithmic trading with Python
=

Use PyAlgoTrade to scrape data from Yahoo finance.

* http://gbeced.github.io/pyalgotrade/
* http://gbeced.github.io/pyalgotrade/docs/v0.16/html/tutorial.html

```bash
python -c "from pyalgotrade.tools import yahoofinance; yahoofinance.download_daily_bars('orcl', 2000, 'orcl-2000.csv')"
```

Use the mutual fund screener, choosing >=30% for 1-year and 3-year returns, and manager tenure of at least 3 years.

http://screener.finance.yahoo.com/a?cc=&nm=&proy=&mgrt=3%2F&rtmin=&rtmax=&retrmin=&retrmax=&risrmin=&risrmax=&trytd=&troy=180%2F&trty=180%2F&trfy=&mii=&mfl=&er=&namin=&namax=&tomin=&tomax=&mmcmin=&mmcmax=&vw=1&db=funds

Run Bollinger bands on the data to identify good opportunities to buy and sell.

http://gbeced.github.io/pyalgotrade/docs/v0.16/html/sample_bbands.html

Maybe study up on computational investing.

* http://wiki.quantsoftware.org/index.php?title=Computational_Investing_I
* https://www.coursera.org/course/compinvesting1
