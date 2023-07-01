# -*- coding:utf-8 -*-
# !/usr/bin/env python
"""
@Project ：e-commerce
@File ：__init__.py.py
@Time ：2023/6/27 14:34
@Author ：11031840
@Motto: 理解しあうのはとても大事なことです。理解とは误解の総体に过ぎないと言う人もいますし
"""

import os


class FilePathError(Exception):
    """
    文件路径检测
    """

    def __init__(self, file_path):
        self.file_path = file_path

    def __str__(self):
        return f"文件路径不存在：{self.file_path}"


class FileOpenError(FilePathError):
    """
    文件路径检测
    """

    def __str__(self):
        return f"文件打开异常：{self.file_path}"


def process_file(file_path):
    if not os.path.exists(file_path):
        raise FilePathError(file_path)

    # 处理文件的逻辑


# try:
#     file_path = "path/to/file.txt"
#     process_file(file_path)
# except FilePathError as e:
#     print(e)




