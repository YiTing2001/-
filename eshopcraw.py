"""
update by wengyiting
       in 2022.10.11
"""
from bs4 import BeautifulSoup
import requests
from pandas import DataFrame

#京东的最好爬取——哭了
target = "https://search.jd.com/Search?keyword=书包"


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edge/87.0.664.47'}
req = requests.get(url=target, headers=headers).content.decode('utf-8')
bf = BeautifulSoup(req, "html.parser")


goodslist = bf.find('div', id='J_goodsList')
goodsli = goodslist.find_all('li')

#创建商品属性列表
goodsnamelist = []
goodspricelist = []

#循环抓取数据
for li in goodsli:
    pricetag = li.find('div', class_='p-price')
    if (pricetag != None):
        price = pricetag.text
        res = str(price).replace(' ', '').replace('\t', '').replace('\n', '').replace('￥', '  ')
        goodspricelist.append(res)
    nameinfo = li.find('div', class_='p-name p-name-type-2')
    if (nameinfo != None):
        linkstring = nameinfo.find('a')
        name = linkstring.find('em')
        res = str(name.text).replace(' ', '').replace('\t', '').replace('\n', '')
        goodsnamelist.append(res)

#存储字典
dir_data = {"名称": goodsnamelist, "价格/会员价格": goodspricelist}
data = DataFrame(dir_data)
data.to_csv('bag.csv')

#输出数据
print(data)
