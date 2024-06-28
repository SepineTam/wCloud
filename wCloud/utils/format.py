#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2024 - 2024 Sepine Tam, Inc. All Rights Reserved
#
# @Author : Sepine Tam
# @Email  : sepinetam@gmail.com
# @File   : format.py

def reformat(file_name, file_type='txt'):
    """
    re-name the file name if that is not the standard format
    :param file_name: str, file name to be renamed or adjusted
    :param file_type: str, standard type of file
    :return: str, standard file type
    """
    # from load import load_type

    # type_list: list = load_type()
    if '.' in file_name:
        name, t_type = file_name.split(".")
        # print(name, 'di', t_type)
    else:
        name = file_name
    return name, f'{name}.{file_type}'


if __name__ == '__main__':
    test_name_1, test_in_name_1 = (reformat('test.'))
    print(test_name_1, test_in_name_1)
    test_name_2, test_in_name_2 = (reformat('test.png', 'pdf'))
    print(test_name_2, test_in_name_2)
