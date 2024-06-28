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
    """
    cut text by stopwords into the type of str strip by space
    :param text: str, the text to cut
    :param stopwords: str, the stopwords for cut
    :return: str, cut text
    """
    words = jieba.cut(text, cut_all=False)
    filtered_words = [word for word in words if word not in stopwords]
    return ' '.join(filtered_words)


if __name__ == '__main__':
    from wCloud.utils import *

    cut_words = cut_text(
        (text := read_file('../../in/test.txt')),
        (stopwords := read_file('../../stop.txt'))
    )
    print(cut_words, '\n',
          'cut_words type:', '\t', type(cut_words), '\n'
          'text type:', '\t', '\t', '\t', type(text), '\n'
          'stopwords type:', '\t', type(stopwords)
          )
