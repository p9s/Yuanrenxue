#!/usr/bin/env python
# 猿人学: 第一题
# points:
#     1. requests
#     2. 无限debug
from loguru import logger
import execjs
import requests
import json
import time

class Spider():
    def __init__(self, js_file=None):
        if js_file is None:
            js_file = 'chapter-1.js'
        self.js_file = js_file
        self.ctx = execjs.compile(open(self.js_file).read())

    def get_m(self):
        return self.ctx.call('get_m')


if __name__ == '__main__':
    headers = {'user-agent': 'yuanrenxue.project'}
    s = Spider()
    count = 0
    items = 0

    for page in range(1, 6):
        m = s.get_m()
        url = f'http://match.yuanrenxue.com/api/match/1?m={m}&page={page}'
        logger.info(f"process: {url}")

        data = requests.get(url, headers=headers)
        j = json.loads(data.text)
        logger.debug(j)

        for d in j['data']:
            count += d['value']
            items += 1

        time.sleep(1)

    logger.info(f"{count}/{items}={count/items}")
