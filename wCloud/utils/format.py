#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2024 - 2024 Sepine Tam, Inc. All Rights Reserved
#
# @Author : Sepine Tam
# @Email  : sepinetam@gmail.com
# @File   : format.py

def reformat(file_name, file_type='txt'):
    if file_type in file_name:
        name, t_type = file_name.split(".")
    else:
        name = file_name
    return name, name + file_type
