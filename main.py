#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2024 - 2024 Sepine Tam, Inc. All Rights Reserved
#
# @Author : Sepine Tam
# @Email  : sepinetam@gmail.com
# @File   : main.py

from wCloud import generate

out_path = generate(
    text_name=(in_name := "test.txt"),
    stopwords_path='stop.txt',
    font='SimHei.ttf'
)
