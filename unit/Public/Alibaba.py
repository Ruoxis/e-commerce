# -*- coding:utf-8 -*-
# !/usr/bin/env python
"""
@Project ：资源检查
@File ：Alibaba.py
@Time ：2023/6/26 15:28
@Author ：11031840
@Motto: 理解しあうのはとても大事なことです。理解とは误解の総体に过ぎないと言う人もいますし
"""
import time
import re
# # https://detail.1688.com/offer/714617846155.html
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas
from unit.tool import Excle
# from unit import Excle
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)
driver.get('https://www.1688.com/')
driver.maximize_window()
driver.execute_script("window.open('https://detail.1688.com/offer/714617846155.html');")
driver.switch_to.window(driver.window_handles[-1])
time.sleep(2)
title_text = driver.find_element(By.CLASS_NAME, 'title-text').text
sku_button = driver.find_element(By.CLASS_NAME, 'sku-wrapper-expend-button')
driver.execute_script("arguments[0].click();", sku_button)


def get_product_information():
    pattern = r'https://\S+\.jpg'
    prop_img = driver.find_elements(By.CLASS_NAME, 'prop-img')
    prop_name = driver.find_elements(By.CLASS_NAME, 'prop-name')
    img_url = [re.search(pattern, i.get_attribute('style')).group() for i in prop_img]
    img_name = [i.get_attribute('title') for i in prop_name]
    return img_url, img_name


def get_inventory_information():
    sku_item_name = driver.find_elements(By.CLASS_NAME, 'sku-item-name')
    discountPrice_price = driver.find_elements(By.CLASS_NAME, 'discountPrice-price')
    sku_item_sale_num = driver.find_elements(By.CLASS_NAME, 'sku-item-sale-num')
    sku_item_name_ = [i.text for i in sku_item_name]
    discountPrice_price_ = [i.text for i in discountPrice_price]
    sku_item_sale_num_ = [i.text for i in sku_item_sale_num]
    return sku_item_name_, discountPrice_price_, sku_item_sale_num_


img_url, img_name = get_product_information()
sku_item_name_, discountPrice_price_, sku_item_sale_num_ = get_inventory_information()

if len(img_url) == len(img_name) and (len(sku_item_name_) == len(discountPrice_price_) == len(sku_item_sale_num_)):
    df1 = pandas.DataFrame({
        'img_url': img_url,
        'img_name': img_name
    })
    df2 = pandas.DataFrame({
        "型号名": [i for i in sku_item_name_],
        "售价": [i for i in discountPrice_price_],
        "库存数量": [i for i in sku_item_sale_num_]
    })
    exc = Excle('{}.xlsx'.format(title_text))
    exc.data_analyse_to_excel({
        "产品基本信息": df1,
        "产品库存信息": df2,
        "产品链接地址": pandas.DataFrame(
            {"链接地址": [driver.current_url]})
    })
    for index, i in enumerate(sku_item_sale_num_):
        print(sku_item_name_[index], discountPrice_price_[index], i)
