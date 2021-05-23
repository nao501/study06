import requests
import urllib

from requests.api import get
import pprint

def get_api(url):
    result = requests.get(url)
    return result.json()


def main():
    keyword = "鬼滅"
    url = "https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706?format=json&keyword={}&applicationId=1019079537947262807".format(
        keyword)
    request_deta=get_api(url)
    if request_deta == None:
        return False
    else:
        request_deta
    count=0
    while count<=3:
        print(request_deta['Items'][count]['Item']['itemName'],request_deta['Items'][count]['Item']['itemPrice'],"円\n")
        count=count+1


main()
