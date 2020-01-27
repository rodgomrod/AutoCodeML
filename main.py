#!/usr/bin/env python
# -*- coding: utf-8 -*-

from methods.reading import *
from methods.preprocessing import *
from methods.feature_selection import *

class main(read, prepro):

    def __init__(self, file, data_path, separate, how_cat, how_num):

        self.file = file
        self.data_path = data_path
        self.separate = separate
        self.how_cat = how_cat
        self.how_num = how_num

        read.__init__(self, file=self.file, data_path=self.data_path, separate=self.separate)
        prepro.__init__(self, file=self.file, separate=self.separate,
                        how_cat=self.how_cat, how_num=self.how_num)

