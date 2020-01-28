#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import os

with open("config/test_example_conf.json", 'r') as json_conf:
    configuration = json.load(json_conf)

os.system('python main.py {0} {1} {2} {3} {4} {5} {6} "{7}" {8} {9} {10} {11} {12} {13}'.format(
    configuration["file_name"],
    configuration["data_path"],
    configuration["separate"],
    configuration["how_cat"],
    configuration["how_num"],
    configuration["how_ft_sel"],
    configuration["mode"],
    configuration["params"],
    configuration["alg"],
    configuration["how_val"],
    configuration["train_path"],
    configuration["test_path"],
    configuration["target_label"],
    configuration["drop_cols"]
))

