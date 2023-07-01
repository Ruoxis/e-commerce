# -*- coding:utf-8 -*-
# !/usr/bin/env python
"""
@Project ：e-commerce
@File ：documentor.py
@Time ：2023/6/27 14:21
@Author ：11031840
@Motto: 理解しあうのはとても大事なことです。理解とは误解の総体に过ぎないと言う人もいますし
"""
import imghdr

from PIL import Image

from unit.Api.Errors import *


def is_boolean(variable, type_=bool):
    """
    类型检测
    :param variable:
    :param type_:
    :return:
    """
    return isinstance(variable, type_)


class FileType:
    def __init__(self, filename):
        @my_open_file(filename,'')
        def a(file_path=filename):
            import pandas as pd
            return pd.read_excel(file_path)

        try:
            if os.path.isfile(filename):
                self.filename = filename
            else:
                print(1)
                OSError('文件不存在')
        except OSError as e:
            print(e)

    def is_video_file(self, filename):
        """
        视频类型文件检测
        :param filename:
        :return:
        """
        image_type = imghdr.what(filename)
        return image_type and image_type.startswith('video')

    def is_image_file(self, filename):
        """
        图片类型文件检测
        :param filename:
        :return:
        """
        try:
            Image.open(filename)
            return True
        except IOError:
            return False


class FileValid:
    def __init__(self, filename, file_types=False, extension=False):
        self.filename = filename
        self.file_types = file_types
        if extension:
            pass

    def is_valid_filename(self, filename):
        # 检查是否包含禁止使用的特殊字符
        forbidden_chars = ['/', '\\', ':', '*', '?', '"', '<', '>', '|']
        for char in forbidden_chars:
            if char in filename:
                return False

        # 检查文件名长度，根据实际需求进行调整
        if len(filename) > 255:
            return False

        if is_boolean(self.file_types):
            # 检查文件扩展名，如果不需要检查扩展名，可以删除此部分
            _, file_extension = os.path.splitext(filename)
            allowed_extensions = ['.txt', '.jpg', '.mp3']  # 可接受的文件扩展名列表
            if file_extension not in allowed_extensions:
                return False

        # 检查文件夹名是否是保留字，如果不需要检查保留字，可以删除此部分
        reserved_names = ['CON', 'PRN', 'AUX']
        for reserved_name in reserved_names:
            if filename.upper() == reserved_name:
                return False

        # 所有条件通过，说明是合法的文件名或文件夹名
        return True

    # 测试
    filename1 = r'D:\file.txt'  # 合法文件名
    filename2 = 'dir123'  # 合法文件夹名
    filename3 = 'file?.txt'  # 非法文件名

    # print(is_valid_filename(filename1))  # 输出 True
    # print(is_valid_filename(filename2))  # 输出 True
    # print(is_valid_filename(filename3))  # 输出 False


video_file = 'video.mp4'  # 视频文件
image_file = 'image.jpg'  # 图片文件
#
# print(is_video_file(video_file))  # 输出 True
# print(is_video_file(image_file))  # 输出 False
FileType(image_file)
