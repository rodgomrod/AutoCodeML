#!/usr/bin/env python
# -*- coding: utf-8 -*-


class gkf(object):

    def __init__(self, file):

        self.file = file


    def create(self):

        self.file.write('## Group K Fold ##\n')
        self.file.write('from sklearn.model_selection import GroupKFold\n\n')

        self.file.write('group_cols = ["selection"]\n')
        self.file.write('groups = X.groupby(group_cols).grouper.group_info[0]\n')
        self.file.write('gkf = GroupKFold(n_splits=k)\n\n')

        self.file.write('fold_strategy = gkf.split(X, y, groups)\n\n')

