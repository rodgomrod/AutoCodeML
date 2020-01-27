#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .algorithms.catboost import *
from .algorithms.lightgbm import *
from .algorithms.xgboost import *

class model(cat, xgb, lgb):

    def __init__(self, file, mode, params, alg, validation):

        self.file = file
        self.mode = mode
        self.params = params
        self.alg = alg
        self.validation = validation

        cat.__init__(self, file=self.file, mode=self.mode, params=self.params)
        xgb.__init__(self, file=self.file, mode=self.mode, params=self.params)
        lgb.__init__(self, file=self.file, mode=self.mode, params=self.params)


    def create(self):

        if self.alg == 'cat':
            cat.create_model(self)
        elif self.alg == 'xgb':
            xgb.create_model(self)
        elif self.alg == 'lgb':
            lgb.create_model(self)
        else:
            raise ValueError('{} is not in the algorithm list: ["cat", "xgb", "lgb"]'.format(self.alg))


