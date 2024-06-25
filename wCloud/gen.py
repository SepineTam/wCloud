#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2024 - 2024 Sepine Tam, Inc. All Rights Reserved
#
# @Author : Sepine Tam
# @Email  : sepinetam@gmail.com
# @File   : gen.py

from wordcloud import WordCloud
from matplotlib import pyplot as plt

from wCloud.utils import *


def gen_fig(text_name, stopwords_path='stop.txt', font='SimHei.ttf'):
    name, file_type = text_name.split('.')

    in_path = f'in/{text_name}'
    out_path = f'out/{name}.png'

    text = read_file(in_path)
    stopwords = load_stopwords(stopwords_path)

    word = cut_text(text, stopwords)

    wordcloud = WordCloud(
        font_path=font, width=800, height=500, background_color='white'
    ).generate(word)

    plt.figure(figsize=plt.figaspect(0.5), facecolor='white')
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.savefig(out_path)
    return out_path
