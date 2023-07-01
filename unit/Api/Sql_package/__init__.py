# -*- coding:utf-8 -*-
# !/usr/bin/env python
"""
@Project ：e-commerce
@File ：__init__.py.py
@Time ：2023/6/30 16:47
@Author ：11031840
@Motto: 理解しあうのはとても大事なことです。理解とは误解の総体に过ぎないと言う人もいますし
@File ：__init__.py功能简介：

"""
import mysql.connector


class CommerceSql():
    def __init__(self):
        pass

    # 连接到数据库
    cnx = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="hubangguo199780",
        database="e-commerce"
    )

    # 创建一个游标对象
    cursor = cnx.cursor()
    insert_query = "INSERT INTO images (name, file_path) VALUES (%s, %s)"

    # 要插入的数据
    data = [
        ("image1", "/path/to/image1.jpg"),
        ("image2", "/path/to/image2.jpg"),
        ("image3", "/path/to/image3.jpg")
    ]

    # 执行插入操作
    cursor.executemany(insert_query, data)

    # 提交更改
    cnx.commit()

    # 关闭连接
    cursor.close()
    cnx.close()
