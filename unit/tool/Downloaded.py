# -*- coding:utf-8 -*-
# !/usr/bin/env python
"""
@Project ：e-commerce
@File ：Downloaded.py
@Time ：2023/6/27 10:49
@Author ：11031840
@Motto: 理解しあうのはとても大事なことです。理解とは误解の総体に过ぎないと言う人もいますし
"""


class Downloaded:
    def __init__(self, path):
        self.path = path

    def downloaded_resource(self):
        sheet = pd.read_excel('../../Data/临时.xlsx', sheet_name=0)
        for index, row in sheet.iterrows():
            print(row.img_url)
            response = requests.get(row.img_url, stream=True)
            with open('../../Data/img/' + row.img_name + '.' + row.img_url.split('.')[-1], 'wb') as f:
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)


Downloaded().downloaded_resource()
