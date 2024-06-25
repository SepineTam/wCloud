#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2024 - 2024 Sepine Tam, Inc. All Rights Reserved
#
# @Author : Sepine Tam
# @Email  : sepinetam@gmail.com
# @File   : utils.py

import jieba


def load_stopwords(filepath='stop.txt'):
    with open(filepath, 'r', encoding='utf-8') as f:
        stopwords = {line.strip() for line in f if line.strip()}
    return stopwords


def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
    return text


def cut_text(text, stopwords):
    words = jieba.cut(text, cut_all=False)
    filtered_words = [word for word in words if word not in stopwords]
    return ' '.join(filtered_words)
