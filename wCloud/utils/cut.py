#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2024 - 2024 Sepine Tam, Inc. All Rights Reserved
#
# @Author : Sepine Tam
# @Email  : sepinetam@gmail.com
# @File   : cut.py

import jieba


def cut_text(text, stopwords):
    words = jieba.cut(text, cut_all=False)
    filtered_words = [word for word in words if word not in stopwords]
    return ' '.join(filtered_words)
