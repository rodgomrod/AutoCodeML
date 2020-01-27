#!/usr/bin/env python
# -*- coding: utf-8 -*-


class tss(object):

    def __init__(self, file):

        self.file = file


    def create(self):

        self.file.write('## Time Series Split ##\n')
        self.file.write('from sklearn.model_selection import TimeSeriesSplit\n\n')

        self.file.write('tss = TimeSeriesSplit(n_splits=k, max_train_size=None)\n\n')

        self.file.write('fold_strategy = tscv.split(X, y)\n\n')

