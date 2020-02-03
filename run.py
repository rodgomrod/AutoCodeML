#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import os
import platform

## Operating System ##
system = platform.system()
if system == 'Windows':
    interpreter = 'python'
else:
    interpreter = 'python3'

'''
## Config ##
with open("config/test_example_conf.json", 'r') as json_conf:
    configuration = json.load(json_conf)
'''

## Run flask app ##
os.system('{0} FlaskApp/flask_app.py'.format(interpreter))

'''
## Run main file ##
os.system('{0} main.py {1} {2} {3} {4} {5} {6} {7} "{8}" {9} {10} {11} {12} {13} {14}'.format(
    interpreter,
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
'''
