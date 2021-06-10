import requests
import pandas as pd
import time


def read_tickers():
    return pd.read_csv('data/companies_nyse_tech.csv')


def get_time_series_daily(tickers, key):
    for symbol in tickers:
        print(symbol) # to keep track of where we are
        response = requests.get(f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={key}&outputsize=full')
        if response.status_code == 200:
            response_dict = response.json()
            df = pd.DataFrame.from_dict(response_dict['Time Series (Daily)'])
            df.to_csv(f'data/time_series_daily_curated/{symbol}.csv')
            time.sleep(12) # max 5 requests per minute


def get_company_overview(tickers, key):
    for symbol in tickers:
        pass


if __name__ == '__main__':
    api_key = input()
    get_time_series_daily(['NFLX','TSLA','IGV','SPY','QQQ','IWM','DIA','XLE','XLP'], api_key)
