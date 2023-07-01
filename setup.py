# -*- coding:utf-8 -*-
# !/usr/bin/env python
"""
@Project ：e-commerce
@File ：setup.py
@Time ：2023/6/29 9:03
@Author ：11031840
@Motto: 理解しあうのはとても大事なことです。理解とは误解の総体に过ぎないと言う人もいますし
"""
from setuptools import setup, find_packages

setup(
    name="e-commerce",
    version="1.0.0",
    author="iぺ南辞丶せ",
    author_email="842750171@qq.com",
    description="A e-commerce services package",
    url="https://github.com/Ruoxis/e-commerce.git",
    packages=find_packages(),
    install_requires=[
        "requests",
        "pandas",
        "selenium",
        "PIL",
        "imghdr"
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
