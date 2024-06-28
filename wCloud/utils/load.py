#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2024 - 2024 Sepine Tam, Inc. All Rights Reserved
#
# @Author : Sepine Tam
# @Email  : sepinetam@gmail.com
# @File   : load.py

def load_stopwords(filepath='stop.txt'):
    with open(filepath, 'r', encoding='utf-8') as f:
        stopwords = {line.strip() for line in f if line.strip()}
    return stopwords
