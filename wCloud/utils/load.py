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


def load_type(filepath='type'):
    """
    load type from type file
    :return: type list
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        type_list = []
        for line in f:
            type_list.append(type_i) if (type_i:=line.strip()) != "" else None
    return type_list


def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
    return text


if __name__ == '__main__':
    types = load_type()
    print(types)
