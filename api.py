import requests
import urllib

from requests.api import get


def get_api(url):
    result = requests.get(url)
    return result.json()


def main():
    keyword = "鬼滅"
    url = "https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706?format=json&keyword={}&applicationId=1019079537947262807".format(
        keyword)
    request_deta=get_api(url).items[0].item.itemName
    print(request_deta)


main()
