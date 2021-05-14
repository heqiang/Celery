import requests
from lxml import  etree
headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'sec-ch-ua': '^\\^',
    'sec-ch-ua-mobile': '?0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Referer': 'https://movie.douban.com/top250',
    'Accept-Language': 'zh-CN,zh;q=0.9',
}

params = (
    ('start', '25'),
    ('filter', ''),
)


def douban():
    response = requests.get('https://movie.douban.com/top250', headers=headers, params=params)
    html = etree.HTML(response.text)
    for x in html.xpath('//ol[@class="grid_view"]/li'):
        title = x.xpath(".//div[@class='hd']//span[1]/text()")[0]
        with open("douban.txt","a",encoding="utf-8") as f:
                f.write(title+"\n")