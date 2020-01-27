#!/usr/bin/env python
# -*- coding: utf-8 -*-

class feature_correlation(object):

    def __init__(self, file):

        self.file = file


    def select(self):
        
        self.file.write('## Linear Feature Correlation ##\n\n')
        self.file.write('corr = X_fit.corr()\n\n'
                        'list_columns_correlated = list()\n'
                        'for i, col in enumerate(corr.columns):\n'
                            '\tfor other_col in corr.index:\n'
                                '\t\tif corr[col][other_col] > 0.95 and col != other_col:\n'
                                    '\t\t\tlist_columns_correlated.append(col)\n'
                                    '\t\t\tlist_columns_correlated.append(other_col)\n\n'
                        'list_columns_correlated = list(set(list_columns_correlated))\n')