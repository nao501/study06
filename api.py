import requests
import urllib

from requests.api import get

GET https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706

def get_api(url):
    result = requests.get(url)
    return result.json()


def main():
    keyword = "鬼滅"
    url = "https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706?format=json&keyword={}&applicationId=1019079537947262807".format(
        keyword)
    request_deta=get_api(url)["items": [{"item": {"itemName": "a"}}]]
    print(request_deta)


main()
