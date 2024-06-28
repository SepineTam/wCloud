#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2024 - 2024 Sepine Tam, Inc. All Rights Reserved
#
# @Author : Sepine Tam
# @Email  : sepinetam@gmail.com
# @File   : read.py

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
    return text
