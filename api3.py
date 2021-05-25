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
    url = "https://app.rakuten.co.jp/services/api/Product/Search/20170426?"
    search_params={
        "format":"json",
        "keyword":keyword,
        "applicationId":1019079537947262807
        }
    request_deta=get_api(url,params = search_params)
    item_key = ['productName','salesMaxPrice','salesMinPrice']
    item_list = []
    ##pprint.pprint(request_deta['Products'][0]['Product']['productName'])
    for i in range(0, len(request_deta['Products'])):
        for key in item_key:
            item = request_deta['Products'][i]['Product'][key]
            item_list.append(item)
    print(item_list)
    
    

main()
