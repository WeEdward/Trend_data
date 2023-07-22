import json
import pandas as pd
from pytrends.request import TrendReq
import matplotlib.pyplot as plt
import plotly.express as px

## Connect to Google

# 讀取配置文件
with open('config.json') as f:
    config = json.load(f)

# 從配置文件中獲取帳號和密碼
google_username = config['google_username']
google_password = config['google_password']

# 建立pytrends物件
# , retries=2, backoff_factor=0.1, requests_args={'verify':False}
pytrends = TrendReq(hl='zh-TW')


## Request a Report
# keywords= input() // 後期優化用
keywords = ['比特幣']

# data= pytrends.request_report(keywords, hl='en-US', cat=None, geo=None, date=None)
pytrends.build_payload(keywords, cat=None, geo='TW', timeframe= 'all')

# 獲取資料
data = pytrends.interest_over_time()
data = data.reset_index() 
# print(type(data['date']))
# print(type(data))


fig = px.line(data, x="date", y= keywords, title= 'Search Interest Over Time')
fig.show()


