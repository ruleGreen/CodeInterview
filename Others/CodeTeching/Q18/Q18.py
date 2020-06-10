# Carrey Wong
# 2020 05 27
import csv
import requests
from lxml import etree

headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
           'Accept-Encoding': 'gzip, deflate, br',
           'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7',
           'Cache-Control': 'max-age=0',
           'Connection': 'keep-alive',
           'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}

response = requests.get("https://www.baidu.com/", headers=headers)
with open('test.txt', 'w', encoding='utf-8') as f:
    f.write(response.text)

print(response.text)
html = etree.HTML(response.text)

# ul class="s-news-rank-content"  => li class="news-meta-item clearfix" data-index="0" => a span class="title-content-title"
ul = html.xpath('//ul[@class="s-hotsearch-content"]/li')
result = []
for li in ul:
    title = li.xpath('.//span[@class="title-content-title"]')[0].text
    href = li.xpath('.//a[@class="title-content c-link c-font-medium c-line-clamp1"]')[0].get('href')
    result.append([title, href])
    print(title, href)

# save it to csv
with open("results.csv", 'w') as f:
    writer = csv.writer(f)
    writer.writerow(["title", "href"])
    writer.writerows(result)



