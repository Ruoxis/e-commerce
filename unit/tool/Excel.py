# -*- coding:utf-8 -*-
# !/usr/bin/env python
"""
@Project ：e-commerce
@File ：Excel.py
@Time ：2023/6/26 15:37
@Author ：11031840
@Motto: 理解しあうのはとても大事なことです。理解とは误解の総体に过ぎないと言う人もいますし
"""
from pathlib import Path
import requests
import pandas as pd
import os
from Data import *


class Excle:
    def __init__(self, out_path):
        if os.path.isdir(out_path):
            self.out_path = out_path
        elif os.path.isfile(out_path):
            self.out_path_name = out_path
        else:
            self.out_path_name = '临时.xlsx'

    def data_analyse_to_excel(self, data):
        """
        数据预处理，[DataFrame data1,DataFrame data2],
        {sheet_name1: DataFrame data1,sheet_name2: DataFrame data2}
        :param data:
        :return:
        """
        writer = pd.ExcelWriter(self.out_path_name)
        print(type(data))
        if type(data) is list or type(data) is tuple:
            # 无明确sheet名的时候输出excel
            for index, i in enumerate(data):
                i.to_excel(writer, sheet_name='Sheet{}'.format(index))
        elif type(data) is dict:
            # 有确定sheet名的时候输出excel
            for key, value in data.items():
                value.to_excel(writer, sheet_name=key)
        writer.save()
        return writer.path



