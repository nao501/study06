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
    request_deta=get_api(url)
    if request_deta == None:
        return False
    else:
        print(request_deta["items"][0]["item"]["itemName"])
    


main()
