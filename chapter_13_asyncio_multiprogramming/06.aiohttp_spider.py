# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Time    : 2021/5/17 上午9:19
# @Author  : QA-wyy
# @File    : 06.aiohttp_spider.py
# @Description: 
-------------------------------------------------
"""
# async 爬虫  去重  入库
import asyncio
import re
import aiohttp
from pyquery import PyQuery
from lxml import etree

pool = ''
# sem = asyncio.Semaphore(4)  用来控制并发数，不指定会全速运行
stop = False
headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) \
	Chrome/61.0.3163.100 Safari/537.36'
}
MAX_PAGE = 10
TABLE_NAME = 'data'  # 数据表名
city = 'zh'  # 城市简写
url = 'https://{}.lianjia.com/ershoufang/pg{}/'  # url地址拼接
urls = []  # 所有页的url列表
links_detail = set()  # 爬取中的详情页链接的集合
crawled_links_detail = set()  # 爬取完成的链接集合，方便去重


async def fetch(url, session):
	"""
	aiohttp获取网页源码
	"""
	# async with sem:
	try:
		async with session.get(url, headers=headers, verify_ssl=False) as resp:
			if resp.status in [200, 201]:
				data = await resp.text()
				return data
	except Exception as e:
		print(e)


def extract_links(source):
	"""
	提取出详情页的链接
	"""
	pq = PyQuery(source)
	for link in pq.items("a"):
		_url = link.attr("href")
		if _url and re.match('https://.*?/\d+.html', _url) and _url.find('{}.lianjia.com'.format(city)):
			links_detail.add(_url)

	print(links_detail)


def extract_elements(source):
	"""
	提取出详情页里面的详情内容
	"""
	try:
		dom = etree.HTML(source)
		title = dom.xpath('//title/text()')[0]
		print(title)


	except Exception as e:
		print('解析详情页出错！')
		pass

async def handle_elements(link, session):
	"""
	获取详情页的内容并解析
	"""
	print('开始获取: {}'.format(link))
	source = await fetch(link, session)
	# 添加到已爬取的集合中
	crawled_links_detail.add(link)
	extract_elements(source)


async def consumer():
	"""
	消耗未爬取的链接
	"""
	async with aiohttp.ClientSession() as session:
		while not stop:
			if len(urls) != 0:
				_url = urls.pop()
				source = await fetch(_url, session)
				print(_url)
				extract_links(source)

			if len(links_detail) == 0:
				print('目前没有待爬取的链接')
				await asyncio.sleep(2)
				continue

			link = links_detail.pop()
			if link not in crawled_links_detail:
				asyncio.ensure_future(handle_elements(link, session))


async def main(loop):
	for i in range(1, MAX_PAGE):
		urls.append(url.format(city, str(i)))
	print('爬取总页数：{} 任务开始...'.format(str(MAX_PAGE)))
	asyncio.ensure_future(consumer())


if __name__ == '__main__':
	loop = asyncio.get_event_loop()
	asyncio.ensure_future(main(loop))
	loop.run_forever()
