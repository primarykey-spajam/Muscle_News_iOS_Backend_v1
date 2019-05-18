import requests as web
import bs4
import csv

from ipdb import set_trace

def get_text(list_keywd):

    resp = web.get('https://news.infoseek.co.jp/search?type=article&num=10&q=' + '　'.join(list_keywd))

    resp.raise_for_status()

    # 取得したHTMLをパースする
    soup = bs4.BeautifulSoup(resp.text, "html.parser")
    # 検索結果のタイトルとリンクを取得
    link_elem01 = soup.select('.article-list > li > a')

    # 1番上の記事URLを取得
    #_url_text = link_elem01[0].get('href')
    #url_text = "https://news.infoseek.co.jp"+_url_text
    url_text = 'https://news.infoseek.co.jp/article/sankein_wst1905180016/'

    # 記事の情報を取得
    resp = web.get(url_text)
    resp.raise_for_status()

    # 取得したHTMLをパースする
    soup = bs4.BeautifulSoup(resp.text, "html.parser")

    # テキストを取得
    all_p_soup = soup.find_all("p")
    text = ""
    for i in range(len(all_p_soup)-55):
        text += all_p_soup[i].text
    text = text.replace('\n','')


    return text
