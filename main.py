#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2024 - 2024 Sepine Tam, Inc. All Rights Reserved
#
# @Author : Sepine Tam
# @Email  : sepinetam@gmail.com
# @File   : main.py

import sys
from wCloud import generate


def main():
    """
    Main function to generate word cloud from a text file.
    If no arguments are provided, default values are used.
    Usage: python main.py [<text_file> <stopwords_file> <font_file>]
    """

    # Default values
    text_file = "test.txt"
    stopwords_file = "stop.txt"
    font_file = "SimHei.ttf"

    # Check command line arguments
    if len(sys.argv) > 4:
        print("Usage: python main.py [<text_file> <stopwords_file> <font_file>]")
        sys.exit(1)

    # Override default values with command line arguments if provided
    if len(sys.argv) >= 2:
        text_file = sys.argv[1]
    if len(sys.argv) >= 3:
        stopwords_file = sys.argv[2]
    if len(sys.argv) == 4:
        font_file = sys.argv[3]

    # Generate word cloud
    out_path = generate(
        text_name=text_file,
        stopwords_path=stopwords_file,
        font=font_file
    )

    # Print the output path of the generated word cloud
    print(f"Generated word cloud saved to: \"{out_path}\"")


if __name__ == "__main__":
    main()
