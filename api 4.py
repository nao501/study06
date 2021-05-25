import requests
import urllib
import pandas as pd
import numpy  as np
from requests.api import get
import pprint

def get_api(url,params):
    result = requests.get(url,params)
    return result.json()


def main():
    keyword = "鬼滅"
    url = "https://app.rakuten.co.jp/services/api/IchibaItem/Ranking/20170628?"
          
    search_params={
        "format":"json",
        "keyword":keyword,
        "applicationId":1019079537947262807,
        "sort":"-itemPrice",
        'period':"realtime",
        "minPice":200
        }
    request_deta=get_api(url,params = search_params)
    item_key = ['itemName','rank', 'itemPrice', 'itemCaption', 'itemUrl']
    item_list = []
    for i in range(0, len(request_deta['Items'])):
        tmp_item = {}
        item = request_deta['Items'][i]['Item']
        for key, value in item.items():
            if key in item_key:
                tmp_item[key] = value
        item_list.append(tmp_item.copy())
    items_df = pd.DataFrame(item_list)

# 列の順番を入れ替える
    items_df = items_df.reindex(columns=['itemName','rank', 'itemPrice', 'itemCaption', 'itemUrl'])

# 列名と行番号を変更する:列名は日本語に、行番号は1からの連番にする
    items_df.columns = ['商品名', '順位','商品価格', '商品説明文', '店舗URL']
    items_df.index = np.arange(1, 31)
    items_df.to_csv('rakuten_api_ranking.csv',encoding='utf_8_sig')
    print("完了")

main()
