#!/usr/bin/env python
# -*- coding: utf-8 -*-


class skf(object):

    def __init__(self, file):

        self.file = file


    def create(self):

        self.file.write('## Stratified K Fold ##\n')
        self.file.write('from sklearn.model_selection import StratifiedKFold\n\n')

        self.file.write('skf = StratifiedKFold(n_splits=k, shuffle=True, random_state=42)\n\n')

        self.file.write('fold_strategy = skf.split(X_train, y_train)\n\n')

